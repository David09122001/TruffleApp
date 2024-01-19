# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Category_model(models.Model):
    _name='truffle_app.category_model'
    _description = 'Category Model'

    name = fields.Char(string="Name",help="Name of the category",requiered=True)
    description = fields.Char(string="Description",help="Description of the category",requiered=True)
    product = fields.One2many("truffle_app.product_model","category",string="List of products")
    parent_id = fields.Many2one("truffle_app.category_model",string="Category parent")
    subcategories = fields.One2many("truffle_app.category_model", "parent_id", string="Subcategories")