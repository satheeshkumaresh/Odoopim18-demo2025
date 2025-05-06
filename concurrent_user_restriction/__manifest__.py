# -*- coding: utf-8 -*-
{
    'name': 'MisterArt Odoo PIM-concurrent login restriction',
    'version': '18.0',
    "author": "Navabrind IT",
    'summary': '',
    'description': """ OdooPIM For MisterArt

    """,
    'category': 'product',
    'depends': ['pim_ext'],
    'data': [
        'data/data.xml',
            'security/ir.model.access.csv',
            # 'views/family_attribute.xml',
            # 'views/product_attribute.xml',
            # 'views/product_brand.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'concurrent_user_restriction/static/src/js/form_controller.js',
            'concurrent_user_restriction/static/src/xml/formView.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
