import frappe


@frappe.whitelist()
def get_dashboard_data():
    # 汇总驾驶舱顶部 KPI 数据
    total_customer = frappe.db.count("Customer Service Record")
    active_customer = frappe.db.count(
        "Customer Service Record",
        {"service_status": "使用中"},
    )
    lost_customer = frappe.db.count(
        "Customer Service Record",
        {"service_status": "已流失"},
    )
    monthly_new = frappe.db.sql(
        """
        SELECT COUNT(DISTINCT customer_code)
        FROM `tabCustomer Service Record`
        WHERE DATE_FORMAT(start_date, '%Y-%m')
            = DATE_FORMAT(CURDATE(), '%Y-%m')
        """
    )[0][0]

    return {
        "total_customer": total_customer,
        "active_customer": active_customer,
        "monthly_new": monthly_new,
        "lost_customer": lost_customer,
    }


@frappe.whitelist()
def get_growth_trend():
    # 返回按月份统计的客户增长趋势
    data = frappe.db.sql(
        """
        SELECT
            DATE_FORMAT(start_date,'%Y-%m') month,
            COUNT(DISTINCT customer_code) total
        FROM `tabCustomer Service Record`
        GROUP BY
            DATE_FORMAT(start_date,'%Y-%m')
        ORDER BY month
        """,
        as_dict=True,
    )

    return data


@frappe.whitelist()
def get_service_type():
    # 统计各服务类型的客户数量
    data = frappe.db.sql(
        """
        SELECT
            service_type,
            COUNT(DISTINCT customer_code) AS total
        FROM `tabCustomer Service Record`
        GROUP BY service_type
        """,
        as_dict=True,
    )

    return data


@frappe.whitelist()
def get_city_distribution():
    # 统计各城市客户分布并按数量降序展示
    data = frappe.db.sql(
        """
        SELECT
            city,
            COUNT(DISTINCT customer_code) AS total
        FROM `tabCustomer Service Record`
        GROUP BY city
        ORDER BY total DESC
        """,
        as_dict=True,
    )

    return data


@frappe.whitelist()
def get_battery_usage():
    # 统计电池型号使用情况，过滤空值
    data = frappe.db.sql(
        """
        SELECT
            battery_model,
            COUNT(*) AS total
        FROM `tabCustomer Service Record`
        WHERE
            battery_model IS NOT NULL
            AND battery_model != ''
        GROUP BY battery_model
        ORDER BY total DESC
        """,
        as_dict=True,
    )

    return data


@frappe.whitelist()
def get_world_distribution():
    # 统计各国家客户分布
    data = frappe.db.sql(
        """
        SELECT
            country,
            COUNT(DISTINCT customer_code) AS total
        FROM `tabCustomer Service Record`
        GROUP BY country
        ORDER BY total DESC
        """,
        as_dict=True,
    )

    return data
