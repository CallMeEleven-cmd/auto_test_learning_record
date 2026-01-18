# def 函数名(参数1, 参数2, 参数3):
#     “”“ 用法 ”“”
#     # 函数体

#     return 

# 1. 定义函数：提取嵌套字典中的报表名称
def get_report_name(api_response):
    """
    从FRS接口响应字典中提取第一个报表的名称
    :param api_response: 接口响应的嵌套字典
    :return: 第一个报表名称（str）
    """
    # 复用第一单元的嵌套取值逻辑
    reports_list = api_response.get("data", {}).get("reports", [])
    # 判断列表是否为空，避免索引报错
    if reports_list:
        return reports_list[0].get("report_name", "未知报表")
    else:
        return "无报表数据"

# 2. 调用函数（用第一单元的模拟接口响应）
frs_api_response = {
    "code": 200,
    "msg": "success",
    "data": {
        "reports": [
            {"report_name": "UK财务月报", "generate_time": "2024-12-01"},
            {"report_name": "US财务季报", "generate_time": "2024-09-30"}
        ]
    }
}

# 调用函数并接收返回值
first_report_name = get_report_name(frs_api_response)
print("第一个报表名称：", first_report_name)  # 输出：第一个报表名称：UK财务月报

# 测试空数据场景（验证函数鲁棒性）
empty_response = {"code": 200, "msg": "success", "data": {"reports": []}}
empty_name = get_report_name(empty_response)
print("空数据场景结果：", empty_name)  # 输出：空数据场景结果：无报表数据c