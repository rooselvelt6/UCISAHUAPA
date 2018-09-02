# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ExamenFisico(models.Model):
	_name = "admision.examenfisico"

	# RESUMEN DEL EXAMEN
	resumen = fields.Html(
	    string='Resumen',
	)

	# PIEL
	piel = fields.Html(
	    string='Piel',
	)

	# CARDIOPULMONAR
	cardiopulmonar = fields.Html(
	    string='Cardiopulmonar',
	)

	# ABDOMEN
	abdomen = fields.Html(
	    string='Abdomen',
	)

	# NEUROLOGICO
	neurologico = fields.Html(
	    string='Neurológico',
	)

	# UROGENITAL
	urogenital = fields.Html(
	    string='Urogenital',
	)

	# EXTREMIDADES
	extremidades = fields.Html(
	    string='Extremidades',
	)

	# CABEZA
	cabeza = fields.Html(
	    string='Cabeza',
	)

	# GENITALES
	genitales = fields.Html(
	    string='Genitales',
	)

	# OIDOS
	oidos = fields.Html(
	    string='Oidos',
	)

	# GASES ARTERIALES
	gases_arteriales = fields.Html(
	    string='Gases arteriales',
	)

	# BOCA
	boca = fields.Html(
	    string='Boca',
	)

	# OJOS
	ojos = fields.Html(
	    string='Ojos',
	)