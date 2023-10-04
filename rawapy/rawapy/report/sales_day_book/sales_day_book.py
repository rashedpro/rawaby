# Copyright (c) 2023, slnee and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data =get_columns(),get_data(filters)
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
		{"label":"Type Of Transaction ","fieldname":"Type_of_transaction","fieldtype":"data"},
		{"label":"Voucher","fieldname":"voucher","fieldtype":"data"},
		{"label":"Received Amount","fieldname":"received_amount","fieldtype":"data"},
	]
	return columns

def get_data(filters):
	
	sales_invoice=get_sales_invoice(filters)
	payment_entry=get_payment_entry(filters)

	return sales_invoice+payment_entry


def get_sales_invoice(filters):
	condition=get_condition(filters)
	
	data=frappe.db.sql(""" select name as voucher ,paid_amount as received_amount ,'Sales Invoice' as Type_of_transaction
					 		from `tabSales Invoice` where {}  and is_pos=1
			""".format(condition), as_dict=1)
	
	return data



def get_payment_entry(filters):
	condition=get_condition(filters)
	
	data=frappe.db.sql(""" select name as voucher ,total_allocated_amount as received_amount,'Payment Entry' as Type_of_transaction 
					 		from `tabPayment Entry` where {} 
			""".format(condition), as_dict=1)
	
	return data
def get_condition(filters):
	condition="owner='{0}' and posting_date ='{1}'".format(filters.get("user"),filters.get("date"))
	return condition
