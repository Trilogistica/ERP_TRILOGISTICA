{
    'name': 'facturacion',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Modulo de Facturación Custom',
    'description': """
        Módulo de Facturación personalizado para Odoo.
    """,
    'author': 'Tu nombre',
    'website': 'https://www.tu-sitio-web.com',
    'depends': ['account'],  # Dependencia del módulo de contabilidad de Odoo
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_views.xml',
        'data/invoice_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 1,
}

