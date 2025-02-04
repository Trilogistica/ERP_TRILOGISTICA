# -*- coding: utf-8 -*-
# from odoo import http


# class HojaCalculo(http.Controller):
#     @http.route('/hoja_calculo/hoja_calculo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hoja_calculo/hoja_calculo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hoja_calculo.listing', {
#             'root': '/hoja_calculo/hoja_calculo',
#             'objects': http.request.env['hoja_calculo.hoja_calculo'].search([]),
#         })

#     @http.route('/hoja_calculo/hoja_calculo/objects/<model("hoja_calculo.hoja_calculo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hoja_calculo.object', {
#             'object': obj
#         })

