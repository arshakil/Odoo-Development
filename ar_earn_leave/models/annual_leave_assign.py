from odoo import fields, models

class EmployeeJoining(models.Model):
    _name = 'earn.leave.assign'
    _description = 'Annual Leave assign days'
    _rec_name = "earn_leave_days"
    _order = "id desc"

    earn_leave_days = fields.Integer(string="Assign Earn Leave Days")