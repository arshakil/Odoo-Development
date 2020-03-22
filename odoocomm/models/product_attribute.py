# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _


class ProductAttribute(models.Model):
    _inherit = "product.attribute"
    
    chart_image = fields.Binary(string="Chart Image")

