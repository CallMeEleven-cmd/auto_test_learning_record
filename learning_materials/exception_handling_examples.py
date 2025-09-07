# 异常处理学习素材和练习

import logging
import json
from typing import Optional

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 1. 基础异常处理
def basic_exception_handling():
    """基础异常处理示例"""
    print("=== 基础异常处理 ===")
    
    # try-except 基本用法
    try:
        number = int(input("请输入一个数字: "))
        result = 10 / number
        print(f"10 除以 {number} 等于 {result}")
    except ValueError:
        print("错误：输入的不是有效数字")
    except ZeroDivisionError:
        print("错误：不能除以零")
    except Exception as e:
        print(f"发生了未预期的错误: {e}")
    else:
        print("计算成功完成")
    finally:
        print("无论是否发生异常都会执行这里")

# 2. 自定义异常
class CustomError(Exception):
    """自定义异常基类"""
    pass

class ValidationError(CustomError):
    """数据验证异常"""
    def __init__(self, message, field_name=None):
        self.message = message
        self.field_name = field_name
        super().__init__(self.message)

class BusinessLogicError(CustomError):
    """业务逻辑异常"""
    pass

class DataNotFoundError(CustomError):
    """数据未找到异常"""
    def __init__(self, data_type, identifier):
        self.data_type = data_type
        self.identifier = identifier
        message = f"{data_type} with identifier '{identifier}' not found"
        super().__init__(message)

# 3. 用户注册系统示例
class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

class UserRegistry:
    def __init__(self):
        self.users = {}
    
    def validate_user_data(self, username, email, age):
        """验证用户数据"""
        if not username or len(username) < 3:
            raise ValidationError("用户名长度至少3个字符", "username")
        
        if "@" not in email or "." not in email:
            raise ValidationError("邮箱格式不正确", "email")
        
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValidationError("年龄必须是0-150之间的整数", "age")
        
        if username in self.users:
            raise BusinessLogicError(f"用户名 '{username}' 已存在")
    
    def register_user(self, username, email, age):
        """注册用户"""
        try:
            self.validate_user_data(username, email, age)
            user = User(username, email, age)
            self.users[username] = user
            logger.info(f"用户 {username} 注册成功")
            return user
        except ValidationError as e:
            logger.error(f"数据验证失败: {e.message} (字段: {e.field_name})")
            raise
        except BusinessLogicError as e:
            logger.error(f"业务逻辑错误: {e}")
            raise
        except Exception as e:
            logger.error(f"注册用户时发生未知错误: {e}")
            raise CustomError("用户注册失败") from e
    
    def get_user(self, username):
        """获取用户"""
        if username not in self.users:
            raise DataNotFoundError("User", username)
        return self.users[username]

# 4. 文件操作异常处理
def safe_file_operations():
    """安全的文件操作"""
    
    def read_json_file(filename):
        """安全读取JSON文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            logger.error(f"文件 {filename} 不存在")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"JSON文件格式错误: {e}")
            return None
        except PermissionError:
            logger.error(f"没有权限读取文件 {filename}")
            return None
        except Exception as e:
            logger.error(f"读取文件时发生未知错误: {e}")
            return None
    
    def write_json_file(filename, data):
        """安全写入JSON文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
                logger.info(f"数据成功写入文件 {filename}")
                return True
        except (IOError, OSError) as e:
            logger.error(f"写入文件失败: {e}")
            return False
        except TypeError as e:
            logger.error(f"数据序列化失败: {e}")
            return False
    
    # 测试文件操作
    test_data = {"name": "张三", "age": 25, "city": "北京"}
    
    if write_json_file("test_data.json", test_data):
        loaded_data = read_json_file("test_data.json")
        if loaded_data:
            print(f"读取的数据: {loaded_data}")

# 5. 网络请求异常处理
def safe_network_request():
    """安全的网络请求示例"""
    import requests
    from requests.exceptions import RequestException, Timeout, ConnectionError
    
    def fetch_data(url, timeout=10):
        """安全的HTTP请求"""
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # 如果状态码不是200会抛出异常
            return response.json()
        except Timeout:
            logger.error(f"请求超时: {url}")
            return None
        except ConnectionError:
            logger.error(f"连接失败: {url}")
            return None
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP错误: {e}")
            return None
        except json.JSONDecodeError:
            logger.error("响应不是有效的JSON格式")
            return None
        except RequestException as e:
            logger.error(f"请求异常: {e}")
            return None

