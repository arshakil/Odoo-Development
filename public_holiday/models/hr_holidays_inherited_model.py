from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, datetime
from datetime import datetime, timedelta
class Hr_Holidays_inherited_Model(models.Model):
    _inherit = 'hr.holidays'



    @api.model
    def create(self, vals):
        holiday_status_id=vals['holiday_status_id']

        Is_check_hr_holidays_status= self.env['hr.holidays.status'].search([('id','=',holiday_status_id),('exclude_public_holidays','=',True)])
        if Is_check_hr_holidays_status:
            if vals['date_from'] and vals['date_to']:
                count = 0;

                start_date = datetime.strptime(vals['date_from'], '%Y-%m-%d %H:%M:%S').date()
                end_date = datetime.strptime(vals['date_to'], '%Y-%m-%d %H:%M:%S').date()

                range_of_dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
                for public_holiday_date in range_of_dates:
                    check_public_holidays = self.env['public_holiday.public_holiday'].search([])
                    for pub_holiday in check_public_holidays:
                        if str(public_holiday_date)==pub_holiday.start:
                            count+=1
                        else:
                            pass
                set_count=vals['number_of_days_temp']-float(count)
                if vals['number_of_days_temp']<1:
                    vals['number_of_days_temp']=0
                else:
                    vals['number_of_days_temp']=set_count

        return super(Hr_Holidays_inherited_Model, self).create(vals)


