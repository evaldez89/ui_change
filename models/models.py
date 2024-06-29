# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ui_change(models.Model):
#     _name = 'ui_change.ui_change'
#     _description = 'ui_change.ui_change'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

