# import frappe


# def execute(filters=None):

#     columns = [
#         {
#             "label": "月份",
#             "fieldname": "month",
#             "fieldtype": "Data",
#             "width": 120
#         },
#         {
#             "label": "新增客户",
#             "fieldname": "new_customer",
#             "fieldtype": "Int",
#             "width": 120
#         },
#         {
#             "label": "流失客户",
#             "fieldname": "lost_customer",
#             "fieldtype": "Int",
#             "width": 120
#         }
#     ]


#     data = frappe.db.sql(
#         """
#         SELECT
#             DATE_FORMAT(start_date,'%Y-%m') month,

#             COUNT(DISTINCT customer_code) new_customer,

#             COUNT(
#                 DISTINCT CASE
#                     WHEN service_status='已流失'
#                     THEN customer_code
#                 END
#             ) lost_customer

#         FROM `tabCustomer Service Record`

#         GROUP BY
#             DATE_FORMAT(start_date,'%Y-%m')

#         ORDER BY month

#         """,
#         as_dict=True
#     )


#     # 折线图数据
#     chart = {
#         "data": {
#             "labels": [
#                 row.month for row in data
#             ],
#             "datasets": [
#                 {
#                     "name": "新增客户",
#                     "values": [
#                         row.new_customer for row in data
#                     ]
#                 },
#                 {
#                     "name": "流失客户",
#                     "values": [
#                         row.lost_customer for row in data
#                     ]
#                 }
#             ]
#         },
#         "type": "line",
#         "height": 300
#     }


#     return columns, data, None,chart
import frappe


def execute(filters=None):

    columns = [
        {
            "label": "月份",
            "fieldname": "month",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "新增客户",
            "fieldname": "new_customer",
            "fieldtype": "Int",
            "width": 120
        },
        {
            "label": "流失客户",
            "fieldname": "lost_customer",
            "fieldtype": "Int",
            "width": 120
        }
    ]


    data = frappe.db.sql(
        """
        SELECT
            DATE_FORMAT(start_date,'%Y-%m') month,

            COUNT(DISTINCT customer_code) new_customer,

            COUNT(
                DISTINCT CASE
                    WHEN service_status='已流失'
                    THEN customer_code
                END
            ) lost_customer

        FROM `tabCustomer Service Record`

        GROUP BY
            DATE_FORMAT(start_date,'%Y-%m')

        ORDER BY month

        """,
        as_dict=True
    )


    # 折线图数据
    chart = {
        "data": {
            "labels": [
                row.month for row in data
            ],
            "datasets": [
                {
                    "name": "新增客户",
                    "values": [
                        row.new_customer for row in data
                    ]
                },
                {
                    "name": "流失客户",
                    "values": [
                        row.lost_customer for row in data
                    ]
                }
            ]
        },
        "type": "line",
        "height": 300
    }


    return columns, data, None,chart