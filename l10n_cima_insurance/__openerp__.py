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
    'name' : 'CIMA Insurance Chart of Accounts - 2014',
    'version' : '1.0',
    'author' : 'Africa Performances',
    'category' : 'Localization/Account Charts',
    'description': 	"""
					IMPORTANT: After installation, the account width must be 4
					
					- Accounting chart CIMA for Insurance companies according to the 2014 revision
					- Account type from Annual Financial Statement
					- Control all account types and chart of account (TO DO)
					- Set tax configuration (TO DO)
					
					""",
    'website': 'http://www.africaperformances-ci.com/',
    'depends' : ['account', 'base_vat','l10n_cima_insurance_account_type',],
    'demo' : [],
    'data' : ['l10n_cima_insurance_data.xml', 'l10n_cima_insurance_wizard.xml',],
	'auto_install': False,
    'installable': True,
    'active': False,
    'application': False,	
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
