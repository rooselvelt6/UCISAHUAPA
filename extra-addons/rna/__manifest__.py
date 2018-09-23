# -*- coding: utf-8 -*-
{
    'name': "Agente basado en RNA",

    'summary': """RNA tipo MLP con BP""",

    'description': """
        Red neuronal artificial multicapa con retroprogación de errores para la estimación de la estadía de un paciente en la UCI del SAHUAPA en base a 
        variables de admisión del mismo.

        El sistema neuronal hace uso de las variables de la evaluación de la admisión para realizar el cálculo de la variable de estadía.

            - Tiempo de estadía hospitalaria: diferencia entre las fechas de ingreso al hospital y de ingreso a UCI.
            - Antecedentes del paciente.
            - Ventilación mecánica.
            - Migración del paciente.
            - Color de piel del paciente.
            - Presencia de procesos invasivos.
            - Edad.
            - Sexo.
            - Tipo de admisión. 
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
        #'security/ir.model.access.csv',
        'views/rna.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}