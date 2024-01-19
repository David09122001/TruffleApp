# -*- coding: utf-8 -*-
# from odoo import http


# class TruffleApp(http.Controller):
#     @http.route('/truffle_app/truffle_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/truffle_app/truffle_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('truffle_app.listing', {
#             'root': '/truffle_app/truffle_app',
#             'objects': http.request.env['truffle_app.truffle_app'].search([]),
#         })

#     @http.route('/truffle_app/truffle_app/objects/<model("truffle_app.truffle_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('truffle_app.object', {
#             'object': obj
#         })
