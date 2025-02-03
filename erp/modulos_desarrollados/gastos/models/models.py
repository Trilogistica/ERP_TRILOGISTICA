# -*- coding: utf-8 -*-

from odoo import models, fields, api


# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Gasto(models.Model):
    _name = 'gastos.gasto'
    # _description = 'gastos.gastos'
    expense_date = fields.Date(string="FECHA")
    supplier = fields.Char(string="PROVEEDOR")
    number = fields.Char(string="NUMERO")
    value = fields.Float(string="VALOR Q")
    no_retencion_isr = fields.Char(string="NUMERO RETENCION ISR")
    isr = fields.Float(string="VALOR ISR")
    constancia = fields.Char(string="CONSTANCIA")
    
    status = fields.Selection(
        selection=[
            ('pagado', 'Pagado'),
            ('en_proceso', 'En Proceso'),
            ('no_pagado', 'No Pagado'),
        ],
        string='Estado de Pago',
        default='no_pagado',  # Valor predeterminado
    )

    @api.model
    def create_gasto(self, expense_date, supplier, number, value, no_retencion_isr, isr, constancia, status='no_pagado'):
        # Crear un nuevo gasto
        record = self.create({
            'expense_date': expense_date,
            'supplier': supplier,
            'number': number,
            'value': value,
            'no_retencion_isr': no_retencion_isr,
            'isr': isr,
            'constancia': constancia,
            'status': status,
        })
        
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

