# -*- coding: utf-8 -*-
{
    'name': "HR Public Holiday",

    'summary': """
        This is module is used to record and monitor public holidays of employees.
        """,

    'description': """
        HR Public Holiday Module mainly tracking the holidays from holidays calendar. When a employee request for a leave at that time it\'show leave request days and also if in between those days has a public leave it'\s show public holiday """,

    'author': "Metamorphosis",
    'website': "https://metamorphosis.com.bd",
    'sequence': '1',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/public_holidays_view.xml',
        'views/hr_holidays_status_inherited_view.xml',
        'views/hr_holidays_inherited_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/cover.png'],
    'icon': "/public_holiday/static/description/icon.png",
    'license': "",
    'installable': True,
    'application': True,
    "license": "OPL-1",
    'price':00.0,
    'currency':'EUR',
}