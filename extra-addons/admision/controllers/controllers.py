# -*- coding: utf-8 -*-
from odoo import http

# class Admision(http.Controller):
#     @http.route('/admision/admision/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/admision/admision/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('admision.listing', {
#             'root': '/admision/admision',
#             'objects': http.request.env['admision.admision'].search([]),
#         })

#     @http.route('/admision/admision/objects/<model("admision.admision"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('admision.object', {
#             'object': obj
#         })