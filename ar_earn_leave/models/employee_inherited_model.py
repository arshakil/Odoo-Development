from odoo import models, fields, api, _
from odoo import fields, models
from datetime import date, datetime
class EmployeeJoining(models.Model):
    _inherit = 'hr.employee'

    joining_date = fields.Date(string="Joining Date",)
    count_earn_days = fields.Integer(string="Annual Days", compute='get_earn_days')

    # @api.depends('joining_date')
    def get_earn_days(self):
        employee_id = self.env['hr.employee'].search([('id', '=', self.id)])
        print ('employee id is:: ', employee_id.joining_date)

        if employee_id.joining_date:
            check_earn_assign_days = self.env['earn.leave.assign'].search([])
            assign_days = check_earn_assign_days.earn_leave_days

            d1 = datetime.strptime(employee_id.joining_date, "%Y-%m-%d").date()
            d2 = datetime.now().date()
            d3 = (d2 - d1).days
            earn_leave_days=d3/assign_days
            # earn_leave_days = d3/18
            self.count_earn_days=earn_leave_days
        else:
            self.count_earn_days=0



    @api.multi
    def action_earn_leaves(self):
        print ('Button Clicked')