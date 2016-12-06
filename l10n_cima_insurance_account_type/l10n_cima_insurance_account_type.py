# -*- coding: utf-8 -*-
# © <2016> <Africa Performances>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import openerp
from openerp import tools, api
from openerp.osv import fields, osv, orm
from openerp.osv.expression import get_unaccent_wrapper

from openerp import SUPERUSER_ID
from openerp import tools
from openerp.tools.translate import _
from openerp.tools import email_re, email_split

from lxml import etree
import math
import pytz
import urlparse

from datetime import datetime
from operator import itemgetter



class account_account_type(osv.osv):
    _name = "account.account.type"
    _inherit = "account.account.type"
	
    def _get_financial_report_ref(self, cr, uid, context=None):
        obj_data = self.pool.get('ir.model.data')
        obj_financial_report = self.pool.get('account.financial.report')
        financial_report_ref = {}
        for key, financial_report in [
                    ('asset','account_financial_report_assets0'),
                    ('liability','account_financial_report_liability0'),
                    ('income','account_financial_report_income0'),
                    ('expense','account_financial_report_expense0'),
                    ('bilan','account_financial_report_bilan0'),
                    ('asstn','account_financial_report_asstn0'),
                    ('vicapi','account_financial_report_vicapi0'),
                    ('perprof','account_financial_report_perprof0'),
                    ('result','account_financial_report_result0'),                                                                                                
                    ]:
            try:
                financial_report_ref[key] = obj_financial_report.browse(cr, uid,
                    obj_data.get_object_reference(cr, uid, 'l10n_cima_insurance_account_type', financial_report)[1] ,
                    context=context)
                
            except ValueError:
                try:
                    financial_report_ref[key] = obj_financial_report.browse(cr, uid,
                    obj_data.get_object_reference(cr, uid, 'account', financial_report)[1],
                    context=context)
                except ValueError:
                    pass
        return financial_report_ref

    def _get_current_report_type(self, cr, uid, ids, name, arg, context=None):
        res = {}
        financial_report_ref = self._get_financial_report_ref(cr, uid, context=context)
        for record in self.browse(cr, uid, ids, context=context):
            res[record.id] = 'none'
            for key, financial_report in financial_report_ref.items():
                list_ids = [x.id for x in financial_report.account_type_ids]
                if record.id in list_ids:
                    res[record.id] = key
        return res

    def _save_report_type(self, cr, uid, account_type_id, field_name, field_value, arg, context=None):
        field_value = field_value or 'none'
        obj_financial_report = self.pool.get('account.financial.report')
        #unlink if it exists somewhere in the financial reports related to BS or PL
        financial_report_ref = self._get_financial_report_ref(cr, uid, context=context)
        for key, financial_report in financial_report_ref.items():
            list_ids = [x.id for x in financial_report.account_type_ids]
            if account_type_id in list_ids:
                obj_financial_report.write(cr, uid, [financial_report.id], {'account_type_ids': [(3, account_type_id)]})
        #write it in the good place
        if field_value != 'none':
            return obj_financial_report.write(cr, uid, [financial_report_ref[field_value].id], {'account_type_ids': [(4, account_type_id)]})

    _columns = {
        'report_type': fields.function(_get_current_report_type, fnct_inv=_save_report_type, type='selection', string='P&L / BS Category', store=True,
            selection= [('none','/'),
                        ('income', _('Profit & Loss (Income account)')),
                        ('expense', _('Profit & Loss (Expense account)')),
                        ('asset', _('Balance Sheet (Asset account)')),
                        ('liability', _('Balance Sheet (Liability account)')),
                        ('bilan', _('Compte 89 - Bilan')),
                        ('asstn', _('Compte 80 - Assurances De Toute Nature')),
                        ('vicapi', _('Compte 80 - Vie / Capitalisation')),
                        ('perprof', _('Compte 87 - Compte General de Pertes et Profits')),						
                        ('result', _('Compte 88 - Resultats en Instance affectation'))], help="This field is used to generate legal reports: profit and loss, balance sheet.", required=True),
    }


def _code_get(self, cr, uid, context=None):
    acc_type_obj = self.pool.get('account.account.type')
    ids = acc_type_obj.search(cr, uid, [])
    res = acc_type_obj.read(cr, uid, ids, ['code', 'name'], context=context)
    return [(r['code'], r['name']) for r in res]


