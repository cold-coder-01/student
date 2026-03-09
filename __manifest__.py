{
    'name': 'Student System',
    'version': '1.1',
    'author': 'Abel M',
    'description': 'School Management System',
    'category': 'Management',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_sequence.xml',
        'views/student_views.xml',
        'views/partner_inherit_view.xml',
        'views/menu_view.xml',
    ],
    'installable': True,
    'application': True,
}
