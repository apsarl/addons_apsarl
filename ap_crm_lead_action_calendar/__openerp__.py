# -*- coding: utf-8 -*-
# © <2016> <Africa Performances>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Lead next action in calendar ",
    "version": "8.0.1.0.0",
    "category": "CRM",
    "website": "http://www.africaperformances-ci.com/",
    "author": "Africa Performances",
	'description': """
	Add a field inside the leads-opportunity form view to plan action or operation in calendar
	""",
    "application": False,
    "installable": True,
    "depends": ["base", "crm",],
	"data": ["ap_crm_lead_action_calendar.xml"],
}
