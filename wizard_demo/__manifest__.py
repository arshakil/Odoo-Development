{
    'name': 'wizard demo',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'wizard test',
    'sequence': '-1',
    'license': 'AGPL-3',
    'author': 'A R SHAKIL',
    'maintainer': 'A R SHAKIL',
    'website': 'odoomates.com',
    'live_test_url': '',
    'depends': ['base',],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'wizards/create_appointment.xml',
        'views/patients.xml',
        'views/appointment.xml',


    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
# Video Explanation: https://www.youtube.com/watch?v=BDepk0LhVuI&list=PLqRRLx0cl0hoJhjFWkFYowveq2Zn55dhM&index=1