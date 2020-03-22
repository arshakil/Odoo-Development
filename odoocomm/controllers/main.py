from odoo import http,models, fields, api, _
import json

from odoo import http
from odoo.http import Response
from odoo.service import model
import json
import werkzeug
import urllib
from datetime import datetime, timedelta
from odoo.addons.web.controllers.main import WebClient
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.http import request
from odoo import tools, SUPERUSER_ID
from odoo.exceptions import UserError
import odoo
import sys
import logging
import binascii
import requests

class OdooCommController(http.Controller):
    _inherit = 'product.job_line'
    value = fields.Float()
    journal_entry = fields.Many2one('account.move')
    cost = fields.Float()

    @http.route(['/restapi/1.0/object/check_agent'])
    def set_file(self, agent_id):
        agent_id = int(agent_id)
        agent_exist = request.env['res.users'].search([('id', '=', agent_id)])
        if str(agent_exist.id) != 'False':
            is_agent = True
        else:
            is_agent = False
        return self.get_response(200, '200', {
            "agent_exist": is_agent,
        })

    def get_response(self, status_code, status, data=None):
        """Returns Response Object with given status code and status"""
        response = Response()
        response.status = status
        if data:
            try:
                response.data = isinstance(data, str) and data or json.dumps(data)
            except Exception as e:
                response.data = str(data)
        response.status_code = status_code
        return response

    @http.route('/api/create_car_request',auth='public')
    def create_car_request(self, **kw):
        return "The car request has been created"


    @http.route('/api/create_account_move_line',auth='public')
    def create_car_request(self, **kw):
        if self.is_finish:
            revenue_account = self.product.revenue_account
            deferred_receivable_account = self.env['ir.values'].get_default('job.config.settings','deferred_receivable_account')
            journal = self.env['ir.values'].get_default('job.config.settings','journal')
        if not self.journal_entry :
            self.journal_entry = self.env['account.move'].create({
                'journal_id': journal,
                'partner_id': self.container.partner.id,
                'date': fields.Date.context_today(self)
                })
        debit_line = self.env['account.move.line'].create({
            'move_id': self.journal_entry.id,
            'account_id': deferred_receivable_account,
            'partner_id': self.container.partner.id,
            'name': 'Finish '+self.job_name,
            'debit': self.cost
        })
        credit_line = self.env['account.move.line'].create({
            'move_id': self.journal_entry.id,
            'account_id': self.product.revenue_account,
            'partner_id': self.container.partner.id,
            'name': 'Finish '+self.job_name,
            'credit': self.cost
            })
        self.journal_entry.line_ids+=debit_line
        self.journal_entry.line_ids+=credit_line
    '''else:
        self.journal_entry.unlink()'''


"""
 class JobLine(models.Model):
     _inherit = 'product.job_line'
     value = fields.Float()
     journal_entry = fields.Many2one('account.move')
     cost = fields.Float()

     @http.route('/api/create_account_move_line_data',auth='public')
     def update_journal(self):
            revenue_account = self.product.revenue_account
             deferred_receivable_account = self.env['ir.values'].get_default('job.config.settings','deferred_receivable_account')
             journal = self.env['ir.values'].get_default('job.config.settings','journal')
            if not self.journal_entry :
                self.journal_entry = self.env['account.move'].create({
                    'journal_id': journal,
                    'partner_id': self.container.partner.id,
                    'date': fields.Date.context_today(self)
                    })
             # if self.container.order.invoice_count > 0:
             #  _logger.info('Type 1  : ')
             # else:
            #   _logger.info('Type 2  : ')
            debit_line = self.env['account.move.line'].create({
                 'move_id': self.journal_entry.id,
                 'account_id': deferred_receivable_account,
                'partner_id': self.container.partner.id,
                'name': 'Finish '+self.job_name,
                'debit': self.cost
            })
            credit_line = self.env['account.move.line'].create({
                'move_id': self.journal_entry.id,
                'account_id': self.product.revenue_account,
                'partner_id': self.container.partner.id,
                'name': 'Finish '+self.job_name,
                'credit': self.cost
             })
             _logger.info(str(debit_line)+' '+str(credit_line))
            self.journal_entry.line_ids+=debit_line
            self.journal_entry.line_ids+=credit_line
        else:
            self.journal_entry.unlink()
            _logger.info('No finish Yet '+str(self.journal_entry))

"""