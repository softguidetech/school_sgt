# -*- coding: utf-8 -*-
{
    'name': "School Website sgt",

    'summary': """School figma
    """,

    'description': """
    """,

    'author': "Jamsheena kc",
    'website': "http://www.sgt.com",

    'category': 'website',
    'assets': {
        'web.assets_frontend': [
            'school_figma/static/scss/styles.scss',
        ]
    },
    'version': '0.1',

    'depends': ['base', 'portal', 'web', 'website', 'website_sale', 'website_blog','school_mngment_sgt'],
    'data': [
        "security/ir.model.access.csv",
        'views/res_company.xml',
        'views/team_work.xml',
        'views/students_comments.xml',
        'views/header.xml',
        'views/footer.xml',
        'views/home.xml',
        'views/contactus.xml',
        'views/aboutus.xml',
    ],
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}
