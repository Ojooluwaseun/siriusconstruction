# -*- coding: utf-8 -*-

from odoo import models, fields, api


class approval_ext(models.Model):
    _inherit = 'approval.request'
   
    unique_id = fields.Char(string='Request Number')
    department_id = fields.Many2one('hr.department', string='Department')
    location_id = fields.Many2one('stock.warehouse', string='Site/Location')
