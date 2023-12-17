import frappe


def set_customer_code(doc,method):
    print(doc.custom_channel_code)
    customer_code=doc.custom_channel_code if doc.custom_channel_code else "A" +"-"+doc.custom_territory_code if doc.custom_territory_code else "B" 
    customer_count=frappe.db.count('Customer')
    customer_count=str(customer_count+1).zfill(7)
    doc.custom_customer_code=customer_code+"-"+customer_count