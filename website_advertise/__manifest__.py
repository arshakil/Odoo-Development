{
    'name': 'Website Advertise',
    'category': 'Website',
    'sequence': 1,
    'website': 'https://metamorphosis.com.bd/',
    'summary': 'Website,Add,Advertise',
    'version': '11.0',
    'author' : 'Metamorphosis',
    'description': """
        Adding time based advertise
        """,
    'depends': ['website','website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/website_advertise_home.xml',
        'views/website_advertise_categories.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
