# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ExamenFisico(models.Model):
	_name = "paciente.examen_fisico"
	_description = "Examen físico del paciente"
	_rec_name = "create_date"

	# RESUMEN DEL EXAMEN
	color = fields.Integer('Color')
	
	kanban_state = fields.Selection([('normal', 'Iniciado'),('bloqueado','En proceso'),('done','Completado')])

	resumen = fields.Text(
	    string='Resumen',
	    translate=True,
	    help='Resumen del examen físico del paciente',
	    required=True
	)
	
	# PIEL
	piel = fields.Text(
	    string='Piel',
	    translate=True,
	    help='Piel',
	    required=True
	)

	# CARDIOPULMONAR
	cardiopulmonar = fields.Text(
	    string='Cardiopulmonar',
	    translate=True,
	    help='Cardiopulmonar',
	    required=True,
	)

	# ABDOMEN
	abdomen = fields.Text(
	    string='Abdomen',
	    translate=True,
	    help='Abdomen',
	    required=True,
	)

	# NEUROLOGICO
	neurologico = fields.Text(
	    string='Neurológico',
	    translate=True,
	    help='Neurológico'
	)

	# UROGENITAL
	urogenital = fields.Text(
	    string='Urogenital',
	    translate=True,
	    help='Urogenital'
	)

	# EXTREMIDADES
	extremidades = fields.Text(
	    string='Extremidades',
	    translate=True,
	    help='Extremidades'
	)

	# CABEZA
	cabeza = fields.Text(
	    string='Cabeza',
	    translate=True,
	    help='Cabeza'
	)

	# GENITALES
	genitales = fields.Text(
	    string='Genitales',
	    translate=True,
	    help='Genitales'
	)

	# OIDOS
	oidos = fields.Text(
	    string='Oidos',
	    translate=True,
	    help='Oidos'
	)

	# GASES ARTERIALES
	gases_arteriales = fields.Text(
	    string='Gases arteriales',
	    translate=True,
	    help='Gases arteriales'
	)

	# BOCA
	boca = fields.Text(
	    string='Boca',
	    translate=True,
	    help='Boca'
	)

	# OJOS
	ojos = fields.Text(
	    string='Ojos',
	    translate=True,
	    help='Ojos'
	)