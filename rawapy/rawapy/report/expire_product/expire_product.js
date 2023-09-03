// Copyright (c) 2023, slnee and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expire Product"] = {
	"filters": [
		{
			"fieldname":"user",
			"label": __("User"),
			"fieldtype": "Link",
			"options": "User",
			get_query: function () {
				return {
				  query: "rawapy.rawapy.report.expire_product.expire_product.get_user",
				};
			  },
			"reqd":1,
		},
	]
};
