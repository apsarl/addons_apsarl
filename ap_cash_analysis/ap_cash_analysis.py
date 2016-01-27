# -*- coding: utf-8 -*-

import openerp
from datetime import datetime, timedelta
import time
from openerp.addons.account import account
from openerp.osv import fields, osv
from openerp import netsvc, tools, pooler
from openerp.tools.translate import _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
from openerp.tools import html2plaintext

# Class for cash forcasting
class account_cash_forcast(osv.osv):

	_name = "account.cash.forcast"
	_description = "Cash forcasting lines"
	_columns = {
			'type': fields.selection([('investment', 'Investment'),('loan', 'Loan'),('charge', 'Charge'),('income', 'Income'),('other', 'Other')], 'Type'),
			'name': fields.char('Reference'),
			'deadline': fields.date('Deadline', help="Deadline of the operation.",),
			'amount': fields.float('Amount',),
			'active': fields.boolean('Enable analysis', help="Uncheck this box if this line is not in the final analysis."),
			'line_id': fields.many2one('account.move.line', 'Journal line', help="This is the journal line",),
			'partner_id': fields.many2one('res.partner', 'Partner',), 
         }
		 
# Class report to call non reconciliated operations in moves lines
class account_cash_analysis(osv.osv):

	_name = "account.cash.analysis"
	_auto = False
	_description = "Non reconciliated operations in moves lines"
	_columns = {
            'type': fields.selection([('receivable', 'Receivable'),('payable', 'Payable'),('investment', 'Investment'),('loan', 'Loan'),('charge', 'Charge'),('income', 'Income'),('other', 'Other')], 'Type', readonly=True),   
            'name': fields.char('Reference', readonly=True), 
            'deadline': fields.date('Due date', help="This field is used for payable and receivable journal entries. You can put the limit date for the payment of this line.", readonly=True),
            'partner_id': fields.many2one('res.partner', 'Partner', readonly=True), 
			'amount': fields.float('Amount', readonly=True),
         }
		
	def init(self, cr):
		tools.drop_view_if_exists(cr, 'account_cash_analysis')
		cr.execute("""
					CREATE OR REPLACE VIEW account_cash_analysis AS ((
					SELECT MIN(account_move_line.id) as id,
					account_account.type AS type,  
					account_move_line.ref AS name, 
					account_move_line.date_maturity AS deadline,
					account_move_line.partner_id AS partner_id, 
					account_move_line.debit - account_move_line.credit as amount					
					FROM 
					public.account_move_line INNER JOIN public.account_account
												ON account_move_line.account_id = account_account.id
											LEFT JOIN public.res_partner
												ON account_move_line.partner_id = res_partner.id
					WHERE 
					account_move_line.reconcile_id IS NULL AND
					account_account.type LIKE 'receivable'
					GROUP BY
					account_account.type, account_move_line.ref, account_move_line.date_maturity, account_move_line.partner_id,  account_move_line.debit, account_move_line.credit
					UNION
					SELECT MIN(account_move_line.id) as id,
					account_account.type AS type,  
					account_move_line.ref AS name, 
					account_move_line.date_maturity AS deadline,
					account_move_line.partner_id AS partner_id, 
					account_move_line.debit - account_move_line.credit as amount
					FROM 
					public.account_move_line INNER JOIN public.account_account
												ON account_move_line.account_id = account_account.id
											LEFT JOIN public.res_partner
												ON account_move_line.partner_id = res_partner.id
					WHERE
					account_move_line.reconcile_id IS NULL AND
					account_account.type LIKE 'payable'
					GROUP BY
					account_account.type, account_move_line.date, account_move_line.ref, account_move_line.date_maturity, account_move_line.partner_id, account_move_line.debit, account_move_line.credit)
					UNION
					SELECT MIN(account_cash_forcast.id) As id,
					account_cash_forcast.type AS type,  
					account_cash_forcast.name AS name, 
					account_cash_forcast.deadline AS deadline,
					account_cash_forcast.partner_id AS partner_id, 
					account_cash_forcast.amount As amount
					FROM 
					public.account_cash_forcast
					WHERE
					account_cash_forcast.active IS True
					GROUP BY
					account_cash_forcast.type, account_cash_forcast.name, account_cash_forcast.deadline, account_cash_forcast.partner_id, account_cash_forcast.amount
				)""")   
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: