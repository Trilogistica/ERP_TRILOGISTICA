# -*- coding: utf-8 -*-
# from odoo import http


# class Evaluacion(http.Controller):
#     @http.route('/evaluacion/evaluacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/evaluacion/evaluacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('evaluacion.listing', {
#             'root': '/evaluacion/evaluacion',
#             'objects': http.request.env['evaluacion.evaluacion'].search([]),
#         })

#     @http.route('/evaluacion/evaluacion/objects/<model("evaluacion.evaluacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('evaluacion.object', {
#             'object': obj
#         })

