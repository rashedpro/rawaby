import frappe


def set_customer_code(doc,method):
    try:
        customer_code=doc.custom_channel_code+"-"+doc.custom_territory_code
        customer_count=frappe.db.count('Customer')
        customer_count=str(customer_count+1).zfill(7)
        doc.custom_customer_code=customer_code+"-"+customer_count
    except Exception:
        pass