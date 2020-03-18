from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo import fields, models
from datetime import date, datetime

class Holidays_inherited_Model(models.Model):
    _inherit = 'hr.holidays'


    @api.onchange('holiday_status_id','employee_id')
    def check_leave_type(self):
        if str(self.holiday_status_id.name) == "Earn Leaves":
            check_earn_assign_days = self.env['earn.leave.assign'].search([])
            print ('Assign Days is : ',check_earn_assign_days.earn_leave_days)
            assign_days = check_earn_assign_days.earn_leave_days

            for record in self:
                if record.employee_id.joining_date:
                    d1 = datetime.strptime(record.employee_id.joining_date, "%Y-%m-%d").date()
                    d2 = datetime.now().date()
                    d3 = (d2 - d1).days
                    earn_leave=d3/assign_days
                    # earn_leave = d3/18

                    check_earn_leave = self.env['hr.holidays'].search([("employee_id", "=", record.employee_id.id), ("holiday_status_id", "=", record.holiday_status_id.id),('type', '=', 'add')])
                    if check_earn_leave:
                        for val in check_earn_leave:
                            if earn_leave>val.number_of_days_temp:
                                print('need update')
                                val.number_of_days_temp=earn_leave
                                val.number_of_days=earn_leave
                            else:
                                print('no need to update please continue')

                    else:
                        holiday_status_id=record.holiday_status_id.id
                        employee_id=record.employee_id.id
                        holiday_type="employee"
                        number_of_days_temp=earn_leave
                        state="validate"
                        manager_id=1
                        type="add"
                        department_id=record.department_id.id
                        number_of_days=earn_leave

                        # current user
                        context = self._context
                        current_uid = context.get('uid')
                        user_id = self.env['res.users'].browse(current_uid).id

                        create_earn_leave = self.env['hr.holidays'].browse(self.env.context.get('active_ids', []))
                        create_earn_leave.create({'holiday_status_id': holiday_status_id,
                                                  'employee_id': employee_id,
                                                  'holiday_type': holiday_type,
                                                  'number_of_days_temp': number_of_days_temp,
                                                  'state': state,
                                                  'manager_id': manager_id,
                                                  'type': type,
                                                  'department_id': department_id,
                                                  'number_of_days': number_of_days,
                                                  })
        else:
            print ("Other Leaves")
