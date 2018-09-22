# -*- coding: utf-8 -*-
from odoo import http

# class Egreso(http.Controller):
#     @http.route('/egreso/egreso/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/egreso/egreso/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('egreso.listing', {
#             'root': '/egreso/egreso',
#             'objects': http.request.env['egreso.egreso'].search([]),
#         })

#     @http.route('/egreso/egreso/objects/<model("egreso.egreso"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('egreso.object', {
#             'object': obj
#         })