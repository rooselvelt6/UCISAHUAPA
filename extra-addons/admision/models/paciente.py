# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Paciente(models.Model):
	_name = "admision.paciente"

	# NUMERO DE HISTORIA CLINICA
	id_historia = fields.Many2one(
	    'admision.historia',
	    string='Field Label',
	)

	# DATOS PERSONALES
	datos_personales = fields.Many2one(
	    'admision.persona',
	    string='Datos personales',
	)

	# PESO CORPORAL
	peso_corporal = fields.Float(
	    string='Peso corporal',
	)

	# FAMILIAR ENCARGADO
	familiar_encargado = fields.Many2one(
	    'admision.familiar',
	    string='Familiar encargado',
	)

	# DIAGNOSTICO DE INGRESO AL HOSPITAL.
	diagnostico_hospital = fields.Many2one(
	    'admision.diagnostico',
	    string='Diagnóstico de ingreso en HUAPA',
	)

	# EXAMEN DE INGRESO AL HOSPITAL.
	examen_hospital = fields.Many2one(
	    'admision.examenfisico',
	    string='Field Label',
	)