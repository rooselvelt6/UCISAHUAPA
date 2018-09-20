# -*- coding: utf-8 -*-
{
    'name': "APACHE II",

    'summary': """Acute Physiology and Chronic Health Evaluation II (APACHE II)""",

    'description': """
        Sistema APACHE II:
            El score: Acute Physiology and Chronic Health Evaluation II 
            (APACHE II), es un sistema de valoración pronostica de mortalidad, 
            que consiste en detectar los trastornos fisiológicos agudos 
            que atentan contra la vida del paciente y se fundamenta en la 
            determinación de las alteraciones de variables fisiológicas y de 
            parámetros de laboratorio, cuya puntuación es un factor 
            predictivo de mortalidad, siendo este índice válido para un amplio 
            rango de diagnósticos, fácil de usar y que puede sustentarse en datos 
            disponibles en la mayor parte de las UCI (Knaus et al., 1985).
            
            El índice APACHE II es calculado en el momento de ingreso o al final 
            del día de internación del paciente, por lo tanto la misma, brinda un 
            perfil momentáneo del estado del internado, no pudiendo 
            aportar información dinámica.
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
        'views/apache2.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'application': True,
}    