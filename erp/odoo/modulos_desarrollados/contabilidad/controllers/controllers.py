from odoo import http
from odoo.http import request, Response
import io
import xlsxwriter

class ContabilidadController(http.Controller):

    @http.route('/descargar_excel_contabilidad', auth='public', type='http', methods=['GET'])
    def descargar_excel(self, **kw):
        contabilidad_nombre = kw.get('name')  # Obtener el nombre de la contabilidad desde la URL

        if not contabilidad_nombre:
            return Response("Debe proporcionar un nombre de contabilidad", status=400)

        # Buscar la contabilidad por nombre
        contabilidad = request.env['contabilidad.contabilidad'].sudo().search([('name', '=', contabilidad_nombre)], limit=1)

        if not contabilidad:
            return Response("No se encontró la contabilidad con ese nombre", status=404)

        # Obtener los gastos asociados a la contabilidad
        gastos = contabilidad.mis_gastos

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet(f'COMPRAS {contabilidad.fecha.month} {contabilidad.fecha.year}')
        formato_encabezado = workbook.add_format({
            'bold': True,
            'font_name': 'Calibri',
            'font_size': 12,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_color': '#063970'
        })

        formato_celdas = workbook.add_format({
            'bold': True,
            'font_name': 'Calibri',
            'font_size': 11,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_color': '#063970'
        })

        
        formato_quetzales = workbook.add_format({
            'bold': True,
            'num_format': 'Q #,##0.00', 
            'font_name': 'Calibri',
            'font_size': 11,
            'border': 1,  
            'align': 'right', 
            'font_color': '#063970'
        })

        formato_quetzales_subrayado = workbook.add_format({
            'bold': True,
            'num_format': 'Q #,##0.00',
            'font_name': 'Calibri',
            'font_size': 11,
            'border': 1,
            'align': 'right',
            'underline': 1
        })

        # Establecemos un ancho
        worksheet.set_column(0, 0, 15.5)
        worksheet.set_column(1, 1, 52.3)
        worksheet.set_column(2, 2, 11.3)
        worksheet.set_column(3, 3, 18)
        worksheet.set_column(4, 4, 25)

        # Encabezados
        headers = ['FECHA', 'PROVEEDOR','VALOR Q',  'No. DE FACTURA', 'RETENCIONES']
        for col_num, header in enumerate(headers):
            worksheet.write(0, col_num, header, formato_encabezado)
            

        ultima_fila = len(gastos) + 1

        for row_num, gasto in enumerate(gastos, start=1):
            worksheet.write(row_num, 0, str(gasto.get('expense_date')), formato_celdas)
            worksheet.write(row_num, 1, gasto.get('supplier'), formato_celdas)
            worksheet.write(row_num, 3, gasto.get('number'), formato_celdas)
            worksheet.write(row_num, 2, gasto.get('value'), formato_quetzales)
            worksheet.write(row_num, 4, gasto.get('constancia'), formato_celdas)

        worksheet.write_formula(ultima_fila, 2, f"=SUM(C2:C{ultima_fila})", formato_quetzales_subrayado)

        workbook.close()
        output.seek(0)

        return Response(
            output.getvalue(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers=[("Content-Disposition", f"attachment; filename={contabilidad_nombre}.xlsx")]
        )
