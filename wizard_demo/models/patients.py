# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, _
from odoo.exceptions import UserError


class HospitalPatient(models.Model):
    """ Defines bills of material for a product or a product template """
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _rec_name = 'name'
    _order = "id desc"

    name = fields.Char(string='Patient Name', required="1")
    patient_age = fields.Integer(string='Age')
    date = fields.Date(string='Date')
    description = fields.Text(string='Description')




