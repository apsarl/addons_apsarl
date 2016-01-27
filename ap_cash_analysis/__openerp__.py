# -*- encoding: utf-8 -*-

{
    'name': 'Cash Analysis and forcasting',
    'version': '1.0',
    'author': 'Africa Performances',
    'category': 'Accounting',
    'website': 'http://www.africaperformances-ci.com/',
    'description': """
Analysis of the partner invoice term with Odoo pivot table in reporting menu.""",
    'depends': ['account', 'account_budget'],
    'data': ['ap_cash_analysis_view.xml'],
    'active': False,
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: