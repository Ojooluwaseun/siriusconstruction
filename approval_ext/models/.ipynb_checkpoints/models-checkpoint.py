# -*- coding: utf-8 -*-

from odoo import models, fields, api


class approval_ext(models.Model):
    _inherit = 'approval.request'
   
    unique_code = fields.Char(string='Request Number')
    department_id = fields.Many2one('hr.department', string='Department')
    location_id = fields.Many2one('stock.warehouse', string='Site/Location')
    
    @api.model
    def _compute_unique_code(self, id):
        record = self.search([('id', '=', id)])
        for rec in record:
            if rec.location_id and rec.department_id and rec.partner_id:
                rec.unique_code = rec.department_id.department_code + '/' + rec.category_id.sequence_code + '/' = rec.partner_id + '/' + rec.location_id.code
    

class department_ext(models.Model):
    _inherit = 'hr.department'
   
    department_code = fields.Char(string='Code')
