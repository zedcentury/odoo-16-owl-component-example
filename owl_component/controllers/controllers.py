# -*- coding: utf-8 -*-
from odoo import http


class OwlComponent(http.Controller):
    @http.route('/owl-component/example-page', type='http', auth='public', website=True, sitemap=True)
    def example_page(self, **kw):
        return http.request.render('owl_component.example_page')
