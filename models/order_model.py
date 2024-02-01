# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class Order_model(models.Model):
    _name='truffle_app.order_model'
    _description = 'Order Model'
    _rec_name = 'reference'

    reference = fields.Integer(string="Reference",required=True,default=lambda self: self._get_id(),index=True,help="Order Reference")
   #invoiceReference =  
    date = fields.Date(string="Emited date",required=True,default=datetime.now(),help="Date")
    base = fields.Float(string="Base",compute="_calculate_base",help="DNI for Client", store=True)
    vat = fields.Selection(string="VAT",selection=[('0','0'),('4','4'),('10','10'),('21','21')], default='0',help="VAT for this invoice")
    total = fields.Float(string="Total",compute="_calculate_total",help="Total invoice",store=True)
    lines = fields.One2many("truffle_app.lineorder_model","order",string="Lines")
    client = fields.Many2one("res.partner", string="Client")
    active = fields.Boolean(string="Historical orders",default=True)
    stateConf = fields.Selection(string="Status",selection=[('D','Draft'),('C','Confirmed')], default="D")
    stateInvo = fields.Selection(string="Status",selection=[('C','Confirmed'),('I','Invoiced')], default="C")

    def _get_id(self):
        if not self.env['truffle_app.order_model'].search([]):
            return 1
        return self.env['truffle_app.order_model'].search([], order='id desc', limit=1).id + 1

    @api.depends('lines')
    def _calculate_base(self):
        for rec in self:
            rec.base = sum(line.price for line in rec.lines)

    @api.depends('base', 'vat')
    def _calculate_total(self):
        self.total =self.base + (self.base*int(self.vat)/100)

    def confirmConfirmed(self):
        # Verificar si la orden ya está confirmada
        if self.stateConf == 'C':
            raise ValidationError("Order is already confirmed.")
        
        # Cambiar el estado de la orden a 'Confirmed'
        self.stateConf = 'C'

        # Crear una nueva factura
        invoice_vals = {
            'date': self.date,
            'base': self.base,
            'vat': self.vat,
            'lines': [(0, 0, {
                'product': line.product.id,
                'quantity': line.quantity,
                'price': line.price,
            }) for line in self.lines],
            'client': self.client.id,
        }

        new_invoice = self.env['truffle_app.invoice_model'].create(invoice_vals)

      
        return new_invoice


    def confirmInvoiced(self):
        if self.stateConf == 'C':
            self.stateInvo = 'I'
        else:
            raise ValidationError("Cannot set to 'Invoiced' without confirming first.")
        
    def set_all_invoices_active(self):
        # Set active=False for all invoices
        confirmed_orders = self.search([('stateInvo', '=', 'I')])
        confirmed_orders.write({'active': False})

        # Set active=True for the new invoices
        new_invoices = self.search([('stateConf', '=', 'D')])
        new_invoices.write({'active': True})
