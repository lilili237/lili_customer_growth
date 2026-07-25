# Lili Customer Growth 项目说明文档

## 1. 项目简介

`Lili Customer Growth` 是一个基于 Frappe Framework 开发的客户增长与运营分析应用，主要用于展示新能源客户的生命周期、增长趋势、服务类型分布、城市分布和电池型号使用情况。

当前项目已实现两项核心能力：

1. 自定义驾驶舱页面 `customer_growth_dash`（要求 3）
2. 报表 `Customer Growth Report`（要求 2）

项目的数据来源是 `Customer Service Record` DocType，页面和报表的统计逻辑都围绕该业务对象展开。

---

## 2. 核心功能

### 2.1 客户增长驾驶舱

- 页面名称：`customer_growth_dash`
- 页面标题：`智格科技客户增长运营大屏`
- 展示内容：累计客户、活跃客户、本月新增、流失客户、增长趋势、服务类型分布、全国客户分布、电池型号统计、运营洞察

页面前端特点：

- 使用 `frappe.ui.make_app_page` 创建页面
- 使用 `frappe.call` 调用 Python 白名单接口
- 使用 `frappe.Chart` 绘制图表
- 使用 jQuery 渲染页面和样式

页面后端接口：

- `get_dashboard_data()`：返回顶部 KPI 数据
- `get_growth_trend()`：返回客户月度增长趋势
- `get_service_type()`：返回服务类型分布
- `get_city_distribution()`：返回城市分布
- `get_battery_usage()`：返回电池型号统计
- `get_world_distribution()`：返回国家分布，当前前端未接入

### 2.2 客户增长报表

- 报表名称：`Customer Growth Report`
- 报表类型：`Script Report`
- 关联 DocType：`Customer Service Record`
- 当前列：`month`、`new_customer`、`lost_customer`

说明：

- Python 负责 SQL 查询和图表数据生成
- JavaScript 负责前端格式化
- 报表权限当前仅配置 `System Manager`
- 报表 JS 中保留了 `growth` 字段格式化逻辑，但当前 Python 未返回该字段

---

## 3. 技术栈

- 框架：Frappe Framework
- 后端语言：Python
- 前端语言：JavaScript
- 数据访问方式：`frappe.db.count()`、`frappe.db.sql()`
- 图表组件：`frappe.Chart`
- 页面类型：Frappe Desk Page
- 报表类型：Script Report

---

## 4. 测试账号

