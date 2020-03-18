{
    'name': 'Image Slider',
    'category': 'Website',
    'sequence': -1,
    'website': 'https://metamorphosis.com.bd/',
    'summary': 'Website,Banner,Image Slider',
    'version': '11.0',
    'author' : 'Metamorphosis',
    'description': """
        Adding time based website banner
        """,
    'depends': ['website',],
    'data': [
        'security/ir.model.access.csv',
        'views/website_banner.xml',
        'views/website_banner_templates.xml',
        'views/slider.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
