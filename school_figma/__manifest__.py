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

    'depends': ['base','portal','web','website', 'website_sale','website_blog'],
    'data': [
        'views/header.xml',
        'views/footer.xml',
        'views/home.xml',
    ],
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3'
}
