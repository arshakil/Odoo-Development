# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class UserExtended(models.Model):
    _inherit = "res.users"
    _description = 'User'
    
    contact_number = fields.Char(string="Contact Number")
    email_address = fields.Char(string="Email")
    facebook_token = fields.Char(string="Facebook Token")
    gmail_token = fields.Char(string="Gmail Token")
    token_status = fields.Char(string="Token Status")
    is_agent = fields.Boolean(string="Is Agent")
    pin = fields.Integer(string="PIN")
