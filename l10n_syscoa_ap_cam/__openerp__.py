# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 AFRICA PERFORMANCES (<www.africaperformances-ci.com>).
#    contact: infos@africaperformances-ci.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'SYSCOA 2015 - Accounting Cameroon by Africa Performances',
    'version' : '1.0',
    'author' : 'Africa Performances',
    'category' : 'Localization/Account Charts',
    'description': 	"""
					Accounting chart SYSCOA for Cameroon according to the 2014 - 2015 new standards.
					- Account type from Annual Financial Statement
					- New Accounts according to the standards
					- VAT Taxes (General Tax 19,25%)
					- Fiscal Position for Cameroon (TO DO)
					""",
    'website': 'http://www.africaperformances-ci.com/',
    'depends' : ['account', 'base_vat'],
    'demo' : [],
    'data' : ['l10n_syscoa_ap_cam_data.xml','l10n_syscoa_ap_cam_wizard.xml'],
    'auto_install': False,
    'installable': True
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
