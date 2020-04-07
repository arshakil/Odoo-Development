# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

class PublicHolidays(models.Model):
    _name = 'public_holiday.public_holiday'
    _rec_name = 'title'

    title = fields.Char(string='Holiday Title', required="True")
    start = fields.Date(string='Start holiday', required="True")
    end = fields.Date(string='End holiday', required="True")
    total_days=fields.Float(string='Total Days', compute="calculate_days")


    @api.model
    def create(self, vals):

        title=vals['title']
        start_date=str(vals['start'])
        end_date=str(vals['end'])
        date_start = datetime.strptime(start_date, "%Y-%m-%d").date()
        date_end = datetime.strptime(end_date, "%Y-%m-%d").date()

        # total_days = (date_start - date_end).days

        range_of_dates = [date_start + timedelta(days=x) for x in range((date_end-date_start).days + 1)]
        if range_of_dates:
            for public_holiday_date in range_of_dates:
                pub_holiday_id = super(PublicHolidays, self).create({
                        'title':title,
                        'start':str(public_holiday_date),
                        'end':str(public_holiday_date)
                })
        return pub_holiday_id



    @api.onchange('start', 'end','total_days')
    def calculate_days(self):
        if self.start and self.end:
            start_date=datetime.strptime(str(self.start),'%Y-%m-%d')
            end_date=datetime.strptime(str(self.end),'%Y-%m-%d')

            # when field is DateTime used this format
            # d1 = datetime.strptime(str(self.start_date), '%Y-%m-%d %H:%M:%S')
            # d2 = datetime.strptime(str(self.end_date), '%Y-%m-%d %H:%M:%S')

            total=end_date-start_date
            total_days=int(total.days)

            if total_days<0:
                raise ValidationError("You can\'t select holiday less then 1 day but you have selected: %s" %total_days +" day. Please change your date Again !!!!")
            else:
                self.total_days=total_days+1





