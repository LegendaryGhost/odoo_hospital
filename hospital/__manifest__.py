{
    'name': "Hospital",
    'version': '1.0',
    'depends': ['base'],
    'author': "Tiarintsoa",
    'description': "An app module to manage an hospital",
    'category': "Hospital Management",
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',

        'data/disease_demo.xml',

        'views/hospital_disease_views.xml',
        'views/hospital_symptom_views.xml',
        'views/hospital_menus.xml',
    ]
}