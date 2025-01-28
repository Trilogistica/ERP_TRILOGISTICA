from odoo import models, fields

class Invoice(models.Model):
    _name = 'facturacion.invoice'
    _description = 'Invoice'

    name = fields.Char(string='Name', required=True)  # Nombre de la facturación
    invoice_date = fields.Date(string='Invoice Date', required=True)  # Fecha de la factura
    total_amount = fields.Monetary(string='Total Amount', required=True, currency_field='currency_id')  # Monto total
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)  # Moneda
    status = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('pagado', 'Pagado'),
            ('cancelado', 'Cancelado'),
        ],
        string='Status',
        required=True,
        default='pendiente'
    )  # Estado de la factura
    description = fields.Text(string='Description')  # Descripción de la factura

