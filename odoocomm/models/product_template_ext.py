# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class ProductTemplateExtended(models.Model):
    _inherit = "product.template"
    _description = 'Product Template'
    
    image_size_chart = fields.Binary(string="Size Chart Image")
    # product_offer_ids = fields.Many2many('product.offer', string="Offers")

