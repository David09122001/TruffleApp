# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class Invoice_model(models.Model):
    _name='truffle_app.invoice_model'
    _description = 'Invoice Model'
    _rec_name = 'reference'

     
    reference = fields.Integer(string="Reference",required=True,default=lambda self: self._get_id(),index=True,help="Invoice Reference")
    #order_reference = fields.Integer(string="Order Reference", related="lines.order.reference", readonly=True, copy=False)

    date = fields.Date(string="Emited date",required=True,default=datetime.now(),help="Date")
    base = fields.Float(string="Base",compute="_calculate_base",help="DNI for Client", store=True)
    vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')], default='0',help="VAT for this invoice")
    total = fields.Float(string="Total",compute="_calculate_total",help="Total invoice",store=True)
    lines = fields.One2many("truffle_app.line_model","reference",string="Lines")
    client = fields.Many2one("res.partner", string="Client")
    active = fields.Boolean(string="Historical invoices",default=True)
    stateConf = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed')], default="D")

    def _get_id(self):
        if not self.env['truffle_app.invoice_model'].search([]):
            return 1
        return self.env['truffle_app.invoice_model'].search([], order='id desc', limit=1).id + 1

    @api.depends('lines')
    def _calculate_base(self):
        for rec in self:
            rec.base = sum(line.price for line in rec.lines)

    @api.depends('base', 'vat')
    def _calculate_total(self):
        self.total =self.base + (self.base*int(self.vat)/100)

    def confirmInvoice(self):
        self.stateConf = 'C'
        

    def set_all_invoices_active(self):
        # Set active=False for all invoices 
        # Añadir tambien las I
        confirmed_orders = self.search([('stateConf', '=', 'C')])
        confirmed_orders.write({'active': False})

        # Set active=True for the new invoices
        new_invoices = self.search([('stateConf', '=', 'D')])
        new_invoices.write({'active': True})


        

    