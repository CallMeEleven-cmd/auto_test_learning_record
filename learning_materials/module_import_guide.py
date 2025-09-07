# Python模块导入机制学习指南

"""
Python模块导入机制详解

本文件详细介绍Python的模块导入机制，包括：
1. 模块和包的概念
2. 导入语句的各种形式
3. 模块搜索路径
4. 相对导入和绝对导入
5. 循环导入问题
6. 动态导入
7. 最佳实践
"""

import sys
import os
import importlib
import importlib.util
from pathlib import Path

# ==================== 1. 模块导入基础 ====================

def basic_imports():
    """基础导入示例"""
    print("=== 基础导入示例 ===")
    
    # 1. 标准库导入
    import datetime
    import json
    import os.path
    
    # 2. 使用别名导入
    import datetime as dt
    import numpy as np  # 如果安装了numpy
    
    # 3. 从模块导入特定对象
    from datetime import datetime, timedelta
    from os.path import join, exists
    
    # 4. 导入所有（不推荐）
    # from datetime import *  # 不推荐，可能造成命名空间污染
    
    # 使用示例
    now = datetime.now()
    print(f"当前时间: {now}")
    
    tomorrow = now + timedelta(days=1)
    print(f"明天: {tomorrow}")
    
    # 检查文件是否存在
    file_path = join(".", "example.txt")
    print(f"文件 {file_path} 存在: {exists(file_path)}")

def module_search_path():
    """模块搜索路径"""
    print("\n=== 模块搜索路径 ===")
    
    print("Python模块搜索路径:")
    for i, path in enumerate(sys.path, 1):
        print(f"  {i}. {path}")
    
    # 添加自定义路径
    custom_path = r"c:\Users\shiyi3-jk\Desktop\fintern_auto\my_modules"
    if custom_path not in sys.path:
        sys.path.append(custom_path)
        print(f"\n添加自定义路径: {custom_path}")
    
    # 查看特定模块的位置
    modules_to_check = ['os', 'sys', 'json', 'datetime']
    print("\n模块文件位置:")
    for module_name in modules_to_check:
        try:
            module = __import__(module_name)
            location = getattr(module, '__file__', '内置模块')
            print(f"  {module_name}: {location}")
        except ImportError:
            print(f"  {module_name}: 未找到")

# ==================== 2. 包和模块结构 ====================

def demonstrate_package_structure():
    """演示包结构"""
    print("\n=== 包结构示例 ===")
    
    # 创建示例包结构
    package_structure = """
    my_package/
    ├── __init__.py          # 包初始化文件
    ├── module1.py           # 模块1
    ├── module2.py           # 模块2
    └── subpackage/          # 子包
        ├── __init__.py
        ├── submodule1.py
        └── submodule2.py
    """
    
    print("典型的包结构:")
    print(package_structure)
    
    # __init__.py 的作用
    init_py_content = '''
    # __init__.py 文件的作用:
    # 1. 将目录标识为Python包
    # 2. 控制包的导入行为
    # 3. 提供包级别的初始化代码
    
    # 示例 __init__.py 内容:
    from .module1 import function1
    from .module2 import Class2
    
    # 定义 __all__ 控制 from package import * 的行为
    __all__ = ['function1', 'Class2', 'CONSTANT']
    
    # 包级别的常量
    CONSTANT = "包级别常量"
    
    # 包初始化代码
    print("初始化 my_package")
    '''
    
    print("__init__.py 示例:")
    print(init_py_content)

# ==================== 3. 相对导入和绝对导入 ====================

