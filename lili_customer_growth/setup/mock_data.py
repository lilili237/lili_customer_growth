import frappe
from frappe.utils import getdate


def create_mock_customer_service_records():
    """
    创建智格科技客户服务记录 Mock 数据
    """


    records = [

        # ================= 杭州 =================

        {
        "customer_code":"CUS001",
        "customer_name":"杭州骑手张伟",
        "customer_type":"个人",
        "phone":"13800000001",
        "city":"杭州",
        "service_type":"租电服务",
        "package_name":"骑手基础套餐",
        "start_date":"2026-01-05",
        "service_status":"使用中",
        "battery_model":"6030",
        "cabinet_code":"HZ-CAB-001",
        "battery_quantity":1,
        "monthly_swap_count":35,
        "source_channel":"官网",
        "region":"浙江"
        },

        {
        "customer_code":"CUS002",
        "customer_name":"杭州骑手李强",
        "customer_type":"个人",
        "phone":"13800000002",
        "city":"杭州",
        "service_type":"租电服务",
        "package_name":"骑手标准套餐",
        "start_date":"2026-01-12",
        "service_status":"使用中",
        "battery_model":"6030",
        "cabinet_code":"HZ-CAB-002",
        "battery_quantity":1,
        "monthly_swap_count":42,
        "source_channel":"线下门店",
        "region":"浙江"
        },

        {
        "customer_code":"CUS003",
        "customer_name":"杭州配送有限公司",
        "customer_type":"企业",
        "phone":"05710000003",
        "city":"杭州",
        "service_type":"换电服务",
        "package_name":"企业换电套餐",
        "start_date":"2025-12-20",
        "service_status":"使用中",
        "battery_model":"6045",
        "cabinet_code":"HZ-CAB-003",
        "battery_quantity":30,
        "monthly_swap_count":1200,
        "source_channel":"销售推广",
        "region":"浙江"
        },


        {
        "customer_code":"CUS004",
        "customer_name":"浙江绿色物流科技",
        "customer_type":"企业",
        "phone":"05710000004",
        "city":"杭州",
        "service_type":"换电服务",
        "package_name":"物流换电方案",
        "start_date":"2026-02-12",
        "service_status":"使用中",
        "battery_model":"6045",
        "cabinet_code":"HZ-CAB-004",
        "battery_quantity":50,
        "monthly_swap_count":2500,
        "source_channel":"合作伙伴",
        "region":"浙江"
        },


        # ================= 上海 =================

        {
        "customer_code":"CUS005",
        "customer_name":"上海闪送运营中心",
        "customer_type":"企业",
        "phone":"02100000005",
        "city":"上海",
        "service_type":"设备服务",
        "package_name":"智能柜部署方案",
        "start_date":"2026-01-18",
        "service_status":"使用中",
        "battery_model":"",
        "cabinet_code":"SH-CAB-001",
        "battery_quantity":0,
        "monthly_swap_count":0,
        "source_channel":"渠道代理",
        "region":"华东"
        },


        {
        "customer_code":"CUS006",
        "customer_name":"上海城市配送公司",
        "customer_type":"企业",
        "phone":"02100000006",
        "city":"上海",
        "service_type":"换电服务",
        "package_name":"城市配送套餐",
        "start_date":"2026-03-01",
        "service_status":"使用中",
        "battery_model":"6045",
        "cabinet_code":"SH-CAB-002",
        "battery_quantity":40,
        "monthly_swap_count":1800,
        "source_channel":"销售推广",
        "region":"华东"
        },


        {
        "customer_code":"CUS007",
        "customer_name":"上海换电代理商",
        "customer_type":"运营商",
        "phone":"02100000007",
        "city":"上海",
        "service_type":"换电服务",
        "package_name":"运营合作套餐",
        "start_date":"2026-02-20",
        "service_status":"使用中",
        "battery_model":"4830",
        "cabinet_code":"SH-CAB-003",
        "battery_quantity":70,
        "monthly_swap_count":3200,
        "source_channel":"合作伙伴",
        "region":"华东"
        },


        # ================= 宁波 =================

        {
        "customer_code":"CUS008",
        "customer_name":"宁波换电运营商",
        "customer_type":"运营商",
        "phone":"05740000008",
        "city":"宁波",
        "service_type":"换电服务",
        "package_name":"运营商合作套餐",
        "start_date":"2025-08-15",
        "end_date":"2026-02-10",
        "service_status":"已流失",
        "battery_model":"4830",
        "cabinet_code":"NB-CAB-001",
        "battery_quantity":80,
        "monthly_swap_count":4000,
        "source_channel":"合作伙伴",
        "region":"浙江"
        },


        {
        "customer_code":"CUS009",
        "customer_name":"宁波物流服务中心",
        "customer_type":"企业",
        "phone":"05740000009",
        "city":"宁波",
        "service_type":"换电服务",
        "package_name":"物流套餐",
        "start_date":"2026-03-05",
        "service_status":"使用中",
        "battery_model":"6045",
        "cabinet_code":"NB-CAB-002",
        "battery_quantity":25,
        "monthly_swap_count":900,
        "source_channel":"销售推广",
        "region":"浙江"
        },


        # ================= 广州 =================

        {
        "customer_code":"CUS010",
        "customer_name":"广州新能源运营商",
        "customer_type":"运营商",
        "phone":"02000000010",
        "city":"广州",
        "service_type":"换电服务",
        "package_name":"城市运营套餐",
        "start_date":"2026-01-25",
        "service_status":"使用中",
        "battery_model":"4830",
        "cabinet_code":"GZ-CAB-001",
        "battery_quantity":100,
        "monthly_swap_count":5000,
        "source_channel":"合作伙伴",
        "region":"广东"
        },


        {
        "customer_code":"CUS011",
        "customer_name":"广州外卖服务站",
        "customer_type":"企业",
        "phone":"02000000011",
        "city":"广州",
        "service_type":"租电服务",
        "package_name":"骑手服务套餐",
        "start_date":"2026-02-05",
        "service_status":"使用中",
        "battery_model":"6030",
        "cabinet_code":"GZ-CAB-002",
        "battery_quantity":10,
        "monthly_swap_count":400,
        "source_channel":"线下门店",
        "region":"广东"
        },


        # ================= 江苏 =================

        {
        "customer_code":"CUS012",
        "customer_name":"江苏物流集团",
        "customer_type":"企业",
        "phone":"02500000012",
        "city":"南京",
        "service_type":"设备服务",
        "package_name":"物流设备方案",
        "start_date":"2025-11-10",
        "end_date":"2026-01-30",
        "service_status":"已流失",
        "battery_model":"",
        "cabinet_code":"NJ-CAB-001",
        "battery_quantity":0,
        "monthly_swap_count":0,
        "source_channel":"线下门店",
        "region":"江苏"
        },


        {
        "customer_code":"CUS013",
        "customer_name":"苏州配送中心",
        "customer_type":"企业",
        "phone":"05120000013",
        "city":"苏州",
        "service_type":"换电服务",
        "package_name":"企业换电套餐",
        "start_date":"2026-03-15",
        "service_status":"使用中",
        "battery_model":"6045",
        "cabinet_code":"SZ-CAB-001",
        "battery_quantity":35,
        "monthly_swap_count":1500,
        "source_channel":"销售推广",
        "region":"江苏"
        },


        # ================= 成都 =================

        {
        "customer_code":"CUS014",
        "customer_name":"成都物流科技",
        "customer_type":"企业",
        "phone":"02800000014",
        "city":"成都",
        "service_type":"设备服务",
        "package_name":"智能柜方案",
        "start_date":"2026-03-05",
        "service_status":"使用中",
        "battery_model":"",
        "cabinet_code":"CD-CAB-001",
        "battery_quantity":0,
        "monthly_swap_count":0,
        "source_channel":"渠道代理",
        "region":"四川"
        },


        # ================= 武汉 =================

        {
        "customer_code":"CUS015",
        "customer_name":"武汉骑手服务站",
        "customer_type":"企业",
        "phone":"02700000015",
        "city":"武汉",
        "service_type":"租电服务",
        "package_name":"骑手套餐",
        "start_date":"2025-10-08",
        "end_date":"2026-02-01",
        "service_status":"已流失",
        "battery_model":"6030",
        "cabinet_code":"WH-CAB-001",
        "battery_quantity":20,
        "monthly_swap_count":700,
        "source_channel":"官网",
        "region":"湖北"
        }

    ]


    for item in records:

        # 防止重复插入
        if frappe.db.exists(
            "Customer Service Record",
            {
                "customer_code": item["customer_code"]
            }
        ):
            continue

        doc = frappe.get_doc({
            "doctype": "Customer Service Record",
            **item
        })

        doc.insert(ignore_permissions=True)


    frappe.db.commit()

    print("Customer Service Record mock data created")


if __name__ == "__main__":
    create_mock_customer_service_records()