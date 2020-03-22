from odoo import fields,models,api, _,tools
from datetime import timedelta, datetime
from PIL import Image
from odoo.tools import image_resize_images
class WebsiteAdvertiseHome(models.Model):
    _name = 'website.advertise.home'
    _rec_name = 'url'
    # _order = "order desc"


    order = fields.Integer('Order', required=True,)
    url = fields.Char(string="Url", required=True,)
    image = fields.Binary(string="Image", required=True,)
    active = fields.Boolean('Active', default=True)

