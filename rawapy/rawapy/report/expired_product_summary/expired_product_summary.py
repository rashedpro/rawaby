# Copyright (c) 2023, slnee and contributors
# For license information, please see license.txt

import frappe

@frappe.whitelist()
def get_user(doctype, txt, searchfield, start, page_len, filters):
	sql="""
		select 
			u.name from `tabUser`u join `tabPOS Profile User` ppu
			on u.name=ppu.user
		"""
	return frappe.db.sql(sql)


def execute(filters=None):
	columns, data = get_columns(), get_sales_invoice(filters)
	return columns, data

def get_columns():
	columns=[
		{"label":"Warehouse","fieldname":"warehouse","fieldtype":"Link","options":"Warehouse"},
		{"label":"Item Code","fieldname":"item_code","fieldtype":"Link","options":"Item"},
		{"label":"Item Name","fieldname":"item_name","fieldtype":"Link","options":"Item"},
		{"label":"Qty","fieldname":"qty","fieldtype":"Data"},
	]
	return columns

def get_data(filters):
    return	get_sales_invoice(filters)

def get_sales_invoice(filters):
	return frappe.db.sql("""
							select 
					  			si.reason_for_return,si.stock_entry_reference,si.customer,si.posting_date,
					  			si.name,si.return_against,
					  			sii.item_code,sum(ABS(sii.qty)) as qty ,sii.item_name,sii.warehouse
					  		from `tabSales Invoice Item` as sii 
							join
					  			`tabSales Invoice` si on  si.name=sii.parent
					  		and
					  			si.is_return=1 
					  		and
					  			si.owner="{0}"
							and 
					  			si.docstatus=1
							group by sii.item_code
	""".format(filters.get("user")),as_dict=True)