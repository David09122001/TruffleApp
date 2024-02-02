from odoo import models, fields,api

class Product_model(models.Model):
    _name='truffle_app.product_model'
    _description = 'Product Model'

    name = fields.Char(string="Name",help="Name of the product",requiered=True)
    photo = fields.Binary()
    price = fields.Float(string="Price €")
    description = fields.Text(string="Description",help="Description of the product",requiered=True)
    category = fields.Many2one("truffle_app.category_model",string="Category",requiered=True)
    quality  = fields.Many2one("truffle_app.quality_model", string="Quality",requiered=True)
    weight = fields.Many2one("truffle_app.weight_model", string="Weight",requiered=True)
    stock = fields.Integer(string="Stock")
    unit = fields.Selection(
        string="Unit",
        selection=[('liters', 'Liters'), ('grams', 'Grams'), ('kilograms', 'Kilograms')],
        related="weight.Unit",
        readonly=True,
        store=True,
    )
    category_path = fields.Char(string="Category Path", related="category.path", readonly=True, store=True)