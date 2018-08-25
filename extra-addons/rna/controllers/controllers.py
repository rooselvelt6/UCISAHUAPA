# -*- coding: utf-8 -*-
from odoo import http

# class Rna(http.Controller):
#     @http.route('/rna/rna/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rna/rna/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rna.listing', {
#             'root': '/rna/rna',
#             'objects': http.request.env['rna.rna'].search([]),
#         })

#     @http.route('/rna/rna/objects/<model("rna.rna"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rna.object', {
#             'object': obj
#         })