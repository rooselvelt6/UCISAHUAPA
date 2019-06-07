# -*- coding: utf-8 -*-
{
    'name': "RNA",

    'summary': """
        Red neuronal artificial.
        """,

    'description': """
        Red Neuronal Artificial (RNA) tipo perceptron multicapa (MLP) con retropropagación de errores
        basado en TensorFlow y Keras.IO. El sistema se encarga de calcular el tiempo de estadía de un 
        paciente en la UCI del HUAPA basada en los siguientes parámetros:
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
    'depends': ['base','ic'],

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