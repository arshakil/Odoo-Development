from odoo import api, fields, models, tools, _

class PaymentTransactionExtend(models.Model):
    _inherit = "payment.transaction"

    payment_status = fields.Char(name="Payment status")
    transaction_id = fields.Char(name="Transaction ID")
    bank_transaction_id = fields.Char("Bank transaction id")
    card_type = fields.Char("Card type")
    payment_type = fields.Char("Payment type")
    payment_msg = fields.Text('Message')
