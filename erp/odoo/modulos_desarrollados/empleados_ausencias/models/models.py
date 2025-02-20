# models.py
from odoo import models, fields, api

class Empleado(models.Model):
    _name = 'empleados.ausencias'
    _description = 'Registro de empleados y sus ausencias'

    nombre_completo = fields.Char(string='Nombre Completo', required=True)
    dpi = fields.Char(string='DPI', required=True)
    estacion_trabajo = fields.Char(string='Estación de Trabajo')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    puesto = fields.Char(string='Puesto')
    estado_civil = fields.Selection([
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo')
    ], string='Estado Civil')
    sexo = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro')
    ], string='Sexo')
    ausencias_ids = fields.One2many('empleados.ausencias.registro', 'empleado_id', string='Ausencias')
    ausencias_count = fields.Integer(
        string='Cantidad de Ausencias',
        compute='_compute_ausencias_count',
        store=True
    )

    @api.depends('ausencias_ids')
    def _compute_ausencias_count(self):
        for record in self:
            record.ausencias_count = len(record.ausencias_ids)

    def action_view_ausencias(self):
        return {
            'name': 'Ausencias',
            'type': 'ir.actions.act_window',
            'res_model': 'empleados.ausencias.registro',
            'view_mode': 'list,form,calendar',
            'domain': [('empleado_id', '=', self.id)],
            'context': {'default_empleado_id': self.id},
        }

class Ausencia(models.Model):
    _name = 'empleados.ausencias.registro'
    _description = 'Registro de Ausencias de Empleados'

    empleado_id = fields.Many2one('empleados.ausencias', string='Empleado', required=True, ondelete='cascade')
    fecha_inicio = fields.Date(string='Fecha de Inicio', required=True)
    fecha_fin = fields.Date(string='Fecha de Fin', required=True)
    tipo_ausencia = fields.Selection([
        ('enfermedad', 'Enfermedad'),
        ('dias_libres', 'Días Libres'),
        ('feriado_tomado', 'Feriado Tomado'),
        ('feriado_no_tomado', 'Feriado No Tomado')
    ], string='Tipo de Ausencia', required=True)
    descripcion = fields.Text(string='Descripción')

