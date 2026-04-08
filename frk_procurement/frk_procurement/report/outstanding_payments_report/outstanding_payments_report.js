// Copyright (c) 2026, Rice mill procurement system and contributors
// For license information, please see license.txt

frappe.query_reports["Outstanding Payments Report"] = {

    filters: [

        {
            fieldname: "from_date",
            label: "From Date",
            fieldtype: "Date"
        },

        {
            fieldname: "to_date",
            label: "To Date",
            fieldtype: "Date"
        },

        {
            fieldname: "authority",
            label: "Authority",
            fieldtype: "MultiSelectList",

            get_data: function(txt) {

                return [
                    { value: "NCCF", description: "NCCF" },
                    { value: "NAFED", description: "NAFED" },
                    { value: "AP", description: "AP" }
                ];
            }
        },

        {
            fieldname: "particulars",
            label: "Particulars",
            fieldtype: "MultiSelectList",
            options: "FRK Particulars"
        },

        {
            fieldname: "payment_status",
            label: "Payment Status",
            fieldtype: "Select",
            options: "\nPaid\nPartially Paid\nUnpaid"
        }

    ]
};