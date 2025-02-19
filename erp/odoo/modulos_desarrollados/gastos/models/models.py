# -*- coding: utf-8 -*-



# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests

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

    def print_custom_report(self):
        return self.env.ref("template_factura.bill_template_action").report_action(self)


    def download_excel(self):
        url = "http://localhost:8069/descargar_excel"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return {
                    'type': 'ir.actions.act_url',
                    'url': url,
                    'target': 'self',
                }
            else:
                return {'warning': {'title': 'Error', 'message': 'No se pudo descargar el archivo'}}
        except requests.exceptions.RequestException as e:
            return {'warning': {'title': 'Error', 'message': f'Error de conexión: {str(e)}'}}
        
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

