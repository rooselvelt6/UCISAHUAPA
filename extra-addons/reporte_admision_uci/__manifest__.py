# -*- coding: utf-8 -*-
{
    'name': "reporteAdmisionUCI",

    'summary': """
        Reporte de admisión de los pacientes en la UCI SAHUAPA """,

    'description': """
        Reporte para la admisión del paciente en la UCI SAHUAPA.
            - Diagnóstico.
            - Evaluación de ingreso.
            - Examen físico de ingreso.
            - Datos generales.
            - Estimaciones de estadía.
    """,

    'author': "Rooselvelt Angulo",
    'website': "https://github.com/rooselvelt6/UCISAHUAPA/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'UCI',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','admision'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/reporte_admision.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
}