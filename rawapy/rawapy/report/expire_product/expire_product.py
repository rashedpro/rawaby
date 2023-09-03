# Copyright (c) 2023, slnee and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(),get_data(filters)
	return columns, data

@frappe.whitelist()
def get_user(doctype, txt, searchfield, start, page_len, filters):
	sql="""
		select 
			u.name from `tabUser`u join `tabPOS Profile User` ppu
			on u.name=ppu.user
		"""
	return frappe.db.sql(sql)

def get_columns():
	columns=[
		{"label":"Item Code","fieldname":"item_code","fieldtype":"Link","options":"Item"},
		{"label":"Item Name","fieldname":"item_name","fieldtype":"Link","options":"Item"},
		{"label":"Qty","fieldname":"qty","fieldtype":"Data"},
		{"label":"Customer","fieldname":"customer","fieldtype":"Link","options":"Customer"},
		{"label":"Posting Date","fieldname":"posting_date","fieldtype":"Datetime"},
		{"label":"Reason For Return","fieldname":"reason_for_return","fieldtype":"Data"},
		{"label":"Stock Entry Reference","fieldname":"stock_entry_reference","fieldtype":"Link","options":"Stock Entry"},
		{"label":"Sales Invoie","fieldname":"name","fieldtype":"Data"},
		{"label":"Return Against","fieldname":"return_against","fieldtype":"Data"}

	]
	return columns
	 

def get_data(filters):
	return get_sales_invoice(filters)

def get_pso_Profile(filters):
	return frappe.db.sql(""" select ppu.parent from `tabPOS Profile User`ppu where user="{0}"
					""".format(filters.get("user")),as_list=1)


def get_sales_invoice(filters):
	return frappe.db.sql("""
							select 
					  			si.reason_for_return,si.stock_entry_reference,si.customer,si.posting_date,
					  			si.name,si.return_against,
					  			sii.item_code,sii.qty,sii.item_name from `tabSales Invoice Item` as sii 
							join
					  			`tabSales Invoice` si on  si.name=sii.parent
					  		and
					  			si.is_return=1 
					  		and
					  			si.owner="{0}"
	""".format(filters.get("user")),as_dict=True)