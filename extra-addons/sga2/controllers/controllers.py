# -*- coding: utf-8 -*-
from odoo import http

# class Sga2(http.Controller):
#     @http.route('/sga2/sga2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sga2/sga2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sga2.listing', {
#             'root': '/sga2/sga2',
#             'objects': http.request.env['sga2.sga2'].search([]),
#         })

#     @http.route('/sga2/sga2/objects/<model("sga2.sga2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sga2.object', {
#             'object': obj
#         })