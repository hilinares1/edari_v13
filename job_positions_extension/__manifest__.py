# -*- coding: utf-8 -*-
{
    'name': "Job Position Extension",

    'summary': """
        Erpify""",
    'author': "Erpify",
    'website': "https://odoo.ie",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','hr'],

    # always loaded
    'data': [
        'views/job_extension.xml',
    ],

}
