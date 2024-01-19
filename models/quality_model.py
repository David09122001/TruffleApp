from odoo import models, fields,api

class Quality_model(models.Model):
    _name='truffle_app.quality_model'
    _description = 'Quality Model'
   

    name = fields.Char(string="Name",help="Name of the quality",requiered=True)
    category = fields.Many2one("truffle_app.category_model",string="Category",requiered=True)