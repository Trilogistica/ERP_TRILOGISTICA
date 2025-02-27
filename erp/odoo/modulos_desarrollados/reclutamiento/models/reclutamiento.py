from odoo import models, fields, api

class ReclutamientoCandidato(models.Model):
    _name = 'reclutamiento.candidato'
    _description = 'Candidatos en proceso de reclutamiento'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico')
    telefono = fields.Char(string='Teléfono')
    fecha_aplicacion = fields.Date(string='Fecha de Aplicación', default=fields.Date.today)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('entrevista', 'En Entrevista'),
        ('rechazado', 'Rechazado'),
        ('contratado', 'Contratado')
    ], string='Estado', default='pendiente')
