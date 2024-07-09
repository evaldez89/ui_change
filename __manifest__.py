# -*- coding: utf-8 -*-
{
    'name': "KTI UI Changes",

    'summary': "Kleiotechnology Interview Test. Cambio nuevo",

    'description': """
This module is for the interview test
    """,

    'author': "Kleiotechnology",
    'website': "https://kleiotechnology.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'ui_change/static/src/scss/primary_variables.scss'),
        ],
    },
}

