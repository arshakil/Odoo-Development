# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class ProductOffer(models.Model):
    _name = "product.offer"
    _description = 'Product Offer'
    
    image = fields.Binary(string='Image')
    name = fields.Char(string='Name', required = True)
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Active', default = 'True', required = True)
    product_ids = fields.Many2many('product.template', 'offer_product', 'offer_id', 'product_id', string='Products')

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Name already exists.')
    ]

