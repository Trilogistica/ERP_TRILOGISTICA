from odoo import models, fields

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

class EmpleadoAusenciasVista(models.Model):
    _inherit = 'empleados.ausencias'
    
    def get_ausencias(self):
        for record in self:
            record.ausencias_count = len(record.ausencias_ids)
    
    ausencias_count = fields.Integer(string='Cantidad de Ausencias', compute='get_ausencias')

