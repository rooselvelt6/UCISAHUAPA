# -*- coding: utf-8 -*-
from odoo import http

# class Apache(http.Controller):
#     @http.route('/apache/apache/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apache/apache/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('apache.listing', {
#             'root': '/apache/apache',
#             'objects': http.request.env['apache.apache'].search([]),
#         })

#     @http.route('/apache/apache/objects/<model("apache.apache"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apache.object', {
#             'object': obj
#         })