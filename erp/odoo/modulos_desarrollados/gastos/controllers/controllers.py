# # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
from datetime import datetime, timedelta
from odoo.http import request
# import pandas as pd
import io
import json
import xlsxwriter

class GastoController(http.Controller):

    @http.route('/gastos/filter', type='json', auth='public', methods=['POST'])
    def filter_gastos(self, **kwargs):
        import logging
        _logger = logging.getLogger(__name__)

        # Extraer parámetros del request
        year = kwargs.get('year')
        month = kwargs.get('month')

        if not year or not month:
            return {'error': 'Debe proporcionar año y mes'}

        try:
            year = int(year)
            month = int(month)

            # Calcular el último día del mes
            first_day = datetime(year, month, 1)
            next_month = first_day.replace(day=28) + timedelta(days=4)  # Ir al siguiente mes
            last_day = next_month - timedelta(days=next_month.day)  # Retroceder al último día del mes actual

            # Filtrar gastos dentro del rango de fechas
            gastos = request.env['gastos.gasto'].sudo().search([
                ('expense_date', '>=', first_day.strftime('%Y-%m-%d')),
                ('expense_date', '<=', last_day.strftime('%Y-%m-%d')),
                ('status', '=', 'pagado')
            ])

            # Formatear la respuesta
            results = [{
                'expense_date': gasto.expense_date,
                'supplier': gasto.supplier,
                'number': gasto.number,
                'value': gasto.value,
                'status': gasto.status,
                'constancia': gasto.constancia
            } for gasto in gastos]

            return {'gastos': results}

        except ValueError:
            return {'error': 'Año o mes no válidos'}


    @http.route('/descargar_excel', auth='public', type='http', methods=['GET'])
    def descargar_excel(self, **kw):
        output = io.BytesIO()

        # Crear el archivo Excel
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Hoja1')

        # Agregar datos manualmente
        data = [
            ['Columna 1', 'Columna 2'],
            [1, 'A'],
            [2, 'B'],
            [3, 'C']
        ]

        for row_num, row_data in enumerate(data):
            for col_num, cell_data in enumerate(row_data):
                worksheet.write(row_num, col_num, cell_data)

        workbook.close()
        output.seek(0)

        return Response(
            output.getvalue(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers=[("Content-Disposition", "attachment; filename=archivo.xlsx")]
        )
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
