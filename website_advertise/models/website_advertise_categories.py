from odoo import fields,models,api, _,tools
from datetime import timedelta, datetime
from PIL import Image
from odoo.tools import image_resize_images
class WebsiteAdvertiseCategories(models.Model):
    _name = 'website.advertise.categories'
    _rec_name = 'url'
    # _order = "order desc"


    order = fields.Integer('Order', required=True,)
    url = fields.Char(string="Url", required=True,)
    image = fields.Binary(string="Image", required=True,)
    active = fields.Boolean('Active', default=True)
    category_id = fields.Many2one('product.public.category', string='Category')
    destination = fields.Selection([
        ('app', 'app'),
        ('web', 'web'),
    ], 'Destination', default='app', required=True)




