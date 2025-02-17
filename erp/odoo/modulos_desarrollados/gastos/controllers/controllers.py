# # -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
from odoo.http import request
# import pandas as pd
import io
import json
import xlsxwriter

class GastoController(http.Controller):

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
