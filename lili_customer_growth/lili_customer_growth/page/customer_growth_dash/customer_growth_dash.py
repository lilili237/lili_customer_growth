import frappe


@frappe.whitelist()
def get_dashboard_data():

    total_customer = frappe.db.count(
        "Customer Service Record"
    )

    active_customer = frappe.db.count(
        "Customer Service Record",
        {
            "service_status": "使用中"
        }
    )

    lost_customer = frappe.db.count(
        "Customer Service Record",
        {
            "service_status": "已流失"
        }
    )

    monthly_new = frappe.db.sql(
        """
        SELECT COUNT(DISTINCT customer_code)
        FROM `tabCustomer Service Record`
        WHERE DATE_FORMAT(start_date,'%Y-%m')
        =
        DATE_FORMAT(CURDATE(),'%Y-%m')
        """
    )[0][0]


    return {
        "total_customer": total_customer,
        "active_customer": active_customer,
        "monthly_new": monthly_new,
        "lost_customer": lost_customer
    }

@frappe.whitelist()
def get_growth_trend():

    data = frappe.db.sql("""
        SELECT
            DATE_FORMAT(start_date,'%Y-%m') month,
            COUNT(DISTINCT customer_code) total
        FROM
            `tabCustomer Service Record`
        GROUP BY
            DATE_FORMAT(start_date,'%Y-%m')
        ORDER BY month
    """, as_dict=True)

    return data



@frappe.whitelist()
def get_service_type():

    data = frappe.db.sql(
        """
        SELECT
            service_type,
            COUNT(DISTINCT customer_code) AS total

        FROM
            `tabCustomer Service Record`

        GROUP BY
            service_type

        """,
        as_dict=True
    )

    return data

@frappe.whitelist()
def get_city_distribution():

    data = frappe.db.sql(
        """
        SELECT
            city,
            COUNT(DISTINCT customer_code) AS total

        FROM
            `tabCustomer Service Record`

        GROUP BY
            city

        ORDER BY
            total DESC

        """,
        as_dict=True
    )

    return data


@frappe.whitelist()
def get_battery_usage():

    data = frappe.db.sql(
        """
        SELECT
            battery_model,
            COUNT(*) AS total

        FROM
            `tabCustomer Service Record`

        WHERE
            battery_model IS NOT NULL
            AND battery_model != ''

        GROUP BY
            battery_model

        ORDER BY
            total DESC

        """,
        as_dict=True
    )

    return data

@frappe.whitelist()
def get_world_distribution():

    data = frappe.db.sql(
        """
        SELECT

            country,

            COUNT(DISTINCT customer_code) AS total


        FROM
            `tabCustomer Service Record`


        GROUP BY
            country


        ORDER BY
            total DESC

        """,
        as_dict=True
    )


    return data