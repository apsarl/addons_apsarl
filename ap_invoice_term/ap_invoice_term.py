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


# Class report to call non reconciliated operations in moves lines
class account_aged_report(osv.osv):

	_name = "account.aged.report"
	_auto = False	_description = "Non reconciliated operations in moves lines"	_columns = {            'type': fields.selection([('receivable', 'Receivable'),('payable', 'Payable')], 'Type', readonly=True),              'date': fields.date('Date', help="Date of the operation.", readonly=True),             'line_id': fields.many2one('account.move.line', 'Journal line', help="This is the journal line", readonly=True),            'ref': fields.char('Reference', readonly=True),             'date_maturity': fields.date('Due date', help="This field is used for payable and receivable journal entries. You can put the limit date for the payment of this line.", readonly=True),            'partner_id': fields.many2one('res.partner', 'Partner', readonly=True),             'account_id': fields.many2one('account.account', 'Account', readonly=True),            'debit': fields.float('Debit', readonly=True),             'credit': fields.float('Credit', readonly=True),             'reconcile_id': fields.many2one('account.move.reconcile', 'Reconcile', readonly=True),
			'amount': fields.float('Amount', readonly=True),         }
		
	def init(self, cr):
		tools.drop_view_if_exists(cr, 'account_aged_report')
		cr.execute("""
					CREATE OR REPLACE VIEW account_aged_report AS (
					SELECT MIN(account_move_line.id) as id,
					account_account.type AS type,  
					account_move_line.date AS date,
					account_move_line.ref AS ref, 
					account_move_line.date_maturity AS date_maturity,
					account_move_line.partner_id AS partner_id, 
					account_account.id AS account_id,
					account_move_line.debit AS debit, 
					account_move_line.credit AS credit,
					account_move_line.debit - account_move_line.credit as amount,					
					account_move_line.reconcile_id AS reconcile_id
					FROM 
					public.account_move_line INNER JOIN public.account_account
												ON account_move_line.account_id = account_account.id
											LEFT JOIN public.res_partner
												ON account_move_line.partner_id = res_partner.id
					WHERE 
					account_move_line.reconcile_id IS NULL AND
					account_account.type LIKE 'receivable'
					GROUP BY
					account_account.type, account_move_line.date, account_move_line.ref, account_move_line.date_maturity, account_move_line.partner_id, account_account.id, account_move_line.debit, account_move_line.credit, account_move_line.reconcile_id
					UNION
					SELECT MIN(account_move_line.id) as id,
					account_account.type AS type,  
					account_move_line.date AS date, 
					account_move_line.ref AS ref, 
					account_move_line.date_maturity AS date_maturity,
					account_move_line.partner_id AS partner_id, 
					account_account.id AS account_id,
					account_move_line.debit AS debit, 
					account_move_line.credit AS credit,
					account_move_line.debit - account_move_line.credit as amount,
					account_move_line.reconcile_id AS reconcile_id
					FROM 
					public.account_move_line INNER JOIN public.account_account
												ON account_move_line.account_id = account_account.id
											LEFT JOIN public.res_partner
												ON account_move_line.partner_id = res_partner.id
					WHERE
					account_move_line.reconcile_id IS NULL AND
					account_account.type LIKE 'payable'
					GROUP BY
					account_account.type, account_move_line.date, account_move_line.ref, account_move_line.date_maturity, account_move_line.partner_id, account_account.id, account_move_line.debit, account_move_line.credit, account_move_line.reconcile_id
				)""")   # vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: