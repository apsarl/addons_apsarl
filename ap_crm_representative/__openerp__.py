# -*- encoding: utf-8 -*-

{
    'name': 'Representative CRM',
    'version': '1.0',
    'author': 'AFRICA PERFORMANCES',
    'category': 'Customer Relationship Management',
    'website': 'http://www.africaperformances-ci.com/',
    'description': """
Ce module dédié aux entreprises spécialisées dans la représentation commerciale permet de 
collecter les données de vente des clients afin d’analyser leurs performances.
- Analysez les volumes, valeurs de ventes
- Fixez des objectifs par Produit, par Client, par Commercial, par Zone, etc...""",
    'depends': ['base', 'crm', 'gamification'],
    'data': ['rep_sales_view.xml', 'rep_area_view.xml', 'rep_product_view.xml', 'ap_crm_goals.xml', 'security/ir.model.access.csv'],
    'active': False,
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: