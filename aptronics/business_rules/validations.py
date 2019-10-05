import frappe
from frappe import _

def sales_order_unique_by_customer(doc,method):
    exists = frappe.db.sql("SELECT `current` FROM `tabSales Order` WHERE `customer_name`=%s and `po_no`=%s", (doc.customer_name, doc.po_no))
    if exists:
        frappe.throw(_("Sales order no unique for customer: {0} for order number: {1}").format(doc.customer_name, doc.po_no))