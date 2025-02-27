from odoo import models, fields, api
import requests
import json

class Contabilidad(models.Model):
    _name = 'contabilidad.contabilidad'
    _description = 'Modelo de Contabilidad'

    name = fields.Char(string="Nombre", required=True)
    fecha = fields.Date(string="Fecha", default=fields.Date.context_today)
    mis_gastos = fields.Json(string="Gastos", default=[])  # Campo Json para almacenar la lista

    def actualizar_gastos(self):
        """ Llama al endpoint /gastos/filter y actualiza mis_gastos con los resultados """
        url = "http://localhost:8069/gastos/filter"
        params = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "year": str(self.fecha.year),
                "month": str(self.fecha.month)
            }
        }

        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, data=json.dumps(params), headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()

                if 'result' in data and 'gastos' in data['result']:
                    self.mis_gastos = data['result']['gastos']  # Guardar la lista directamente en el campo JSON
                else:
                    raise Exception("No se encontraron gastos en la respuesta")

            else:
                raise Exception(f"Error en la solicitud: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Error de conexión: {str(e)}")

    def download_report(self):
        self.actualizar_gastos()
        url = f"http://localhost:8069/descargar_excel_contabilidad?name={self.name}"
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
