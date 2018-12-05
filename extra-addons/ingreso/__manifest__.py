# -*- coding: utf-8 -*-
{
    'name': "Ingreso a UCI SAHUAPA",

    'summary': """
        Sistema de control de ingreso de pacientes a la UCI del SAHUAPA """,

    'description': """
        Sistema de control de ingreso de pacientes a la UCI del SAHUAPA.
            - Datos personales.
            - Examenes.
            - Diagnosticos.
            - Pruebas de admisión.
            - Entre otras.
    """,

    'author': "Rooselvelt Angulo",
    'website': "https://github.com/rooselvelt6/UCISAHUAPA/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'UCI',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ingreso.xml',
        'views/templates.xml',
        'views/orden.xml',
        'views/familiar.xml',
    
        'views/examen_fisico.xml',
        'reports/reporte_ingreso.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}