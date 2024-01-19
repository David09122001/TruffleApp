from odoo import models, fields,api

class Weight_model(models.Model):
    _name='truffle_app.weight_model'
    _description = 'Weight Model'
    _rec_name = 'weight'

   

    weight = fields.Integer(string="Weight", help="Weight of the product in grams")
    category = fields.Many2one("truffle_app.category_model",string="Category",requiered=True)
    Unit = fields.Selection(string="Unit",selection=[('liters', 'Liters'), ('grams', 'Grams'), ('kilograms', 'Kilograms')],default='grams',help="The unit of the weight")