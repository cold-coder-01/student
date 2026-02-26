{
    'name': 'Student System',
    'version': '1.0',
    'author': 'Abel M',
    'description': 'School Managment System',
    'category':'Managment',
    'depends':['base', 'web'],
    'data':[
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/student_inherit_views.xml',
        'views/partner_inherit_view.xml',
        'views/menu_view.xml',
    ],
    'installable': True,
    'application': True,
}