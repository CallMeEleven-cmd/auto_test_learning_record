import pytest
from utils.api_client import APIClient
import json

@pytest.fixture(scope="session")
def api_client():
    # 实际项目中应从配置文件读取URL
    base_url = "https://xxx.com"
    return APIClient(base_url)

@pytest.fixture(autouse=True)
def mock_api_responses(requests_mock):
    """
    Mock API 响应用于演示。
    在真实环境中，请移除此 fixture 或禁用 requests_mock。
    """
    def login_callback(request, context):
        try:
            json_data = request.json()
        except:
            context.status_code = 400
            return "Invalid JSON"
            
        username = json_data.get("username")
        password = json_data.get("password")
        
        # 场景3: 用户名为空
        if not username:
            context.status_code = 400
            # 模拟返回提示信息
            return "用户名不能为空"
            
        # 场景1: 正常登录
        if username == "test_user" and password == "123456":
            context.status_code = 200
            return json.dumps({"token": "mock-token-xyz", "message": "Login successful"})
            
        # 场景2: 密码错误
        context.status_code = 401
        return "密码错误"

    # 注册 mock, 使用 text 参数接收字符串响应
    requests_mock.post("https://xxx.com/api/user/login", text=login_callback)
