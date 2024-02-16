#-*- coding: utf-8 -*-
from odoo import http
import json  
from odoo.http import request  

class TruffleApp(http.Controller):

    @http.route(['/truffle_app/getProduct', '/truffle_app/getProduct/<int:prodid>'], auth='public', type="http", methods=['GET'])
    def getProduct(self, prodid=None, **kw):
        if prodid:
            domain = [("id", '=', prodid)]
        else:
            domain = []
        fields = ["name", "price", "description", "category", "quality", "weight", "stock", "unit", "category_path"]
        proddata = request.env["truffle_app.product_model"].sudo().search_read(domain, fields)
        

        data = {"status": 200, "data": proddata}
        return request.make_response(json.dumps(data), headers={'Content-Type': 'application/json'})

    @http.route(['/truffle_app/getOrder', '/truffle_app/getOrder/<int:orderid>'], auth='public', type="http", methods=['GET'])
    def getOrder(self, orderid=None, **kw):
        if orderid:
            domain = [("id", '=', orderid)]
        else:
            domain = []
        fields = ["reference","invoice_reference", "date","base", "vat", "total","lines","client","active", "state"]
        orderdata = request.env["truffle_app.order_model"].sudo().search_read(domain, fields)

        for order in orderdata:
            if order.get('date'):
                order['date'] = order['date'].strftime('%Y-%m-%d')

        data = {"status": 200, "data": orderdata}
        return request.make_response(json.dumps(data), headers={'Content-Type': 'application/json'})

    

    @http.route(['/truffle_app/getCategory', '/truffle_app/getCategory/<int:catid>'], auth='public', type="http", methods=['GET'])
    def getCategory(self, catid=None, **kw):
        if catid:
            domain = [("id", '=', catid)]
        else:
            domain = []
        fields = ["name", "description", "product", "parent_id", "subcategories", "path"]
        categorydata = request.env["truffle_app.category_model"].sudo().search_read(domain, fields)

        data = {"status": 200, "data": categorydata}
        return request.make_response(json.dumps(data), headers={'Content-Type': 'application/json'})


