{
    'name': "Leave Request Management",
    'version': '10.0.0.0',
    'author': "A R SHAKIL",
    'category': 'Extra Tools',
    'summary':'Module for managing the Leave Request',
    'maintainer':'Odoo Mates',
    'website':'metamorphosis.com',
    'sequence':'-2',
    'license': 'AGPL-3',
    'depends': ['mail','sale','base','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/leave_type_off.xml',
        'views/leave_request.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