def import_types_explanation():
    """导入类型说明"""
    print("\n=== 绝对导入 vs 相对导入 ===")
    
    absolute_import_example = '''
    # 绝对导入：从项目根目录开始的完整路径
    from my_package.module1 import function1
    from my_package.subpackage.submodule1 import SubClass
    import my_package.module2
    
    # 优点：清晰明确，不依赖当前位置
    # 缺点：路径可能较长
    '''
    
    relative_import_example = '''
    # 相对导入：相对于当前模块的位置
    from .module1 import function1        # 同级目录
    from ..parent_module import something # 上级目录
    from .subpackage.submodule1 import SubClass  # 子目录
    
    # 注意：相对导入只能在包内部使用，不能在脚本中直接执行
    # 优点：便于重构，路径相对简洁
    # 缺点：依赖于当前位置，可能不够清晰
    '''
    
    print("绝对导入示例:")
    print(absolute_import_example)
    print("相对导入示例:")
    print(relative_import_example)
    
    # 导入建议
    import_guidelines = '''
    导入最佳实践：
    
    1. 优先使用绝对导入，更清晰
    2. 包内部模块间可以使用相对导入
    3. 避免深层次的相对导入（超过2级）
    4. 在包的 __init__.py 中使用相对导入组织API
    
    导入顺序建议：
    1. 标准库导入
    2. 第三方库导入  
    3. 本地应用/项目导入
    
    每组之间用空行分隔
    '''
    
    print("导入指导原则:")
    print(import_guidelines)

# ==================== 4. 动态导入 ====================

def dynamic_import_examples():
    """动态导入示例"""
    print("\n=== 动态导入 ===")
    
    # 1. 使用 __import__
    module_name = "json"
    json_module = __import__(module_name)
    data = {"name": "Alice", "age": 25}
    json_str = json_module.dumps(data)
    print(f"使用 __import__ 导入: {json_str}")
    
    # 2. 使用 importlib
    import importlib
    
    # 导入模块
    os_module = importlib.import_module("os")
    current_dir = os_module.getcwd()
    print(f"使用 importlib 导入: 当前目录 {current_dir}")
    
    # 3. 从文件路径导入模块
    def import_from_file(file_path, module_name):
        """从文件路径导入模块"""
        try:
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None:
                return None
            
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module
        except Exception as e:
            print(f"导入失败: {e}")
            return None
    
    # 4. 条件导入
    def conditional_import():
        """条件导入示例"""
        try:
            # 尝试导入可选依赖
            import requests
            print("requests 库可用")
            return requests
        except ImportError:
            print("requests 库不可用，使用替代方案")
            # 使用标准库的 urllib 作为替代
            import urllib.request
            return urllib.request
    
    conditional_import()
    
    # 5. 延迟导入
    def lazy_import_example():
        """延迟导入示例"""
        def get_random_number():
            # 只在需要时才导入
            import random
            return random.randint(1, 100)
        
        return get_random_number()
    
    random_num = lazy_import_example()
    print(f"延迟导入获得随机数: {random_num}")

# ==================== 5. 循环导入问题 ====================

def circular_import_problem():
    """循环导入问题说明"""
    print("\n=== 循环导入问题 ===")
    
    problem_example = '''
    # 循环导入问题示例：
    
    # module_a.py
    from module_b import function_b
    
    def function_a():
        return "A calls " + function_b()
    
    # module_b.py  
    from module_a import function_a  # 这里会产生循环导入
    
    def function_b():
        return "B calls " + function_a()
    '''
    
    solutions = '''
    解决循环导入的方法：
    
    1. 重构代码结构，提取公共依赖
    2. 使用延迟导入（在函数内部导入）
    3. 使用导入语句而不是 from ... import ...
    4. 重新设计模块间的依赖关系
    
    示例解决方案：
    
    # module_a.py
    def function_a():
        import module_b  # 延迟导入
        return "A calls " + module_b.function_b()
    
    # module_b.py
    def function_b():
        return "B"
        
    # 或者提取公共功能到第三个模块
    '''
    
    print("循环导入问题:")
    print(problem_example)
    print("解决方案:")
    print(solutions)

# ==================== 6. 模块缓存和重载 ====================

def module_cache_and_reload():
    """模块缓存和重载"""
    print("\n=== 模块缓存和重载 ===")
    
    print("已加载的模块（部分）:")
    loaded_modules = list(sys.modules.keys())[:10]
    for module in loaded_modules:
        print(f"  - {module}")
    
    print(f"\n总共加载了 {len(sys.modules)} 个模块")
    
    # 模块重载示例
    reload_example = '''
    # 开发过程中重载模块
    
    import importlib
    import my_module
    
    # 修改 my_module.py 后重载
    importlib.reload(my_module)
    
    注意：
    1. reload 只重载模块代码，不重载已创建的对象
    2. 在生产环境中不建议使用重载
    3. 重载不能处理 from ... import ... 的情况
    '''
    
    print("模块重载:")
    print(reload_example)

