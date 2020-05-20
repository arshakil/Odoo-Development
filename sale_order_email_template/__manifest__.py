{
    'name': "Sale Order Email Template",
    'version': '11.0.0.0',
    'author': "Metamorphosis",
    'category': 'Extra Tools',
    'summary':'Module for Sending an email automatically after an order',
    'maintainer':'Metamorphosis',
    'website':'metamorphosis.com',
    'sequence':'-1',
    'license': 'AGPL-3',
    'depends': ['mail','sale','base','base_automation'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/earn_leave.xml',
        'data/order_email_template.xml',

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
