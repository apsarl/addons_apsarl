# -*- coding: utf-8 -*-
# © <2016> <Africa Performances and CERCO TEAM>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import openerp
from openerp.osv import fields, osv, orm
import openerp.tools
from openerp.tools.translate import _

class res_ap_city(osv.osv):
    _name = "res.ap.city"
    _description = 'Cities of country'
	
    _columns = {
        'name': fields.char('City', required=True, size=64, help="Name of the city", translate=True),
		'country_id': fields.many2one('res.country','Country', help="Name of the country", translate=True),
    }