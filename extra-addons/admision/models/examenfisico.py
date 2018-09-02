# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ExamenFisico(models.Model):
	_name = "admision.examenfisico"

	# RESUMEN DEL EXAMEN
	resumen = fields.Html(
	    string='Resumen',
	    translate=True
	)

	# PIEL
	piel = fields.Html(
	    string='Piel',
	    translate=True
	)

	# CARDIOPULMONAR
	cardiopulmonar = fields.Html(
	    string='Cardiopulmonar',
	    translate=True
	)

	# ABDOMEN
	abdomen = fields.Html(
	    string='Abdomen',
	    translate=True
	)

	# NEUROLOGICO
	neurologico = fields.Html(
	    string='Neurológico',
	    translate=True
	)

	# UROGENITAL
	urogenital = fields.Html(
	    string='Urogenital',
	    translate=True
	)

	# EXTREMIDADES
	extremidades = fields.Html(
	    string='Extremidades',
	    translate=True
	)

	# CABEZA
	cabeza = fields.Html(
	    string='Cabeza',
	    translate=True
	)

	# GENITALES
	genitales = fields.Html(
	    string='Genitales',
	    translate=True
	)

	# OIDOS
	oidos = fields.Html(
	    string='Oidos',
	    translate=True
	)

	# GASES ARTERIALES
	gases_arteriales = fields.Html(
	    string='Gases arteriales',
	    translate=True
	)

	# BOCA
	boca = fields.Html(
	    string='Boca',
	    translate=True
	)

	# OJOS
	ojos = fields.Html(
	    string='Ojos',
	    translate=True
	)