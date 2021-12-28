# -*- coding: utf-8 -*-
# from odoo import http


# class ApprovalExt(http.Controller):
#     @http.route('/approval_ext/approval_ext/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approval_ext/approval_ext/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('approval_ext.listing', {
#             'root': '/approval_ext/approval_ext',
#             'objects': http.request.env['approval_ext.approval_ext'].search([]),
#         })

#     @http.route('/approval_ext/approval_ext/objects/<model("approval_ext.approval_ext"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approval_ext.object', {
#             'object': obj
#         })
