# -*- coding: utf-8 -*-
from odoo import http

# class ReporteEmpleadosUci(http.Controller):
#     @http.route('/reporte_empleados_uci/reporte_empleados_uci/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reporte_empleados_uci/reporte_empleados_uci/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('reporte_empleados_uci.listing', {
#             'root': '/reporte_empleados_uci/reporte_empleados_uci',
#             'objects': http.request.env['reporte_empleados_uci.reporte_empleados_uci'].search([]),
#         })

#     @http.route('/reporte_empleados_uci/reporte_empleados_uci/objects/<model("reporte_empleados_uci.reporte_empleados_uci"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reporte_empleados_uci.object', {
#             'object': obj
#         })