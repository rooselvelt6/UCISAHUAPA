# -*- coding: utf-8 -*-
{
    'name': "Apache",

    'summary': """

        Sistema de gravedad de la UCI del SAHUAPA

        """,

    'description': """
        Sistema de gravedad Apache II, es un índice que mide la gravedad de un paciente y estima la mortalidad del mismo
        cada 24H es una UCI basado en parámetros fisiológicos del paciente
            - Cálculo de la gravedad de un paciente en UCI
            - Estimación de la mortalidad de un paciente en UCI
            - APS de un paciente en UCI
    """,

    'author': "Rooselvelt Angulo",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sistema de gravedad de la UCI',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}