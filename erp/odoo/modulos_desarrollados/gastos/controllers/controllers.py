# -*- coding: utf-8 -*-
# from odoo import http


# class Gastos(http.Controller):
#     @http.route('/gastos/gastos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gastos/gastos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gastos.listing', {
#             'root': '/gastos/gastos',
#             'objects': http.request.env['gastos.gastos'].search([]),
#         })

#     @http.route('/gastos/gastos/objects/<model("gastos.gastos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gastos.object', {
#             'object': obj
#         })

