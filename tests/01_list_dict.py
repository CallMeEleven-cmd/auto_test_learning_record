# reports_list = frs_api_response.get("data", {}).get("users", [])

# print("\n借款信息：")
# for report in reports_list:
#     name = report.get("username", "未知")
#     amount = report.get("loan_amount", "未知")
#     print(f"用户姓名：{name}，借款金额：{amount}")


upcredit_api_response = {
    "code": 200,
    "msg": "success",
    "data": {
        "users": [
            {"username": "user001", "loan_amount": 5000, "region": "UK"},
            {"username": "user002", "loan_amount": 8000, "region": "UK"},
            {"username": "user003", "loan_amount": 3000, "region": "US"}
        ],
        "total_user": 3
    }
}

# 提取字段+统计总金额
users_list = upcredit_api_response.get("data", {}).get("users", [])
total_loan = 0  # 初始化总金额

print("用户贷款信息：")
for user in users_list:
    username = user.get("username", "未知用户")
    loan = user.get("loan_amount", 0)
    total_loan += loan  # 累加金额
    print(f"用户名：{username}，贷款金额：{loan}英镑")

print(f"\n所有用户贷款总金额：{total_loan}英镑")




upcredit_api_response = {
    "code": 200,
    "msg": "success",
    "data": {
        "users": [
            {"username": "user001", "loan_amount": 5000, "region": "UK"},
            {"username": "user002", "loan_amount": 8000, "region": "UK"},
            {"username": "user003", "loan_amount": 3000, "region": "US"}
        ],
        "total_user": 3
    }
}

#提取字段
User_list1= upcredit_api_response.get("data", {}).get("users", [])
total_loan1 = 0  # 初始化总金额

for user1 in User_list1:
    username1 = user1.get("username", "未知用户")
    loan1 = user1.get("loan_amount", 0)
    
    total_loan1 += loan1  # 累加金额
    print(f"{username1}贷款金额为{loan1}英镑")
print(f"当前放贷总金额：{total_loan1}英镑")
