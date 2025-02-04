from odoo import http
from odoo.http import request

class ContabilidadController(http.Controller):

    @http.route('/contabilidad/panel', auth='public', website=True)
    def show_dashboard(self, **kw):
        # Aquí puedes pasarle datos a la página web, como la suma total o cualquier otra información
        suma_total = 1000  # Ejemplo de datos que puedes obtener de la base de datos
        suma_isr = 200
        return request.render('contabilidad.dashboard_template', {
            'suma_total': suma_total,
            'suma_isr': suma_isr,
        })
