// Copyright (c) 2023, slnee and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales Day Book"] = {
	"filters": [
		{
			"fieldname":"user",
			"label": __("User"),
			"fieldtype": "Link",
			"options": "User",
			get_query: function () {
				return {
				  query: "rawapy.rawapy.report.sales_day_book.sales_day_book.get_user",
				};
			  },
			"reqd":1,
		},
		{
			"fieldname":"date",
			"label":__("Date"),
			"fieldtype":"Date",
			default:frappe.datetime.nowdate(),
			"reqd":1,
		}
	]
};
