# -*- coding: utf-8 -*-
# from odoo import http


# class Documentos(http.Controller):
#     @http.route('/documentos/documentos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/documentos/documentos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('documentos.listing', {
#             'root': '/documentos/documentos',
#             'objects': http.request.env['documentos.documentos'].search([]),
#         })

#     @http.route('/documentos/documentos/objects/<model("documentos.documentos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('documentos.object', {
#             'object': obj
#         })

