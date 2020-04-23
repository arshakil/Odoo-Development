# -*- coding: utf-8 -*-
{
    'name': "Employee Appraisal",

    'summary': """
    This is module is used to record and monitor periodic Employee Appraisal for each employee
    """,

    'description': """
    Employee Appraisal
    """,

    'author': "Metamorphosis",
    'website': "https://metamorphosis.com.bd",
    'sequence': '1',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','hr','survey'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/survey_inherited_appraisal_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}