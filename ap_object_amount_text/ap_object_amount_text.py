# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp.tools import float_compare


def tradd(num):
    global t1,t2
    ch=''
    if num==0 :
        ch=''
    elif num<20:
        ch=t1[num]
    elif num>=20:
        if (num>=70 and num<=79)or(num>=90):
            z=int(num/10)-1
        else:
            z=int(num/10)
        ch=t2[z]
        num=num-z*10
        if (num==1 or num==11) and z<8:
            ch=ch+' et'
        if num>0:
            ch=ch+' '+tradd(num)
        else:
            ch=ch+tradd(num)
    return ch


def tradn(num):
    global t1,t2
    ch=''
    flagcent=False
    if num>=1000000000:
        z=int(num/1000000000)
        ch=ch+tradn(z)+' milliard'
        if z>1:
            ch=ch+'s'
        num=num-z*1000000000
    if num>=1000000:
        z=int(num/1000000)
        ch=ch+tradn(z)+' million'
        if z>1:
            ch=ch+'s'
        num=num-z*1000000
    if num>=1000:
        if num>=100000:
            z=int(num/100000)
            if z>1:
                ch=ch+' '+tradd(z)
            ch=ch+' cent'
            flagcent=True
            num=num-z*100000
            if int(num/1000)==0 and z>1:
                ch=ch+'s'
        if num>=1000:
            z=int(num/1000)
            if (z==1 and flagcent) or z>1:
                ch=ch+' '+tradd(z)
            num=num-z*1000
        ch=ch+' mille'
    if num>=100:
        z=int(num/100)
        if z>1:
            ch=ch+' '+tradd(z)
        ch=ch+" cent"
        num=num-z*100
        if num==0 and z>1:
           ch=ch+'s'
    if num>0:
        ch=ch+" "+tradd(num)
    return ch


def trad(nb, unite="Franc", decim=" "):
    global t1,t2
    nb=round(nb,2)
    t1=["","un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf"]
    t2=["","dix","vingt","trente","quarante","cinquante","soixante","soixante-dix","quatre-vingt","quatre-vingt dix"]
    z1=int(nb)
    z3=(nb-z1)*100
    z2=int(round(z3,0))
    if z1==0:
        ch="zéro"
    else:
        ch=tradn(abs(z1))
    if z1>1 or z1<-1:
        if unite!='':
            ch=ch+" "+unite+'s'
    else:
        ch=ch+" "+unite
    if z2>0:
        ch=ch+tradn(z2)
        if z2>1 or z2<-1:
            if decim!='':
                ch=ch+" "+decim+'s'
        else:
            ch=ch+" "+decim
    if nb<0:
        ch="moins "+ch
    return ch



# Inherit sale orders class
class sale_order(osv.osv):
	_name = "sale.order"
	_inherit = "sale.order"
	
	
	def _sale_amount_text(self, cr, uid, ids, name, args, context=None):
		res = {}
		for line in self.browse(cr, uid, ids, context=context):
			if line.amount_total <> 0.00:
				res[line.id] = trad(int(line.amount_total)).upper()
		return res
	
	_columns = {
		'object' : fields.char('Objet', required=False, help="Objet de l'offre"),
		'amount_text': fields.function(_sale_amount_text, string='en lettre', type='char', help="Amount in text", readonly=True),
		}
	
	def _prepare_invoice(self, cr, uid, order, lines, context=None):
		"""Prepare the dict of values to create the new invoice for a
			sales order. This method may be overridden to implement custom
			invoice generation (making sure to call super() to establish
			a clean extension chain).

			:param browse_record order: sale.order record to invoice
			:param list(int) line: list of invoice line IDs that must be
									attached to the invoice
			:return: dict of value to create() the invoice
		"""
		if context is None:
			context = {}
		journal_id = self.pool['account.invoice'].default_get(cr, uid, ['journal_id'], context=context)['journal_id']
		if not journal_id:
			raise osv.except_osv(_('Error!'),
				_('Please define sales journal for this company: "%s" (id:%d).') % (order.company_id.name, order.company_id.id))
		invoice_vals = {
			'name': order.client_order_ref or '',
			'origin': order.name,
			'type': 'out_invoice',
			'reference': order.client_order_ref or order.name,
			'account_id': order.partner_invoice_id.property_account_receivable.id,
			'partner_id': order.partner_invoice_id.id,
			'journal_id': journal_id,
			'invoice_line': [(6, 0, lines)],
			'currency_id': order.pricelist_id.currency_id.id,
			'comment': order.note,
			'payment_term': order.payment_term and order.payment_term.id or False,
			'fiscal_position': order.fiscal_position.id or order.partner_invoice_id.property_account_position.id,
			'date_invoice': context.get('date_invoice', False),
			'company_id': order.company_id.id,
			'user_id': order.user_id and order.user_id.id or False,
			'section_id' : order.section_id.id,
			'object': order.object,
		}

        # Care for deprecated _inv_get() hook - FIXME: to be removed after 6.1
		invoice_vals.update(self._inv_get(cr, uid, order, context=context))
		return invoice_vals

	
	

# Inherit sale orders class
class account_invoice(osv.osv):
	_name = "account.invoice"
	_inherit = "account.invoice"
	
	def _sale_amount_text(self, cr, uid, ids, name, args, context=None):
		res = {}
		for line in self.browse(cr, uid, ids, context=context):
			if line.amount_total <> 0.00:
				res[line.id] = trad(int(line.amount_total)).upper()
		return res
	
	_columns = {
		'object' : fields.char('Objet', required=False, help="Objet de l'offre"),
		'amount_text': fields.function(_sale_amount_text, string='en lettre', type='char', help="Amount in text", readonly=True),
		}