from odoo import models, fields, api, _


class Contact_Info(models.Model):
    _inherit = 'res.users'



    pin = fields.Integer(string="PIN")
    # pin3 = fields.Integer(string="PIN")

    @api.model
    def create(self, values):
        # Override the original create function for the res.partner model

        print('values', values['email'])
        print('login', values['login'])

        record = super(Contact_Info, self).create(values)
        print('values', record['email'])
        print('id', record['id'])
        id=record['id']
        print('login', record['login'])

        val = self.search([('id','=',id)])
        print('user id =: ', val.id)
        print('user name =: ',val.name)
        print('user login =: ', val.login)
        print('users',val)
        partners = self.env['res.partner'].search([('name','=',val.name)])
        for ptnr in partners[0]:

            print('partners: ',partners)
            print('partners id: ', ptnr.id)
            print('commercial_partner_id id: ', ptnr.commercial_partner_id)
            print('partners id: ', ptnr.parent_id)

        self.env['res.partner'].browse(ptnr.id).write({
            'id': id,
            'name': val.name,
            'phone': val.login
        })
        return record
