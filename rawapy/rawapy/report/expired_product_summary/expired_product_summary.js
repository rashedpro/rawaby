// Copyright (c) 2023, slnee and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expired Product Summary"] = {
	"filters": [
		{
			"fieldname":"user",
			"label": __("User"),
			"fieldtype": "Link",
			"options": "User",
			get_query: function () {
				return {
				  query: "rawapy.rawapy.report.expired_product_summary.expired_product_summary.get_user",
				};
			  },
			"reqd":1,
		},
	]
};
