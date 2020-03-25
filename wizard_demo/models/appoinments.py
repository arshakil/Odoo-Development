import pytz
from odoo import models, fields, api,  _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _order = "appointment_date desc"
    _rec_name = 'patient_id'


    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    appointment_date = fields.Date(string="Appointment Date")
