# -*- coding: utf-8 -*-
{
    'name' : 'InfoSaône - Module Odoo 13 pour AGARIC',
    'version' : '0.1',
    'author' : 'InfoSaône / Tony Galmiche',
    'category' : 'InfoSaône',
    'description': '''
InfoSaône - Module Odoo 13 pour AGARIC
    ''',
    'maintainer': 'InfoSaône',
    'website': 'https://infosaone.com',
    'depends' : [
        'base',
        'sale_management',
        'account',
    ],
    'init_xml' : [],
    'demo_xml' : [],
    'data': [
        'views/res_company_views.xml',
        'views/sale_report_templates.xml',
        'views/report_invoice.xml',
        'views/report_templates.xml',
    ],
    'installable': True,
    'active': False,
    'application': True,
}

