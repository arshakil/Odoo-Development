# -*- coding: utf-8 -*-
{
    'name': "public_holidays",

    'summary': """
        This is module is used to record and monitor public holidays of employees.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Metamorphosis",
    'website': "https://metamorphosis.com.bd",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_holidays'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/public_holidays_view.xml',
        'views/hr_holidays_status_inherited_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}