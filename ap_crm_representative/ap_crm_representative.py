# -*- coding: utf-8 -*-

import openerp
from datetime import datetime, timedelta
import time
from openerp.addons.crm import crm
from openerp.osv import fields, osv
from openerp import netsvc, tools, pooler
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from openerp.tools import html2plaintext


#sales area to configure
class rep_area(osv.osv):
    """ Areas of sales """

    _name = "rep.area"
    _description = "Area of representative sales"

    _columns = {
            'name': fields.char('Area', size=200, help="Name of the sales area", required=True),
            'company_id': fields.many2one('res.company', 'Company'),
         }
		 
#sales product to configure		 
class rep_product(osv.osv):
    """ product sales """

    _name = "rep.product"
    _description = "Product sales by representative"

    _columns = {
            'name': fields.char('Products', size=200, help="Name of the product sale" , required=True),
            'company_id': fields.many2one('res.company', 'Company'),
         }		 

#line of sales		 
class rep_sales(osv.osv):
    """ customers sales """

    _name = "rep.sales"
    _description = "Lines of customers sales"
    _order = "salecustom_date asc"

    _columns = {
            'salecustom_date': fields.date('Sale Date' , readonly=False, required=True),
            'partner_id': fields.many2one('res.partner', 'Partner' , readonly=False, required=True),
            'areas_id': fields.many2one('rep.area', 'Areas' , readonly=False, required=True),
            'saleproducts_id': fields.many2one('rep.product', 'Products' , readonly=False, required=True),
			'user_id': fields.many2one('res.users', 'Salesperson' , readonly=False, required=False),
            'salecustom_quantity': fields.float('Quantity' , readonly=False, required=True),
            'salecustom_unitprice': fields.float('Unit Price' , readonly=False, required=True),
            'salecustom_amount': fields.float('Amount' , readonly=False, required=True),
            'company': fields.many2one('res.company', 'Company', readonly=False),
         }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
