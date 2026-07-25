// frappe.query_reports["Customer Growth Report"] = {

//     formatter(value, row, column, data) {
//         return value;
//     },

//     chart: {
//         type: "line"
//     }

// };
frappe.query_reports["Customer Growth Report"] = {


    formatter:function(
        value,
        row,
        column,
        data
    ){


        if(column.fieldname=="growth"){


            if(value>0){

                return `

                <span style="
                color:#00ffaa;
                font-weight:bold">

                ↑ ${value}

                </span>

                `;

            }


            else{


                return `

                <span style="
                color:#ff5577">

                ↓ ${value}

                </span>

                `;


            }


        }


        return value;


    },


};