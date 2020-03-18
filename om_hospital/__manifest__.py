{
    'name': "Hospital Management",
    'version': '12.0.0.0',
    'author': "A R SHAKIL",
    'category': 'Extra Tools',
    'summary':'Module for managing the hospital',
    'maintainer':'Odoo Mates',
    'website':'metamorphosis.com',
    'sequence':'10', 
    'license': 'AGPL-3',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/appointment.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

 
}
