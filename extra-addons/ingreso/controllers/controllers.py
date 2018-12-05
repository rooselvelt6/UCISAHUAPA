# -*- coding: utf-8 -*-
from odoo import http

# class Ingreso(http.Controller):
#     @http.route('/ingreso/ingreso/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ingreso/ingreso/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ingreso.listing', {
#             'root': '/ingreso/ingreso',
#             'objects': http.request.env['ingreso.ingreso'].search([]),
#         })

#     @http.route('/ingreso/ingreso/objects/<model("ingreso.ingreso"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ingreso.object', {
#             'object': obj
#         })