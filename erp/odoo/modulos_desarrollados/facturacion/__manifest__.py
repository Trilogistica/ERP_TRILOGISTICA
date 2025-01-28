{
    'name': 'facturacion',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Modulo de Facturación Custom',
    'description': """
        Módulo de Facturación personalizado para Odoo.
    """,
    'author': 'Gustavo',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 1,
}

