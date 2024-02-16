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
    path = fields.Char(string="Path", compute="_compute_path", store=True)

    @api.depends('name', 'parent_id', 'parent_id.path')
    def _compute_path(self):
        for category in self:
            path = category.name
            parent = category.parent_id
            while parent:
                path = f"{parent.name}/{path}" if parent.name else path
                parent = parent.parent_id
            category.path = path

    