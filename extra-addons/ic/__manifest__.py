# -*- coding: utf-8 -*-
{
    'name': "ic",

    'summary': """
        Inteligencia Computacional (IC).
    """,

    'description': """
        Inteligencia Computacional (IC): es un módulo encargado de aplicar diferentes técnicas inteligentes
        de aprendizaje en máquinas y sus diferentes paradigmas de aprendizaje supervisado y no supervisado
        además de lógica difusa, algoritmos genéticos y redes neuronales artificiales.
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
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/paciente.xml',
        'views/familiar.xml',
        'views/examen_fisico.xml',
        'views/orden_medica.xml',
        'views/apache2.xml', # Indice APACHE II
        'reports/reporte_paciente.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
}