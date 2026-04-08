# Copyright (c) 2026, Rice mill procurement system and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

    filters = filters or {}

    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():

    return [

        {
            "label": "Bill Number",
            "fieldname": "bill_no",
            "fieldtype": "Data",
            "width": 150
        },

        {
            "label": "Date",
            "fieldname": "date",
            "fieldtype": "Date",
            "width": 120
        },

        {
            "label": "Authority",
            "fieldname": "authority",
            "fieldtype": "Data",
            "width": 150
        },

        {
            "label": "PO Number",
            "fieldname": "po_no",
            "fieldtype": "Data",
            "width": 150
        },

        {
            "label": "Quantity (MT)",
            "fieldname": "qty",
            "fieldtype": "Float",
            "width": 120
        },

        {
            "label": "Invoice Total",
            "fieldname": "invoice_total",
            "fieldtype": "Currency",
            "width": 150
        },

        {
            "label": "Received Amount",
            "fieldname": "received_amount",
            "fieldtype": "Currency",
            "width": 150
        },

        {
            "label": "Outstanding Amount",
            "fieldname": "outstanding",
            "fieldtype": "Currency",
            "width": 150
        },

        {
            "label": "Days Pending",
            "fieldname": "days_pending",
            "fieldtype": "Int",
            "width": 120
        },

        {
            "label": "Payment Status",
            "fieldname": "payment_status",
            "fieldtype": "Data",
            "width": 150
        }

    ]


def get_data(filters):

    data = [

        {
            "bill_no": "PB-001",
            "date": "2024-01-01",
            "authority": "NCCF",
            "po_no": "SOR2324NCC00538",
            "qty": 25,
            "invoice_total": 1386700,
            "received_amount": 1000000,
            "outstanding": 386700,
            "days_pending": 5,
            "payment_status": "Unpaid"
        },

        {
            "bill_no": "PB-002",
            "date": "2024-01-02",
            "authority": "NAFED",
            "po_no": "SOK2425NCC00545",
            "qty": 23,
            "invoice_total": 3086700,
            "received_amount": 1200000,
            "outstanding": 186700,
            "days_pending": 10,
            "payment_status": "Partially Paid"
        },

        {
            "bill_no": "PB-003",
            "date": "2024-01-03",
            "authority": "AP",
            "po_no": "SOK2425NCC00546",
            "qty": 21,
            "invoice_total": 1386700,
            "received_amount": 1100000,
            "outstanding": 286700,
            "days_pending": 15,
            "payment_status": "Unpaid"
        },

        {
            "bill_no": "PB-004",
            "date": "2024-01-04",
            "authority": "NCCF",
            "po_no": "SOR2324NCC00537",
            "qty": 31,
            "invoice_total": 1386700,
            "received_amount": 1300000,
            "outstanding": 86700,
            "days_pending": 20,
            "payment_status": "Paid"
        },

        {
            "bill_no": "PB-005",
            "date": "2024-01-05",
            "authority": "AP",
            "po_no": "SOK2425NCC00552",
            "qty": 28,
            "invoice_total": 1386700,
            "received_amount": 1250000,
            "outstanding": 136700,
            "days_pending": 25,
            "payment_status": "Unpaid"
        }

    ]
    filtered_data = []

    for row in data:
        
        # From Date
        if filters.get("from_date") and row["date"] < str(filters["from_date"]):
            continue

        # To Date
        if filters.get("to_date") and row["date"] > str(filters["to_date"]):
            continue

        # Authority
        if filters.get("authority"):

            authority_list = filters.get("authority")

            if isinstance(authority_list, str):
                authority_list = authority_list.split(",")

            if row["authority"] not in authority_list:
                continue

        # Payment Status
        if filters.get("payment_status"):

            if row["payment_status"] != filters["payment_status"]:
                continue
        
        filtered_data.append(row)
	

    return filtered_data