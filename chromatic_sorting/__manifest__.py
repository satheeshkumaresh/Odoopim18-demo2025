{
    'name': 'Chromatic Sorting',
    'version': '18.0',
    'category': 'Tools',
    'summary': 'Sort colors based on their chromatic values',
    'description': """
    This module allows users to sort colors based on their chromatic values using HSV.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/chromatic_sorting_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
