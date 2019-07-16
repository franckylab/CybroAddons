{
    'name': "Pharmacy Marketing",
    'summary': """Sales Representative, Doctors, Targets,..etc for Medicine filed """,
    'description': """
""",

    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'category': 'Medicine',
    'version': '0.1',
    'depends': ["base",
                'medical_feature',
                "sale", "marketing",
                "marketing_campaign",
                "hr", "account",
                "hr_payroll"],
    'data': ['views/med_marketing_view.xml',
             'views/rep_view.xml',
             'views/doctor_view.xml',
             'views/doctor_exp_view.xml', ],
    'demo': ['demo/demo.xml'],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': True,
}