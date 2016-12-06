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
                        ('result', _('Compte 88 - Resultats en Instance d'affectation'))], help="This field is used to generate legal reports: profit and loss, balance sheet.", required=True),
    }