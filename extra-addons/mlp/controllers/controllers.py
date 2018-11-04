# -*- coding: utf-8 -*-
from odoo import http

# class Mlp(http.Controller):
#     @http.route('/mlp/mlp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mlp/mlp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mlp.listing', {
#             'root': '/mlp/mlp',
#             'objects': http.request.env['mlp.mlp'].search([]),
#         })

#     @http.route('/mlp/mlp/objects/<model("mlp.mlp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mlp.object', {
#             'object': obj
#         })