# ==================== 7. 实际项目中的导入策略 ====================

def fintern_project_import_analysis():
    """分析fintern项目的导入策略"""
    print("\n=== fintern项目导入分析 ===")
    
    fintern_imports_analysis = '''
    在fintern项目中的导入模式分析：
    
    1. 项目结构导入：
       from fin_tools.oversea.fintern.fintern import Business
       - 这是绝对导入，从项目根目录开始
    
    2. 公共工具导入：
       from py_com.qifu_py_com.utils.com_method import RSAUtils, method_io
       - 导入公司内部的公共工具库
    
    3. 第三方库导入：
       import requests
       from openpyxl import load_workbook
       - 标准的第三方库导入
    
    4. 条件导入：
       try:
           import paramiko
       except:
           paramiko = None
       - 处理可选依赖
    
    5. 相对导入：
       from .common import FinternCom, AutoTestReport
       - 包内部使用相对导入
    
    学习要点：
    - 清晰的包结构组织
    - 合理使用绝对导入和相对导入
    - 处理可选依赖的优雅方式
    - 遵循导入顺序规范
    '''
    
    print(fintern_imports_analysis)

# ==================== 8. 最佳实践和常见错误 ====================

def import_best_practices():
    """导入最佳实践"""
    print("\n=== 导入最佳实践 ===")
    
    best_practices = '''
    Python导入最佳实践：
    
    1. 导入顺序：
       - 标准库
       - 相关第三方库
       - 本地应用/库特定导入
    
    2. 导入风格：
       ✅ 好的做法：
       import os
       import sys
       from datetime import datetime
       
       ❌ 避免的做法：
       from datetime import *  # 命名空间污染
       import os, sys  # 一行多个导入
    
    3. 别名使用：
       import pandas as pd  # 约定俗成的别名
       import numpy as np
       
    4. 条件导入：
       try:
           import optional_dependency
       except ImportError:
           optional_dependency = None
    
    5. 延迟导入：
       def heavy_function():
           import expensive_module  # 只在需要时导入
           return expensive_module.do_work()
    
    6. 避免循环导入：
       - 重新设计模块结构
       - 使用延迟导入
       - 提取公共依赖
    '''
    
    common_errors = '''
    常见导入错误：
    
    1. ModuleNotFoundError:
       - 检查模块名拼写
       - 确认模块在Python路径中
       - 检查虚拟环境是否正确
    
    2. ImportError:
       - 模块存在但有语法错误
       - 依赖缺失
    
    3. 循环导入:
       - 使用 import module 而不是 from module import
       - 延迟导入
       - 重构代码结构
    
    4. 相对导入错误:
       - 确保在包内部使用
       - 不能在脚本中直接运行含相对导入的模块
    '''
    
    print(best_practices)
    print(common_errors)

# ==================== 9. 实战练习 ====================

