from odoo import fields, models

class EmployeeJoining(models.Model):
    _name = 'annual.leave.assign'
    _description = 'Annual Leave assign days'
    _rec_name = "annual_leave_days"
    _order = "id desc"

    annual_leave_days = fields.Integer(string="Assign Annual Leave Days")