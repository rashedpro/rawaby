frappe.ui.form.on("Customer",{
    territory:function(frm){
        frm.set_value("street_name","");
        frm.set_query("street_name", function () {
            return {
                filters: {territory:frm.doc.territory},
                
            }
        });
    }
});