import frappe


def make_sales_invocie(doc,method):
    if doc.is_return and doc.reason_for_return!="Normal Returns":
        custom_settings=frappe.get_doc("Custom Settings")
        data = frappe.new_doc("Stock Entry")
        data.stock_entry_type="Material Issue"
        data.purpose="Material Issue"
        for item in doc.items:
            data.append(
                    'items', {
                        "item_code": item.item_code,
                        "qty": abs(item.qty),
                        "uom": item.uom,
                        "s_warehouse":item.warehouse,
                        "expense_account":custom_settings.sales_invoice_return_expense_account
                    })
        if (hasattr(data, "items")):
            data.insert()
            ref = data.name
            data.submit()
            frappe.db.set_value('Sales Invoice', doc.name,
                                'stock_entry_reference', ref)
            
        