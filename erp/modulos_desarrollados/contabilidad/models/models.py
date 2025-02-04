from odoo import models, fields, api
import requests

class Contabilidad(models.Model):
    _name = 'contabilidad.contabilidad'
    _description = 'contabilidad.contabilidad'

    name = fields.Char()
    suma_total = fields.Float(string="Suma Total de Gastos")
    suma_total_irs = fields.Float(string="Suma Total de IRS")

    @api.model
    def obtener_suma_total(self):
        url = 'http://localhost:8069/gastos/suma_total'

        try:
            response = requests.get(url)
            response.raise_for_status()

            if response.status_code == 200:
                data = response.json()
                # Actualizar los campos con la respuesta
                print(data)
                self.suma_total = data.get('suma_total', 0)
                self.suma_total_irs = data.get('suma_isr', 0)

        except requests.exceptions.RequestException as e:
            print(f"Error al hacer la solicitud: {e}")
            self.suma_total = 0
            self.suma_total_irs = 0

    @api.model
    def cron_actualizar_suma_total(self):
        # Esta función puede ser llamada por un cron job programado
        registros = self.search([])
        for registro in registros:
            registro.obtener_suma_total()
