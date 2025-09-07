# 装饰器学习素材和练习

import time
import functools
from datetime import datetime

# 1. 简单装饰器基础
def simple_decorator(func):
    """最简单的装饰器"""
    def wrapper():
        print("函数执行前")
        result = func()
        print("函数执行后")
        return result
    return wrapper

@simple_decorator
def say_hello():
    print("Hello, World!")

# 2. 带参数的装饰器
def timer(func):
    """计时装饰器"""
    @functools.wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行耗时: {end_time - start_time:.4f}秒")
        return result
    return wrapper

@timer
def slow_function():
    """模拟耗时函数"""
    time.sleep(1)
    return "执行完成"

# 3. 日志装饰器
def logger(func):
    """日志装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] 调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"返回结果: {result}")
            return result
        except Exception as e:
            print(f"函数执行出错: {e}")
            raise
    return wrapper

@logger
def calculate_sum(a, b):
    return a + b

# 4. 带参数的装饰器
def retry(max_attempts=3):
    """重试装饰器 - 装饰器本身带参数"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"第{attempt + 1}次尝试失败: {e}")
                    if attempt == max_attempts - 1:
                        print("达到最大重试次数，放弃执行")
                        raise
                    time.sleep(0.5)
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    """模拟不稳定的函数"""
    import random
    if random.random() < 0.7:  # 70%的概率失败
        raise Exception("随机失败")
    return "成功执行"

# 5. 类装饰器
class CountCalls:
    """统计函数调用次数的类装饰器"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 被调用第 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Hello, {name}!"

# 6. 缓存装饰器
def memoize(func):
    """缓存装饰器 - 记忆化"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = str(args) + str(sorted(kwargs.items()))
        
        if key in cache:
            print(f"从缓存获取 {func.__name__} 的结果")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"缓存 {func.__name__} 的结果")
        return result
    
    return wrapper

@memoize
def fibonacci(n):
    """斐波那契数列（递归版本）"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 7. 权限检查装饰器
def require_permission(permission):
    """权限检查装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 这里假设第一个参数是用户对象
            user = args[0] if args else None
            if user and hasattr(user, 'permissions') and permission in user.permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"需要权限: {permission}")
        return wrapper
    return decorator

class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

@require_permission("admin")
def delete_user(user, target_user_id):
    return f"{user.name} 删除了用户 {target_user_id}"

# 8. 多个装饰器组合
@timer
@logger
@retry(max_attempts=2)
def complex_function(x, y):
    """组合多个装饰器的函数"""
    if x < 0:
        raise ValueError("x不能为负数")
    return x ** y

# 练习和测试
if __name__ == "__main__":
    print("=== 装饰器练习 ===")
    
    # 练习1：基础装饰器
    print("\n1. 简单装饰器:")
    say_hello()
    
    # 练习2：计时装饰器
    print("\n2. 计时装饰器:")
    result = slow_function()
    
    # 练习3：日志装饰器
    print("\n3. 日志装饰器:")
    calculate_sum(10, 20)
    
    # 练习4：重试装饰器
    print("\n4. 重试装饰器:")
    try:
        unreliable_function()
    except:
        print("最终失败")
    
    # 练习5：类装饰器
    print("\n5. 类装饰器:")
    greet("Alice")
    greet("Bob")
    
    # 练习6：缓存装饰器
    print("\n6. 缓存装饰器:")
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(10) = {fibonacci(10)}")  # 第二次调用会使用缓存
    
    # 练习7：权限装饰器
    print("\n7. 权限装饰器:")
    admin_user = User("Admin", ["admin", "read", "write"])
    normal_user = User("User", ["read"])
    
    try:
        print(delete_user(admin_user, "user123"))
    except PermissionError as e:
        print(f"权限错误: {e}")
    
    # 练习8：多装饰器组合
    print("\n8. 多装饰器组合:")
    try:
        result = complex_function(2, 3)
        print(f"结果: {result}")
    except Exception as e:
        print(f"执行失败: {e}")

# 进阶练习题
"""
练习题：
1. 创建一个装饰器，限制函数的调用频率（例如每秒最多调用5次）
2. 创建一个装饰器，将函数的返回值转换为JSON格式
3. 创建一个装饰器，自动处理函数的异常并返回默认值
4. 创建一个装饰器，记录函数的执行时间到文件中
5. 研究 functools.lru_cache 装饰器的用法
"""