- 访问地址：[http://test2.local:8000](http://test2.local:8000)
- 账号：`Administrator`
- 密码：`123456`

---

## 5. 应用基础信息

以下信息定义在 `hooks.py` 中：

- 应用名称：`lili_customer_growth`
- 应用标题：`Lili Customer Growth`
- 发布者：`lili`
- 应用描述：`Customer service lifecycle and growth analysis system`
- 联系邮箱：`13176294627@163.com`
- 许可证：`mit`
- 当前版本：`0.0.1`

模块名定义在 `modules.txt`：

- 模块名称：`Lili Customer Growth`

---

## 6. 目录结构

```text
lili_customer_growth/
├── README.md
├── __init__.py
├── hooks.py
├── modules.txt
├── patches.txt
├── config/
├── setup/
│   └── mock_data.py
├── templates/
└── lili_customer_growth/
    ├── page/
    │   └── customer_growth_dash/
    │       ├── __init__.py
    │       ├── customer_growth_dash.js
    │       ├── customer_growth_dash.json
    │       └── customer_growth_dash.py
    └── report/
        └── customer_growth_report/
            ├── __init__.py
            ├── customer_growth_report.js
            ├── customer_growth_report.json
            └── customer_growth_report.py
```

主要文件说明：

- `hooks.py`：应用基础配置入口
- `modules.txt`：定义模块名
- `patches.txt`：数据库迁移补丁入口，当前未配置实际 patch
- `setup/mock_data.py`：导入演示数据
- `page/customer_growth_dash/`：驾驶舱页面定义、前端和后端接口
- `report/customer_growth_report/`：报表定义、查询逻辑和前端格式化

---

## 7. 数据来源与依赖字段

### 7.1 核心数据对象

整个项目围绕 `Customer Service Record` 进行统计：

- 页面接口直接查询 `tabCustomer Service Record`
- 报表直接查询 `tabCustomer Service Record`
- mock 数据也写入 `Customer Service Record`

### 7.2 当前依赖字段

根据现有页面、报表和 mock 数据脚本，项目至少依赖以下字段：

- `customer_code`
- `customer_name`
- `customer_type`
- `phone`
- `city`
- `country`
- `region`
- `service_type`
- `package_name`
- `start_date`
- `end_date`
- `service_status`
- `battery_model`
- `cabinet_code`
- `battery_quantity`
- `monthly_swap_count`
- `source_channel`

其中统计逻辑明确使用到的字段有：

- `customer_code`
- `start_date`
- `service_status`
- `service_type`
- `city`
- `country`
- `battery_model`

如果这些字段缺失，页面或报表可能会查询失败或数据为空。

---

## 8. 统计逻辑

### 8.1 驾驶舱 KPI

`get_dashboard_data()` 统计内容如下：

- `total_customer`：`Customer Service Record` 总记录数
- `active_customer`：`service_status = "使用中"` 的客户数
- `lost_customer`：`service_status = "已流失"` 的客户数
- `monthly_new`：`start_date` 位于当前月份的新增客户数

### 8.2 图表统计

- `get_growth_trend()`：按月份统计客户增长数量
- `get_service_type()`：按 `service_type` 分组统计
- `get_city_distribution()`：按 `city` 分组并降序排列
- `get_battery_usage()`：过滤空电池型号后按 `battery_model` 统计
- `get_world_distribution()`：按 `country` 分组并降序排列

### 8.3 报表统计

`Customer Growth Report` 的 SQL 逻辑为：

- 使用 `start_date` 按月分组
- `COUNT(DISTINCT customer_code)` 统计新增客户
- `service_status = "已流失"` 时统计流失客户

返回结果包括：

- 表格数据
- 折线图数据

---

## 9. mock 数据说明

项目提供了演示数据脚本：

- 文件路径：`setup/mock_data.py`

作用：

- 自动插入一批 `Customer Service Record` 测试数据
- 方便本地演示、页面验证和报表验证

当前 mock 数据覆盖内容：

- 城市：杭州、上海、宁波、广州、南京、苏州、成都、武汉
- 客户类型：个人、企业、运营商
- 服务类型：租电服务、换电服务、设备服务
- 客户状态：使用中、已流失
- 电池型号：`6030`、`6045`、`4830`

脚本会根据 `customer_code` 做去重判断，因此可以重复执行而不会重复插入同一批数据。

---

## 10. 安装与部署

### 10.1 基础前提

建议准备以下环境：

- Linux 开发或部署环境
- 已安装 Frappe Bench
- 已有可用站点
- 已具备 Frappe / ERPNext 基础运行环境

### 10.2 安装应用

```bash
bench --site your-site-name install-app lili_customer_growth
```

### 10.3 执行迁移

```bash
bench --site your-site-name migrate
```

### 10.4 清缓存并重建前端

如果页面或报表更新后未生效，可执行：

```bash
bench clear-cache
bench clear-website-cache
bench build
```

---

## 11. 初始化数据

导入 mock 数据前，请先确认：

- `Customer Service Record` 已存在
- 字段已创建完整
- 当前环境具备插入权限

导入方式：

```python
from lili_customer_growth.setup.mock_data import create_mock_customer_service_records
create_mock_customer_service_records()
```

如果通过 `bench console` 执行：

```bash
bench --site your-site-name console
```

然后执行：

```python
from lili_customer_growth.setup.mock_data import create_mock_customer_service_records
create_mock_customer_service_records()
```

---

## 12. 页面和报表使用说明

### 12.1 驾驶舱页面

- 页面名：`customer_growth_dash`
- 可在 Frappe Desk 中搜索页面名称后打开

页面加载后会自动：

- 拉取 KPI 数据
- 渲染增长趋势图
- 渲染服务类型分布图
- 渲染全国客户分布图
- 渲染电池型号统计图
- 输出运营洞察文案

### 12.2 报表

- 报表名：`Customer Growth Report`
- 主要查看每月新增客户、每月流失客户和折线图趋势

如果没有权限访问报表，请先检查用户是否拥有 `System Manager` 角色。

---

## 13. 当前配置状态

### 13.1 已存在的配置

- 已配置应用基础信息
- 已定义模块 `Lili Customer Growth`
- 已定义页面 `customer_growth_dash`
- 已定义脚本报表 `Customer Growth Report`

### 13.2 当前未启用的扩展

`hooks.py` 中以下能力当前仍为默认注释状态：

- `required_apps`
- `add_to_apps_screen`
- `app_include_css`
- `app_include_js`
- `web_include_css`
- `web_include_js`
- `page_js`
- `doctype_js`
- `doc_events`
- `scheduler_events`
- `notification_config`
- `override_whitelisted_methods`
- `auth_hooks`

说明当前项目结构较轻，核心逻辑主要集中在页面、报表和 mock 数据中。

### 13.3 Patch 状态

`patches.txt` 当前没有实际 patch 条目。

---

## 14. 已知注意事项

接手项目时，建议优先注意以下几点：

1. `Customer Service Record` 的 DocType 定义未在当前仓库中看到
2. 页面和报表强依赖 SQL 查询字段
3. `get_world_distribution()` 已写好，但前端暂未使用
4. 报表 JS 中的 `growth` 格式化逻辑属于预留逻辑
5. 当前项目未配置自动化测试

---

## 15. 维护建议

后续维护时，建议按以下顺序排查：

1. 确认应用是否已安装到目标站点
2. 确认 `Customer Service Record` 是否存在
3. 确认相关字段是否完整
4. 确认页面和报表访问权限
5. 确认是否执行过 `bench migrate`
6. 确认是否执行过 `bench build`
7. 确认站点中是否已有业务数据
8. 必要时导入 mock 数据进行验证
