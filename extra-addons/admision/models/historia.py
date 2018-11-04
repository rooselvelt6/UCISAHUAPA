# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Historia(models.Model):
	_name = "admision.historia"
	_description = "Historias"

	# CAMPO PARA MOSTRAR EN RELACIÓN
	_rec_name = "numero"
	
	# RESUMEN
	numero = fields.Char(string='Número de historia',
						   index=True, 
						   help='Número de la Historia Clínica')
	_sql_constraints = [
	    ('numero_uniq', 'unique (numero)', ('Este número de historia ya se encuentra registrado !!!')),
	]
	@api.constrains('numero')
	def check_numero(self):
		if not self.numero:
			raise exceptions.ValidationError(
				'El número de historia debe ser completado !!!'
			)
		if((len(self.numero) < 6)):
			raise exceptions.ValidationError(
				'El número de historia debe poseer un mínimo de 6 digitos !!!'
			)
		if((len(self.numero) > 7)):
			raise exceptions.ValidationError(
				'El número de historia debe poseer un máximo de 7 digitos !!!'
			)
		if(not self.numero.isdigit()):
			raise exceptions.ValidationError(
				"El número de historia no es válida !!!"
			)

		if (self.numero.isspace()):
			raise exceptions.ValidationError(
				"No se puede registrar una historia vacia !!!"
			)
		if (self.numero.isalpha()):
			raise exceptions.ValidationError(
				"Por favor ingresar un número de historia correcto !!!"
			)




