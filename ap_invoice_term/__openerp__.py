# -*- encoding: utf-8 -*-

{
    'name': 'Invoice Term Analysis',
    'version': '1.0',
    'author': 'Africa Performances',
    'category': 'Accounting',
    'website': 'http://www.africaperformances-ci.com/',
    'description': """
Analysis of the partner invoice term with Odoo pivot table in reporting menu.""",
    'depends': ['account',],
    'data': ['ap_invoice_term_view.xml'],
	'auto_install': False,
    'installable': True,
    'active': False,
    'application': False,	
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: