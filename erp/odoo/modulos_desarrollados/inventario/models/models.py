from odoo import models, fields, api

class Inventario(models.Model):
    _name = 'inventario.inventario'
    _description = 'Gestión de Inventario de Servicios'
    
    name = fields.Char(string='Número', required=True)
    proveedor_id = fields.Many2one('res.partner', string='Proveedor', required=True)
    servicio_ids = fields.One2many('inventario.servicio', 'inventario_id', string='Servicios')
    
    @api.depends('servicio_ids.precio')
    def _compute_total(self):
        for record in self:
            record.total = sum(servicio.precio for servicio in record.servicio_ids)
    
    total = fields.Float(string='Total', compute='_compute_total', store=True)

class Servicio(models.Model):
    _name = 'inventario.servicio'
    _description = 'Servicios en Inventario'
    
    name = fields.Char(string='Nombre del Servicio/Producto', required=True)
    precio = fields.Float(string='Precio', required=True)
    fecha_compra = fields.Date(string='Fecha de Compra', required=True)
    inventario_id = fields.Many2one('inventario.inventario', string='Inventario')
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('asignado', 'Asignado'),
        ('mantenimiento', 'En Mantenimiento'),
        ('baja', 'De Baja')
    ], string='Estado', default='disponible', required=True)
    descripcion = fields.Text(string='Descripción')
    codigo = fields.Char(string='Código')
