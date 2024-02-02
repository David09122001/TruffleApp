# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LineorderModel(models.Model):
    _name='truffle_app.lineorder_model'
    _description = 'Line Order Model'

    order = fields.Many2one("truffle_app.order_model", string="Order reference")
    product = fields.Many2one("truffle_app.product_model", string="Product", required=True)
    weight = fields.Integer(string="Weight", help="Total weight of the product")
    quantity = fields.Integer(string="Quantity", help="Quantity of the product.", required=True)
    price = fields.Float(string="Price", compute="_compute_price", help="Price of the product.")
    unit_price = fields.Float(string="Unit price", help="Unit price of the product.")
    unit = fields.Selection(string="Unit", related="product.unit", readonly=True, store=True)

    @api.onchange('product')
    def _onchange_product(self):
        self.unit_price = self.product.price

    @api.onchange('quantity')
    def _onchange_quantity(self):
        if self.quantity and self.product.weight.weight != 0:
            self.weight = self.quantity * self.product.weight.weight
        else:
            self.weight = 0

    @api.onchange('unit_price')
    def _onchange_unit_price(self):
        self._compute_price()

    @api.depends('quantity', 'product.weight.weight')
    def _compute_price(self):
        for line in self:
            if line.product and line.product.weight.weight != 0:
                weight = line.product.weight.weight
                price_product = line.unit_price

                if line.quantity > line.product.stock:
                    raise ValidationError("The quantity exceeds the available stock for the product.")

                line.weight = line.quantity * line.product.weight.weight
                line.price = (line.weight / weight) * price_product
            else:
                line.price = 0