def create_practice_modules():
    """创建练习用的模块文件"""
    print("\n=== 创建练习模块 ===")
    
    # 创建练习目录结构
    practice_dir = Path("c:/Users/shiyi3-jk/Desktop/fintern_auto/learning_materials/practice_package")
    practice_dir.mkdir(exist_ok=True)
    
    # 创建主包的 __init__.py
    init_content = '''# practice_package/__init__.py
"""
练习包 - 演示Python包结构和导入机制
"""

from .math_utils import add, multiply
from .string_utils import reverse_string, capitalize_words

__version__ = "1.0.0"
__all__ = ["add", "multiply", "reverse_string", "capitalize_words"]

print("practice_package 包已初始化")
'''
    
    with open(practice_dir / "__init__.py", "w", encoding="utf-8") as f:
        f.write(init_content)
    
    # 创建 math_utils.py
    math_utils_content = '''# math_utils.py
"""数学工具模块"""

def add(a, b):
    """加法函数"""
    return a + b

def multiply(a, b):
    """乘法函数"""
    return a * b

def divide(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("不能除以零")
    return a / b

# 模块级别常量
PI = 3.14159

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
'''
    
    with open(practice_dir / "math_utils.py", "w", encoding="utf-8") as f:
        f.write(math_utils_content)
    
    # 创建 string_utils.py
    string_utils_content = '''# string_utils.py
"""字符串工具模块"""

def reverse_string(s):
    """反转字符串"""
    return s[::-1]

def capitalize_words(s):
    """首字母大写"""
    return s.title()

def count_words(s):
    """统计单词数"""
    return len(s.split())

# 相对导入示例（从同包的其他模块导入）
def math_and_string_demo():
    from .math_utils import add
    result = add(1, 2)
    return f"Math result: {result}"

if __name__ == "__main__":
    test_str = "hello world python"
    print(f"原字符串: {test_str}")
    print(f"反转: {reverse_string(test_str)}")
    print(f"首字母大写: {capitalize_words(test_str)}")
    print(f"单词数: {count_words(test_str)}")
'''
    
    with open(practice_dir / "string_utils.py", "w", encoding="utf-8") as f:
        f.write(string_utils_content)
    
    print(f"练习模块已创建在: {practice_dir}")

def practice_imports():
    """导入练习"""
    print("\n=== 导入练习 ===")
    
    try:
        # 确保路径在sys.path中
        practice_path = "c:/Users/shiyi3-jk/Desktop/fintern_auto/learning_materials"
        if practice_path not in sys.path:
            sys.path.insert(0, practice_path)
        
        # 1. 导入整个包
        import practice_package
        print("包导入成功")
        
        # 2. 使用包中的函数
        result1 = practice_package.add(10, 20)
        result2 = practice_package.reverse_string("Hello")
        print(f"包函数调用: add(10, 20) = {result1}")
        print(f"包函数调用: reverse_string('Hello') = {result2}")
        
        # 3. 从包中导入特定模块
        from practice_package import math_utils
        result3 = math_utils.multiply(3, 4)
        print(f"模块函数调用: multiply(3, 4) = {result3}")
        
        # 4. 从模块导入特定函数
        from practice_package.string_utils import capitalize_words
        result4 = capitalize_words("python programming")
        print(f"直接函数调用: capitalize_words = {result4}")
        
    except ImportError as e:
        print(f"导入失败: {e}")
        print("请先运行 create_practice_modules() 创建练习模块")

# ==================== 主函数 ====================

def main():
    """主函数"""
    print("Python模块导入机制学习指南")
    print("=" * 50)
    
    # 基础概念
    basic_imports()
    module_search_path()
    demonstrate_package_structure()
    
    # 导入类型
    import_types_explanation()
    
    # 高级话题
    dynamic_import_examples()
    circular_import_problem()
    module_cache_and_reload()
    
    # 实际项目分析
    fintern_project_import_analysis()
    
    # 最佳实践
    import_best_practices()
    
    # 实战练习
    create_practice_modules()
    practice_imports()

if __name__ == "__main__":
    main()

# ==================== 学习建议 ====================

learning_suggestions = '''
Python模块导入学习建议：

1. 理论学习（1-2天）：
   - 理解模块、包的概念
   - 掌握各种导入语法
   - 了解Python的模块搜索机制

2. 实践练习（2-3天）：
   - 创建自己的包和模块
   - 练习不同的导入方式
   - 解决常见的导入问题

3. 项目分析（1-2天）：
   - 分析fintern项目的导入结构
   - 理解大型项目的组织方式
   - 学习最佳实践

4. 深入学习：
   - 研究importlib模块的高级用法
   - 了解Python包管理工具（pip, setuptools）
   - 学习虚拟环境的使用

记住：
- 多动手实践，不要只看理论
- 遇到导入错误时，仔细阅读错误信息
- 养成良好的代码组织习惯
- 关注项目的可维护性和可读性
'''

print(learning_suggestions)