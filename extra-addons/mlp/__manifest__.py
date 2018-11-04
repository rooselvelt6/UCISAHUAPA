# -*- coding: utf-8 -*-
{
    'name': "mlp",

    'summary': """Multilayer Perceptron""",

    'description': """
        RNA tipo perceptron multicapa con interfaz gráfica definida para 
        entrenamiento, prueba, validación y manejo de hiperparámetros
        del sistema general.
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
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}