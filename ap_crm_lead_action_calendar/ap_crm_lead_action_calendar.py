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

	
class crm_lead(osv.osv):
    _name = "crm.lead"
    _inherit = "crm.lead"
    _order= "create_date desc"
	
    _columns = {
        'calendar_id': fields.many2one('calendar.event','Next Action Planned', help="Plan the next action to do in calendar"),
		'planned_date': fields.datetime('Planned Date',)
    }
	
	
    def on_change_calendar_id(self, cr, uid, ids, calendar_id, context=None):
        values = {}
        if calendar_id:
            calendar = self.pool.get('calendar.event').browse(cr, uid, calendar_id, context=context)
            values = {'planned_date': calendar.start_datetime,}
        return {'value': values}