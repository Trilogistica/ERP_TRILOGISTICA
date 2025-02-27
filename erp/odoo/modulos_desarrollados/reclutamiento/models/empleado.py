class Empleado(models.Model):
    _inherit = 'hr.employee'

    codigo_empleado = fields.Char(string='Código de Empleado', required=True, copy=False, default=lambda self: self.env["ir.sequence"].next_by_code("hr.empleado"))

