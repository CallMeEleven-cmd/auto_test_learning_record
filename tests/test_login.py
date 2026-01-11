import pytest

class TestLogin:
    
    def test_login_success(self, api_client):
        """测试正常登录"""
        payload = {
            "username": "test_user", 
            "password": "123456"
        }
        response = api_client.post("/api/user/login", json=payload)
        
        assert response.status_code == 200
        result = response.json()
        assert result.get("token") is not None
        assert len(result.get("token")) > 0

    def test_login_password_error(self, api_client):
        """测试密码错误"""
        payload = {
            "username": "test_user", 
            "password": "wrong_password"
        }
        response = api_client.post("/api/user/login", json=payload)
        
        assert response.status_code == 401
        # 假设返回结构中包含 message 字段
        assert "密码错误" in response.text

    def test_login_username_empty(self, api_client):
        """测试用户名为空"""
        payload = {
            "username": "", 
            "password": "123456"
        }
        response = api_client.post("/api/user/login", json=payload)
        
        assert response.status_code == 400
        assert "用户名不能为空" in response.text
