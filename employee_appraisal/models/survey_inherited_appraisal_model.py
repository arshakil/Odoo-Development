from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Survey_Inherited_Appraisal_Model(models.Model):
    _inherit = 'survey.survey'

    employee_id = fields.Many2one('hr.employee', string='Employee')
    manager_id = fields.Many2one('hr.employee', string='Manager',)
    subordinates_id = fields.Many2one('hr.employee', string='Subordinates',)
    colleagues_id = fields.Many2one('hr.employee', string='Colleagues',)
    appraisal_deadline = fields.Date(string="Appraisal Deadline")
    # company_id = fields.Many2one(related='employee_id.address_id', string='Company',)
    company_id = fields.Many2one('res.company', string='Company')

    mail_to_employee_ischecked = fields.Boolean(string="Mail To Employee")
    # mail_to_employee_text = fields.Html(string='Mail To Employee')
    mail_to_employee_text = fields.Html(string='Mail To Employee',  default=lambda self: self._get_default_employee_text())

    mail_to_manager_ischecked = fields.Boolean(string="Mail To Manager")
    # mail_to_manager_text = fields.Html(string='Mail To Manager')
    mail_to_manager_text = fields.Html(string='Mail To Manager',  default=lambda self: self._get_default_manager_text())

    mail_to_subordinates_ischecked = fields.Boolean(string="Mail To Subordinates")
    # mail_to_subordinates_text = fields.Html(string='Mail To Subordinates')
    mail_to_subordinates_text = fields.Html(string='Mail To Subordinates', default=lambda self: self._get_default_subordinates_text())

    mail_to_colleagues_ischecked = fields.Boolean(string="Mail To Colleagues")
    # mail_to_colleagues_text = fields.Html(string='Mail To Colleagues')
    mail_to_colleagues_text = fields.Html(string='Mail To Colleagues', default=lambda self: self._get_default_colleagues_text())


    # mail body text
    mail_content = "An appraisal was requested.<br>" \
                   "Please schedule an appraisal date together.<br>" \
                   "Hereunder, you will find the link towards the Performance appraisal form: <br>" \
                   "The employee copy the document and complete his part, then share the document with the manager with edition right in order for him to complete his part.<br>" \
                   "<br>Thank you!" \
                   "<br>The HR department"

    # mail body text function
    @api.model
    def _get_default_employee_text(self):
        return self.mail_content
    def _get_default_manager_text(self):
        return self.mail_content
    def _get_default_subordinates_text(self):
        return self.mail_content
    def _get_default_colleagues_text(self):
        return self.mail_content


    @api.model
    def create(self, vals):
        result = super(Survey_Inherited_Appraisal_Model, self).create(vals)

        context = self._context
        current_uid = context.get('uid')
        user = self.env['res.users'].browse(current_uid)

        # print ('User is: ',user.name)
        # print ('User Email is: ', user.email)
        # print ('mail_to_employee_ischecked',vals['mail_to_employee_ischecked'])
        #

        # MAIL TO EMPLOYEE
        if vals['employee_id'] and vals['mail_to_employee_ischecked']:
            id = vals['employee_id']
            employee_id = self.env['hr.employee'].search([('id', '=', id)], limit=0)

            # print ("Employee Id",id)
            # print ("Employee", employee_id)
            # print ("Employee", employee_id.work_email)
            # print ("mail_to_employee_ischecked",vals['mail_to_employee_ischecked'])

            # SEND EMAIL
            template_obj = self.env['mail.mail']
            template_data = {
                'subject': 'An Employee Appraisal Was Requested',
                'body_html': vals['mail_to_employee_text'],
                'email_from': user.email,
                'email_to': employee_id.work_email,
                'auto_delete': True,
                'state': 'outgoing',
                # 'email_to': 'shakil.ahmed363410@gmail.com'
            }
            if user.email and employee_id.work_email:
                template_id = template_obj.create(template_data)
                template_obj.send(template_id)
            else:
                raise ValidationError("Please check Employee email receiving address can't be empty ")


        # MAIL TO MANAGER
        if vals['manager_id'] and vals['mail_to_manager_ischecked']:
            id = vals['manager_id']
            manager_id = self.env['hr.employee'].search([('id', '=', id)], limit=0)

            # SEND EMAIL
            template_obj = self.env['mail.mail']
            template_data = {
                'subject': 'An Manager Appraisal Was Requested',
                'body_html': vals['mail_to_manager_text'],
                'email_from': user.email,
                'email_to': manager_id.work_email,
                'auto_delete': True,
                'state': 'outgoing',
                # 'email_to': 'shakil.ahmed363410@gmail.com'
            }
            if user.email and employee_id.work_email:
                template_id = template_obj.create(template_data)
                template_obj.send(template_id)
            else:
                raise ValidationError("Please check Manager email receiving address can't be empty ")


        # MAIL TO SUBORDINATES
        if vals['subordinates_id'] and vals['mail_to_subordinates_ischecked']:
            id = vals['subordinates_id']
            subordinates_id = self.env['hr.employee'].search([('id', '=', id)], limit=0)

            # SEND EMAIL
            template_obj = self.env['mail.mail']
            template_data = {
                'subject': 'An Subordinates Appraisal Was Requested',
                'body_html': vals['mail_to_subordinates_text'],
                'email_from': user.email,
                'email_to': subordinates_id.work_email,
                'auto_delete': True,
                'state': 'outgoing',
                # 'email_to': 'shakil.ahmed363410@gmail.com'
            }
            if user.email and employee_id.work_email:
                template_id = template_obj.create(template_data)
                template_obj.send(template_id)
            else:
                raise ValidationError("Please check Subordinates email receiving address can't be empty ")



        # MAIL TO COLLEAGUES
        if vals['colleagues_id'] and vals['mail_to_colleagues_ischecked']:
            id = vals['colleagues_id']
            colleagues_id = self.env['hr.employee'].search([('id', '=', id)], limit=0)

            # SEND EMAIL
            template_obj = self.env['mail.mail']
            template_data = {
                'subject': 'An Colleagues Appraisal Was Requested',
                'body_html': vals['mail_to_colleagues_text'],
                'email_from': user.email,
                'email_to': colleagues_id.work_email,
                'auto_delete': True,
                'state': 'outgoing',
            }
            if user.email and employee_id.work_email:
                template_id = template_obj.create(template_data)
                template_obj.send(template_id)
            else:
                raise ValidationError("Please check Colleagues email receiving address can't be empty ")

        return result







