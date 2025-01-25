# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gasto(models.Model):
      _name = 'gastos.gasto'
#     _description = 'gastos.gastos'
      name = fields.Char(string="Descripcion")
      value = fields.Integer(string="Valor")
      expense_date = fields.Date(string="Fecha de Gasto")

      @api.model
      def create_gasto(self):
        for record in self:
            self.create({'name': 'Nuevo Gasto', 'value': 0.0})
            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

