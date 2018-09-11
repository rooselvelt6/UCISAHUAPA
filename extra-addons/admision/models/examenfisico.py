# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ExamenFisico(models.Model):
	_name = "admision.examenfisico"

	# RESUMEN DEL EXAMEN
	resumen = fields.Html(
	    string='Resumen',
	    translate=True,
	    help='Resumen del examen físico del paciente'
	)

	# PIEL
	piel = fields.Html(
	    string='Piel',
	    translate=True,
	    help='Piel'
	)

	# CARDIOPULMONAR
	cardiopulmonar = fields.Html(
	    string='Cardiopulmonar',
	    translate=True,
	    help='Cardiopulmonar'
	)

	# ABDOMEN
	abdomen = fields.Html(
	    string='Abdomen',
	    translate=True,
	    help='Abdomen'
	)

	# NEUROLOGICO
	neurologico = fields.Html(
	    string='Neurológico',
	    translate=True,
	    help='Neurológico'
	)

	# UROGENITAL
	urogenital = fields.Html(
	    string='Urogenital',
	    translate=True,
	    help='Urogenital'
	)

	# EXTREMIDADES
	extremidades = fields.Html(
	    string='Extremidades',
	    translate=True,
	    help='Extremidades'
	)

	# CABEZA
	cabeza = fields.Html(
	    string='Cabeza',
	    translate=True,
	    help='Cabeza'
	)

	# GENITALES
	genitales = fields.Html(
	    string='Genitales',
	    translate=True,
	    help='Genitales'
	)

	# OIDOS
	oidos = fields.Html(
	    string='Oidos',
	    translate=True,
	    help='Oidos'
	)

	# GASES ARTERIALES
	gases_arteriales = fields.Html(
	    string='Gases arteriales',
	    translate=True,
	    help='Gases arteriales'
	)

	# BOCA
	boca = fields.Html(
	    string='Boca',
	    translate=True,
	    help='Boca'
	)

	# OJOS
	ojos = fields.Html(
	    string='Ojos',
	    translate=True,
	    help='Ojos'
	)