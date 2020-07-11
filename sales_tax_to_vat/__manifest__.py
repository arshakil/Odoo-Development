{
    'name': "Sales Tax To VAT",

    'summary': """ Sales Tax To VAT""",

    'description': """
        Quotations, Sales Orders, Sales renaming Tax To VAT.
    """,

    'author': "Metamorphosis",
    'website': "https://metamorphosis.com.bd",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'reports/report.xml',
        'views/sale_tax_to_vat.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
