from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PurchaseInherit(models.Model):

    _inherit = 'purchase.order'

    ref_no = fields.Char(string="REF NO")

    partner_ids = fields.Many2one('res.partner', string='Vendor', 
                    domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    state = fields.Selection([
        ('draft', 'RFQ'),
        ('step1', 'STEP 1'),
        ('step2', 'STEP 2'),
        ('sent', 'RFQ Sent'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)




    # @api.model
    # def create(self, vals):
    #     vals['partner_id']=self.ref_no
    #     return super(PurchaseInherit, self).create(vals)


    # @api.onchange("ref_no")
    # def _onchange_purchase_id(self):
    #     for record in self:
    #         self.env['purchase.order'].create({'partner_id':record.ref_no})

    # @api.depends('ref_no')
    # def _compute_purchase_id(self):
    #     for record in self:
    #         self.env['purchase.order'].create({'partner_id':record.ref_no})
            

