# -*- coding: utf-8 -*-
{
    'name': "owl_component",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'owl_component/static/**/*'
        ],
        # 'owl_component.assets': [
        #     # bootstrap
        #     ('include', 'web._assets_helpers'),
        #     'web/static/src/scss/pre_variables.scss',
        #     'web/static/lib/bootstrap/scss/_variables.scss',
        #     ('include', 'web._assets_bootstrap'),
        #
        #     'web/static/src/libs/fontawesome/css/font-awesome.css',  # required for fa icons
        #     'web/static/src/legacy/js/promise_extension.js',  # required by boot.js
        #     'web/static/src/boot.js',  # odoo module system
        #     'web/static/src/env.js',  # required for services
        #     'web/static/src/session.js',  # expose __session_info__ containing server information
        #     'web/static/lib/owl/owl.js',  # owl library
        #     'web/static/lib/owl/odoo_module.js',  # to be able to import "@odoo/owl"
        #     'web/static/src/core/utils/functions.js',
        #     'web/static/src/core/browser/browser.js',
        #     'web/static/src/core/registry.js',
        #     'web/static/src/core/assets.js',
        #     'owl_component/static/**/*'
        # ]
    }
}
