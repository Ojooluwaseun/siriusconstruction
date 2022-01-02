# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class approval_ext(models.Model):
    _inherit = 'approval.request'
   
    unique_code = fields.Char(string='Request Number')
    next = fields.Char(string = 'Next Number', copy=False, default='New')
    department_id = fields.Many2one('hr.department', string='Department')
    location_id = fields.Many2one('stock.warehouse', string='Site/Location')
    
    @api.model
    def create(self, vals):
        if vals.get('next', 'New') = 'New':
            vals['next'] = self.env['ir.sequence'].next_by_code('approval.sequence') or 'New'
        result = super(approval_ext, self).create(vals)
        return result
            
    
    @api.model
    def _compute_unique_code(self, id):
        record = self.search([('id', '=', id)])
        for rec in record:
            if rec.location_id and rec.department_id and rec.partner_id:
                todays_date = date.today()
                rec.unique_code = rec.department_id.department_code + '/' + rec.category_id.sequence_code + '/' + str(rec.partner_id.id) + '/' + rec.location_id.code + '/' + str(todays_date.year) + '/' + str(todays_date.month) + '/' + rec.next
    

class department_ext(models.Model):
    _inherit = 'hr.department'
   
    department_code = fields.Char(string='Code')
