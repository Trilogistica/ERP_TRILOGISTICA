from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'facturacion.invoice'
    _description = 'Factura'
    
    name = fields.Char(string='Nombre', required=True)
    invoice_date = fields.Date(string='Fecha de Factura', required=True)
    total_amount = fields.Monetary(string='Monto Total', required=True, currency_field='currency_id')
    currency_id = fields.Many2one(
        'res.currency',
        string='Moneda',
        required=True,
        default=lambda self: self.env.ref('base.GTQ'),  # Quetzal por defecto
        domain=[('name', 'in', ['GTQ', 'USD'])] # Monedas disponibles, si se desea agregar una nueva ponerla en la lista 
    )
    status = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('pagado', 'Pagado'),
            ('cancelado', 'Cancelado'),
        ],
        string='Estado',
        required=True,
        default='pendiente'
    )
    description = fields.Text(string='Descripción')

    @api.model
    def _get_allowed_currencies(self):
        return self.env['res.currency'].search([('name', 'in', ['GTQ', 'USD'])])
