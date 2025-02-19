{
    'name': 'Empleados y Ausencias',
    'version': '1.0',
    'summary': 'Gestión de empleados y ausencias',
    'category': 'Human Resources',
    'depends': ['base'],
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
        'models/models.py'
    ],
    'installable': True,
    'application': True,
}

