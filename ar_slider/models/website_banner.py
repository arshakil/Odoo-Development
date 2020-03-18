from odoo import fields,models,api, _
from datetime import timedelta, datetime

class WebsiteBannerSetup(models.Model):
    _name = 'website.slide'
    
    
    name = fields.Char(string="Title")
    image = fields.Binary(string="Image")




