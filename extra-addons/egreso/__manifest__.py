# -*- coding: utf-8 -*-
{
    'name': "Egreso UCI",

    'summary': """
        Sistema de control de egreso de pacientes admitidos en la UCI del SAHUAPA.""",

    'description': """
        Sistema de control de egresos de pacientes admitidos en la UCI.
            - Historia de admisión a UCI.
            - Examenes.
            - Diagnosticos.
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
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}


