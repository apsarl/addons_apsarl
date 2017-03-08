# -*- coding: utf-8 -*-
# © <2016> <Africa Performances and CERCO TEAM>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import openerp
from openerp.osv import fields, osv, orm
import openerp.tools
from openerp.tools.translate import _

class res_ap_country(osv.osv)
    _name = "res.country"
    _description = 'Geolocalisation of country'

    _columns = {
        'country_latitude': fields.float('Geo Latitude', digits=(16, 5)),
        'country_longitude': fields.float('Geo Longitude', digits=(16, 5)),
    }

class res_ap_city(osv.osv):
    _name = "res.ap.city"
    _description = 'Cities with geolocalisation'
	
    _columns = {
        'name': fields.char('City', required=True, size=64, help="Name of the city", translate=True),
        'country_id': fields.many2one('res.country','Country', help="Name of the country", translate=True),
        'city_latitude': fields.float('Geo Latitude', digits=(16, 5)),
        'city_longitude': fields.float('Geo Longitude', digits=(16, 5)),
    }

class res_ap_partner(osv.osv)
    _name = "res.partner"
    _description = 'Add many2one city field'
	
    _columns = {
        'city_id': fields.many2one('res.ap.city','City', help="City", translate=True),
    }