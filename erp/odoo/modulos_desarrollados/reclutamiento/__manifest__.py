{
    'name': 'Gestión de Reclutamiento',
    'version': '1.0',
    'summary': 'Módulo para gestionar reclutamiento y empleados',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/reclutamiento_views.xml',
        'views/empleado_views.xml'
    ],
    'installable': True,
    'application': True,
}
