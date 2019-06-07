# -*- coding: utf-8 -*-
from odoo import http

# class Ic(http.Controller):
#     @http.route('/ic/ic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ic/ic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ic.listing', {
#             'root': '/ic/ic',
#             'objects': http.request.env['ic.ic'].search([]),
#         })

#     @http.route('/ic/ic/objects/<model("ic.ic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ic.object', {
#             'object': obj
#         })