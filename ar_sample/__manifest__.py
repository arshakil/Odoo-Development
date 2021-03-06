{
    'name': "Sample Management",
    'version': '12.0.0.0',
    'author': "A R SHAKIL",
    'category': 'Extra Tools',
    'summary':'Module for managing the Sample',
    'maintainer':'Odoo Mates',
    'website':'metamorphosis.com',
    'sequence':'11', 
    'license': 'AGPL-3',
    'depends': ['mail', 'purchase',],
    'data': [
        'security/ir.model.access.csv',
        'views/manufacturer.xml',
        'views/productgenerator.xml',
        'views/samplebooking.xml',
        'reports/report.xml',
        'reports/booking_card.xml',
        'views/purchase_order_inherit_view.xml',
        
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
