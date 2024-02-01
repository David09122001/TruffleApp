# -*- coding: utf-8 -*-
{
    'name': "truffle_app",

    'summary': """
        App to sell truffles and more related things""",

    'description': """
        App to sell truffles and more related things
    """,

    'author': "David",
    'website': "https://www.truffleapp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_view.xml',
        'views/quality_view.xml',
        'views/weight_view.xml',
        'views/category_view.xml',
        'views/line_view.xml',
        'views/lineorder_view.xml',
        'views/invoice_view.xml',
        'views/order_view.xml',
        'views/menu.xml'
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
