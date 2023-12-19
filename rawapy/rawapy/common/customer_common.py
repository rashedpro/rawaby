import frappe


def set_customer_code(doc,method):

    try:
        if not doc.custom_customer_code:
            last_customers=frappe.get_all("Customer",filters={"territory":doc.territory},fields=["name","custom_channel","territory","custom_territory_code","custom_channel_code","custom_customer_code"],order_by="creation desc",limit=1)
            if last_customers:
                last_customer_code=last_customers[0].custom_customer_code.split('-')[-1]
                last_customer_code=int(last_customer_code)+1
                customer_code=doc.custom_territory_code+"-"+doc.custom_channel_code
                doc.custom_customer_code=customer_code+"-"+str(last_customer_code).zfill(7)
    except Exception:
        pass

def generate_customer_code():
        territories=frappe.get_all("Territory",fields=["name","custom_codes"])
        for territory in territories:
            if territory.name  not in ["Saudi Arabia","Rest Of The World","All Territories"]:
                customers=frappe.get_all("Customer",filters={"territory":territory.name},fields=["name","custom_channel","territory","custom_territory_code","custom_channel_code"],order_by="creation")
                counter=1
                for customer in customers:
                    code=str(counter).zfill(5)
                    customer_code=territory.custom_codes+"-"+customer.custom_channel_code+"-"+code
                    cus=frappe.get_doc("Customer",customer.name)
                    cus.custom_customer_code=customer_code
                    cus.save()
                    counter+=1


