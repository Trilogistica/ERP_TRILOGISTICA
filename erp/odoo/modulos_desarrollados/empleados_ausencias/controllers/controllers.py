# -*- coding: utf-8 -*-
# from odoo import http


# class EmpleadosAusencias(http.Controller):
#     @http.route('/empleados_ausencias/empleados_ausencias', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/empleados_ausencias/empleados_ausencias/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('empleados_ausencias.listing', {
#             'root': '/empleados_ausencias/empleados_ausencias',
#             'objects': http.request.env['empleados_ausencias.empleados_ausencias'].search([]),
#         })

#     @http.route('/empleados_ausencias/empleados_ausencias/objects/<model("empleados_ausencias.empleados_ausencias"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('empleados_ausencias.object', {
#             'object': obj
#         })

