# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoocomm',
    'summary': """Extension for Odoo Commerce mobile apps""",
    'description': """

Odoo Commerce
=============
Integrate some essential features for Odoo Commerce mobile apps.
    """,
    'version': '11.0.1.0',
    'author': 'Metamorphosis',
    'company': 'Metamorphosis Limited',
    'website': 'metamorphosis.com.bd',
    'category': 'Tools',
    'sequence': 1,
    'depends': ['base', 'product', 'contacts','website','payment',],
    'data': [
        'views/product_template_form.xml',
        'views/product_offer.xml',
        'views/user_form.xml',
        'views/product_attribute_view.xml',
        'views/payment_transaction.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'icon': "/odoocomm/static/description/icon.png",
    "images": ["/static/description/banner.png"],
    "license": "OPL-1",
    "price": 0,
    "currency": "EUR",
}
