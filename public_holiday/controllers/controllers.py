# -*- coding: utf-8 -*-
from odoo import http

# class PublicHolyday(http.Controller):
#     @http.route('/public_holiday/public_holiday/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/public_holiday/public_holiday/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('public_holiday.listing', {
#             'root': '/public_holiday/public_holiday',
#             'objects': http.request.env['public_holiday.public_holiday'].search([]),
#         })

#     @http.route('/public_holiday/public_holiday/objects/<model("public_holiday.public_holiday"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('public_holiday.object', {
#             'object': obj
#         })