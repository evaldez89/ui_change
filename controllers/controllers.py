# -*- coding: utf-8 -*-
# from odoo import http


# class UiChange(http.Controller):
#     @http.route('/ui_change/ui_change', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ui_change/ui_change/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ui_change.listing', {
#             'root': '/ui_change/ui_change',
#             'objects': http.request.env['ui_change.ui_change'].search([]),
#         })

#     @http.route('/ui_change/ui_change/objects/<model("ui_change.ui_change"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ui_change.object', {
#             'object': obj
#         })

