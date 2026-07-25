frappe.query_reports["Customer Growth Report"] = {
    // 对增长字段做颜色和方向标识，其他字段保持原样
    formatter: function (value, _row, column, _data) {
        if (column.fieldname == "growth") {
            if (value > 0) {
                return `
                    <span style="color:#00ffaa; font-weight:bold">
                        ↑ ${value}
                    </span>
                `;
            } else {
                return `
                    <span style="color:#ff5577">
                        ↓ ${value}
                    </span>
                `;
            }
        }

        return value;
    },
};
