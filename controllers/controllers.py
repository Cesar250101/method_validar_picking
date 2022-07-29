# -*- coding: utf-8 -*-
from odoo import http

# class MethodValidarPicking(http.Controller):
#     @http.route('/method_validar_picking/method_validar_picking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_validar_picking/method_validar_picking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_validar_picking.listing', {
#             'root': '/method_validar_picking/method_validar_picking',
#             'objects': http.request.env['method_validar_picking.method_validar_picking'].search([]),
#         })

#     @http.route('/method_validar_picking/method_validar_picking/objects/<model("method_validar_picking.method_validar_picking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_validar_picking.object', {
#             'object': obj
#         })