from odoo import models, fields

class CustomInvoice(models.Model):
    _name = 'custom.invoice'
    _description = 'Factura personalizada'

    name = fields.Char(string='Número de Factura', required=True)
    date_invoice = fields.Date(string='Fecha de Factura', required=True)
    amount_total = fields.Float(string='Total', required=True)
    partner_id = fields.Many2one('res.partner', string='Cliente', required=True)

