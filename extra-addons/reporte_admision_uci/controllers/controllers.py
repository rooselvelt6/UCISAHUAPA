# -*- coding: utf-8 -*-
from odoo import http

# class ReporteAdmisionUci(http.Controller):
#     @http.route('/reporte_admision_uci/reporte_admision_uci/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reporte_admision_uci/reporte_admision_uci/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reporte_admision_uci.listing', {
#             'root': '/reporte_admision_uci/reporte_admision_uci',
#             'objects': http.request.env['reporte_admision_uci.reporte_admision_uci'].search([]),
#         })

#     @http.route('/reporte_admision_uci/reporte_admision_uci/objects/<model("reporte_admision_uci.reporte_admision_uci"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reporte_admision_uci.object', {
#             'object': obj
#         })