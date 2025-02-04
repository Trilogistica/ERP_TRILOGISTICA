from odoo import http
from odoo.http import request
from odoo.http import Response
import json

class GastoController(http.Controller):
    @http.route('/gastos/suma_total', auth='public', type='http')
    def suma_total_gastos(self, **kw):
        # Obtener todos los gastos con estado 'pagado'
        total = request.env['gastos.gasto'].search([('status', '=', 'pagado')]).mapped('value')
        total_isr =  request.env['gastos.gasto'].search([('status', '=', 'pagado')]).mapped('isr')
        # Sumar todos los valores de los gastos
        suma_total = sum(total)
        suma_isr = sum(total_isr)
        
        # Crear la respuesta JSON
        return Response(
            json.dumps({'suma_total': suma_total, 'suma_isr': suma_isr}),
            content_type='application/json',
        )

