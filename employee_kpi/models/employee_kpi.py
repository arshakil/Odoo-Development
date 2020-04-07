# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime
class Employee_kpi(models.Model):
    _name = 'employee_kpi.employee_kpi'
    _description = 'Employee KPI'
    _rec_name = "employee_id"
    _order = "id asc"


    employee_id = fields.Many2one('hr.employee', string='Employee', required="1")
    job_title = fields.Many2one('hr.job', string='Job Title',required="1")
    department = fields.Char(related="employee_id.department_id.name", string='Department',required="1")
    # year = fields.Date(string="Year",required="1")
    valid_from = fields.Date(string="Valid From",required="1")
    valid_to = fields.Date(string="Valid To", required="1")
    employee_kpi_lines = fields.One2many('employee_kpi.lines', 'employee_kpi_id', string='Employee KPI Lines',)

    state = fields.Selection([
        ('draft', "Draft"),
        ('approved', "Approved"),
        ('refuse', "Refuse"),], string="Status", default='draft')

    def action_approved(self):
        self.state = "approved"
    def action_refuse(self):
        self.state = "refuse"

    def action_cancel(self):
        self.state = "draft"


    # changing kpi dynamically
    @api.onchange('job_title')
    def _LoadedAllKPI(self):
        kpi_lines=[]
        job_title_ids = self.env['employee_kpi.assign'].search([('job_title.id', '=', self.job_title.id)])
        # print('bundle_product_ids',job_title_ids)
        for kpi in job_title_ids:
            # print('kpi_title', str(kpi.kpi_title))
            line = (0,0,{
                'kpi_title':kpi.id
            })
            kpi_lines.append(line)
        self.employee_kpi_lines=kpi_lines


    @api.model
    def create(self, vals):
        result = super(Employee_kpi, self).create(vals)
        if not result.employee_kpi_lines:
            raise ValidationError(_('You can\'t Create because you didn\'t Assign any KPI!!, OR Please create KPI first for this job title'))

        # validation check for date
        valid_from = datetime.strptime(vals['valid_from'], '%Y-%m-%d')
        valid_to = datetime.strptime(vals['valid_to'], '%Y-%m-%d')
        total_days = valid_to - valid_from
        days_is = int(total_days.days)+1
        if days_is < 1:
            raise ValidationError("You can\'t select that date!!, You have selected: %s" % total_days.days + " days"+" and Please check your Valid To field")

        return result


    @api.multi
    def unlink(self):
        print ('delete is called')
        for kpi in self:
           if kpi.state in ('refuse'):
              raise ValidationError(_('You cannot delete KPI which is not draft State. You should change the state from Refuse to Draft.'))
           elif kpi.state in ('approved'):
              raise ValidationError(_('You cannot delete an KPI after it has been Approved. You can set it back to "Draft" state and delete it\'s content'))
        return super(Employee_kpi, self).unlink()



class Employee_kpi_lines(models.Model):
    _name = 'employee_kpi.lines'
    _description = 'Employee KPI Lines'
    _rec_name = "kpi_title"
    _order = "id asc"


    # kpi_title = fields.Many2one('employee_kpi.assign', string="KPI Title")
    kpi_title = fields.Many2one('employee_kpi.assign', string="KPI Title", inverse='_inverse_upper_name',)
    measurement = fields.Char(string="Measurement")
    target = fields.Float(string="Target", digits=(12,2))
    actual = fields.Float(string="Actual")
    unit = fields.Char(string="Unit")
    employee_kpi_id = fields.Many2one('employee_kpi.employee_kpi', string='Employee KPI Assign',ondelete='cascade')




    # for individual kpi change kpi_title = fields.Many2one('employee_kpi.assign', string="KPI Title", inverse='_inverse_upper_name')
    @api.onchange('employee_kpi_id')
    def _inverse_upper_name(self):
        job_title_ids = self.env['employee_kpi.assign'].search([('job_title.id', '=', self.employee_kpi_id.job_title.id)])
        # print('bundle_product_ids',job_title_ids)
        return {'domain': {'kpi_title': [('id', 'in', job_title_ids.ids)]}}


class Employee_kpi_assign(models.Model):
    _name = 'employee_kpi.assign'
    _description = 'Employee KPI Assign'
    _rec_name = "kpi_title"
    _order = "id asc"

    job_title = fields.Many2one('hr.job', string='Job Title', required="1")
    kpi_title = fields.Char(string="KPI Title", required="1")



    @api.multi
    def unlink(self):
        job_title_id_exist = self.env['employee_kpi.lines'].search([('kpi_title.id', '=', self.id)])
        if job_title_id_exist:
            raise ValidationError(_('You cannot delete an KPI after it has been Used. You have to delete used KPI first then you can delete it.'))
        else:
            return super(Employee_kpi_assign, self).unlink()

