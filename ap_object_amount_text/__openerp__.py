# -*- encoding: utf-8 -*-

{
    'name': 'Object, Amount to text in Order and invoice',
    'version': '1.0',
    'author': 'Africa Performances',
    'category': 'Accounting',
    'website': 'http://www.africaperformances-ci.com/',
    'description': """
using code NEXTMA nextma_facture_montant_lettres from V7 
* Add object in sales order and invoice
* Add amount to text in sales order an invoice
""",
    'depends': ['sale','account',],
    'data': ['ap_object_amount_text.xml', 'sale_report.xml', 'invoice_report.xml',],
	'auto_install': False,
    'installable': True,
    'active': False,
    'application': False,	
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
