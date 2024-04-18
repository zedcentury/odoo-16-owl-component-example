# -*- coding: utf-8 -*-
from odoo import http


class OwlComponent(http.Controller):
    @http.route('/owl_component/first', type='http', auth='public')
    def first(self, **kw):
        return http.request.render('owl_component.first')

    @http.route('/owl_component/second', type='http', auth='public', website=True, sitemap=True)
    def second(self, **kw):
        return http.request.render('owl_component.second')

    @http.route('/owl_component/third', type='http', auth='public', website=True, sitemap=True)
    def third(self, **kw):
        return http.request.render('owl_component.third')