# 6. 上下文管理器与异常处理
class DatabaseConnection:
    """模拟数据库连接上下文管理器"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"连接到数据库 {self.db_name}")
        self.connection = f"connection_to_{self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"操作过程中发生异常: {exc_type.__name__}: {exc_value}")
            print("回滚事务")
        else:
            print("提交事务")
        
        print(f"关闭数据库连接 {self.db_name}")
        self.connection = None
        # 返回False表示不抑制异常
        return False

def database_operation_example():
    """数据库操作示例"""
    try:
        with DatabaseConnection("user_db") as conn:
            print(f"使用连接 {conn} 执行数据库操作")
            # 模拟可能出错的操作
            raise ValueError("模拟数据库操作错误")
    except ValueError as e:
        print(f"捕获到异常: {e}")

# 7. 异常链和异常重新抛出
def exception_chaining_example():
    """异常链示例"""
    
    def low_level_function():
        """底层函数"""
        raise ValueError("底层错误")
    
    def mid_level_function():
        """中层函数"""
        try:
            low_level_function()
        except ValueError as e:
            # 异常链：保留原始异常信息
            raise RuntimeError("中层处理失败") from e
    
    def high_level_function():
        """高层函数"""
        try:
            mid_level_function()
        except RuntimeError as e:
            print(f"高层捕获异常: {e}")
            print(f"原始异常: {e.__cause__}")

# 8. 异常处理最佳实践
class APIClient:
    """API客户端示例 - 展示异常处理最佳实践"""
    
    def __init__(self, base_url):
        self.base_url = base_url
    
    def make_request(self, endpoint, data=None):
        """发起API请求"""
        url = f"{self.base_url}/{endpoint}"
        
        try:
            # 这里模拟API请求
            if endpoint == "error":
                raise ConnectionError("网络连接失败")
            elif endpoint == "invalid":
                raise ValueError("无效的请求数据")
            
            return {"status": "success", "data": data}
            
        except ConnectionError:
            logger.error(f"网络连接失败: {url}")
            # 重新抛出，让调用者处理
            raise
        except ValueError as e:
            logger.error(f"请求数据无效: {e}")
            # 转换为更具体的业务异常
            raise ValidationError("请求数据格式错误") from e
        except Exception as e:
            logger.error(f"API请求意外失败: {e}")
            # 包装未知异常
            raise CustomError("API请求失败") from e

# 主函数和练习
def main():
    """主函数 - 运行所有示例"""
    
    print("=== 异常处理学习示例 ===\n")
    
    # 1. 基础异常处理
    # basic_exception_handling()  # 注释掉因为需要用户输入
    
    # 2. 自定义异常和用户注册系统
    print("=== 用户注册系统示例 ===")
    registry = UserRegistry()
    
    # 成功案例
    try:
        user = registry.register_user("alice", "alice@example.com", 25)
        print(f"用户注册成功: {user.username}")
    except CustomError as e:
        print(f"注册失败: {e}")
    
    # 失败案例
    test_cases = [
        ("ab", "alice@example.com", 25),  # 用户名太短
        ("bob", "invalid-email", 25),      # 邮箱格式错误
        ("charlie", "charlie@example.com", -5),  # 年龄无效
        ("alice", "alice2@example.com", 30),     # 用户名已存在
    ]
    
    for username, email, age in test_cases:
        try:
            registry.register_user(username, email, age)
        except CustomError as e:
            print(f"注册失败 - {username}: {e}")
    
    # 3. 获取用户示例
    try:
        user = registry.get_user("alice")
        print(f"找到用户: {user.username}")
        
        unknown_user = registry.get_user("unknown")
    except DataNotFoundError as e:
        print(f"用户查找失败: {e}")
    
    # 4. 文件操作
    print("\n=== 文件操作示例 ===")
    safe_file_operations()
    
    # 5. 数据库操作
    print("\n=== 数据库操作示例 ===")
    database_operation_example()
    
    # 6. 异常链
    print("\n=== 异常链示例 ===")
    exception_chaining_example()
    
    # 7. API客户端
    print("\n=== API客户端示例 ===")
    client = APIClient("https://api.example.com")
    
    # 测试不同的异常情况
    test_endpoints = ["success", "error", "invalid"]
    for endpoint in test_endpoints:
        try:
            result = client.make_request(endpoint, {"test": "data"})
            print(f"请求成功: {endpoint} -> {result}")
        except CustomError as e:
            print(f"请求失败: {endpoint} -> {e}")

if __name__ == "__main__":
    main()

# 练习题
"""
异常处理练习题：

1. 基础练习：
   - 编写一个安全的数字输入函数，处理各种输入异常
   - 创建一个文件读取函数，优雅处理文件不存在、权限不足等异常

2. 进阶练习：
   - 设计一个银行账户类，处理余额不足、无效操作等业务异常
   - 创建一个配置文件解析器，处理格式错误、字段缺失等异常

3. 实战练习：
   - 模拟fintern项目中的API调用，处理网络异常、响应异常等
   - 实现一个日志记录系统，优雅处理文件写入异常

4. 高级练习：
   - 设计异常处理策略：何时捕获、何时重抛、何时忽略
   - 研究Python内置异常层次结构
   - 学习使用logging模块记录异常信息
"""