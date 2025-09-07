# 字典和列表操作学习素材和练习

import json
import copy
from collections import defaultdict, Counter, OrderedDict
from operator import itemgetter

# ==================== 列表操作 ====================

def list_operations_basic():
    """基础列表操作"""
    print("=== 基础列表操作 ===")
    
    # 1. 创建列表
    numbers = [1, 2, 3, 4, 5]
    fruits = ["apple", "banana", "orange"]
    mixed = [1, "hello", 3.14, True]
    
    # 2. 列表索引和切片
    print(f"第一个元素: {numbers[0]}")
    print(f"最后一个元素: {numbers[-1]}")
    print(f"前三个元素: {numbers[:3]}")
    print(f"后两个元素: {numbers[-2:]}")
    print(f"步长为2: {numbers[::2]}")
    
    # 3. 添加元素
    fruits.append("grape")              # 末尾添加
    fruits.insert(1, "watermelon")      # 指定位置插入
    fruits.extend(["mango", "kiwi"])    # 扩展列表
    print(f"添加后的水果: {fruits}")
    
    # 4. 删除元素
    fruits.remove("banana")             # 删除指定值
    popped = fruits.pop()               # 删除并返回最后一个
    del fruits[0]                       # 删除指定索引
    print(f"删除操作后: {fruits}, 弹出的元素: {popped}")
    
    # 5. 查找和统计
    if "apple" in fruits:
        index = fruits.index("apple")
        print(f"apple的索引: {index}")
    
    count = fruits.count("apple")
    print(f"apple出现次数: {count}")

def list_operations_advanced():
    """高级列表操作"""
    print("\n=== 高级列表操作 ===")
    
    # 1. 列表推导式
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 基础推导式
    squares = [x**2 for x in numbers]
    evens = [x for x in numbers if x % 2 == 0]
    
    # 带条件的推导式
    processed = [x*2 if x > 5 else x for x in numbers]
    
    print(f"平方数: {squares}")
    print(f"偶数: {evens}")
    print(f"条件处理: {processed}")
    
    # 2. 嵌套列表推导式
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for row in matrix for item in row]
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    print(f"原矩阵: {matrix}")
    print(f"展平: {flattened}")
    print(f"转置: {transposed}")
    
    # 3. 排序操作
    students = [
        {"name": "Alice", "age": 20, "grade": 85},
        {"name": "Bob", "age": 19, "grade": 92},
        {"name": "Charlie", "age": 21, "grade": 78}
    ]
    
    # 多种排序方式
    by_age = sorted(students, key=lambda x: x["age"])
    by_grade_desc = sorted(students, key=itemgetter("grade"), reverse=True)
    
    print(f"按年龄排序: {by_age}")
    print(f"按成绩降序: {by_grade_desc}")
    
    # 4. 列表的其他高级操作
    # zip组合
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    combined = list(zip(names, scores))
    print(f"组合结果: {combined}")
    
    # enumerate枚举
    for index, fruit in enumerate(["apple", "banana", "orange"], 1):
        print(f"{index}. {fruit}")

def list_performance_tips():
    """列表性能优化技巧"""
    print("\n=== 列表性能技巧 ===")
    
    # 1. 列表vs生成器
    import sys
    
    # 列表（占用更多内存）
    list_comp = [x**2 for x in range(1000)]
    # 生成器（惰性求值，节省内存）
    gen_exp = (x**2 for x in range(1000))
    
    print(f"列表大小: {sys.getsizeof(list_comp)} bytes")
    print(f"生成器大小: {sys.getsizeof(gen_exp)} bytes")
    
    # 2. 预分配vs动态增长
    # 好的做法：预知大小时预分配
    known_size_list = [None] * 1000
    
    # 3. 使用deque进行频繁的开头插入/删除
    from collections import deque
    
    # 列表在开头插入很慢
    normal_list = [1, 2, 3, 4, 5]
    # deque在两端操作都很快
    dq = deque([1, 2, 3, 4, 5])
    
    print("使用deque进行两端操作更高效")

# ==================== 字典操作 ====================

def dict_operations_basic():
    """基础字典操作"""
    print("\n=== 基础字典操作 ===")
    
    # 1. 创建字典
    person = {"name": "Alice", "age": 25, "city": "Beijing"}
    empty_dict = {}
    dict_from_keys = dict.fromkeys(["a", "b", "c"], 0)
    
    print(f"person: {person}")
    print(f"从键创建: {dict_from_keys}")
    
    # 2. 访问和修改
    print(f"姓名: {person['name']}")
    print(f"年龄: {person.get('age', '未知')}")
    print(f"职业: {person.get('job', '未知')}")  # 默认值
    
    # 修改和添加
    person['age'] = 26
    person['job'] = 'Engineer'
    
    # 3. 删除操作
    removed_city = person.pop('city', '默认值')
    print(f"删除的城市: {removed_city}")
    
    # 4. 字典方法
    print(f"所有键: {list(person.keys())}")
    print(f"所有值: {list(person.values())}")
    print(f"所有项: {list(person.items())}")

def dict_operations_advanced():
    """高级字典操作"""
    print("\n=== 高级字典操作 ===")
    
    # 1. 字典推导式
    numbers = [1, 2, 3, 4, 5]
    square_dict = {x: x**2 for x in numbers}
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    
    print(f"平方字典: {square_dict}")
    print(f"偶数平方: {even_squares}")
    
    # 2. 嵌套字典操作
    employees = {
        "Alice": {"age": 25, "department": "IT", "salary": 50000},
        "Bob": {"age": 30, "department": "Finance", "salary": 55000},
        "Charlie": {"age": 28, "department": "IT", "salary": 52000}
    }
    
    # 查找IT部门员工
    it_employees = {name: info for name, info in employees.items() 
                   if info["department"] == "IT"}
    print(f"IT部门员工: {it_employees}")
    
    # 计算平均工资
    avg_salary = sum(info["salary"] for info in employees.values()) / len(employees)
    print(f"平均工资: {avg_salary}")
    
    # 3. 字典合并（Python 3.9+）
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    dict3 = {"b": 20, "e": 5}
    
    # 使用 | 操作符合并（Python 3.9+）
    # merged = dict1 | dict2 | dict3
    
    # 兼容旧版本的合并方式
    merged = {**dict1, **dict2, **dict3}
    print(f"合并字典: {merged}")
    
    # 4. setdefault 和 defaultdict
    from collections import defaultdict
    
    # 使用 setdefault
    groups = {}
    data = [("Alice", "IT"), ("Bob", "Finance"), ("Charlie", "IT")]
    
    for name, dept in data:
        groups.setdefault(dept, []).append(name)
    
    print(f"使用setdefault分组: {groups}")
    
    # 使用 defaultdict
    groups2 = defaultdict(list)
    for name, dept in data:
        groups2[dept].append(name)
    
    print(f"使用defaultdict分组: {dict(groups2)}")

def dict_practical_examples():
    """字典实用示例"""
    print("\n=== 字典实用示例 ===")
    
    # 1. 统计词频
    text = "hello world hello python world"
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    
    # 使用Counter更简单
    from collections import Counter
    word_count2 = Counter(text.split())
    
    print(f"词频统计1: {word_count}")
    print(f"词频统计2: {dict(word_count2)}")
    print(f"最常见的2个词: {word_count2.most_common(2)}")
    
    # 2. 配置管理
    config = {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "mydb"
        },
        "cache": {
            "host": "redis-server",
            "port": 6379
        },
        "debug": True
    }
    
    # 安全地获取嵌套值
    def get_nested_value(d, keys, default=None):
        """安全获取嵌套字典的值"""
        for key in keys:
            if isinstance(d, dict) and key in d:
                d = d[key]
            else:
                return default
        return d
    
    db_host = get_nested_value(config, ["database", "host"], "默认主机")
    missing_key = get_nested_value(config, ["nonexistent", "key"], "未找到")
    
    print(f"数据库主机: {db_host}")
    print(f"不存在的键: {missing_key}")
    
    # 3. 数据转换和清洗
    raw_data = [
        {"name": "Alice", "age": "25", "salary": "50000"},
        {"name": "Bob", "age": "30", "salary": "55000"},
        {"name": "Charlie", "age": "invalid", "salary": "52000"}
    ]
    
    def clean_employee_data(data):
        """清洗员工数据"""
        cleaned = []
        for item in data:
            try:
                cleaned_item = {
                    "name": item["name"].strip(),
                    "age": int(item["age"]) if item["age"].isdigit() else None,
                    "salary": float(item["salary"]) if item["salary"].replace(".", "").isdigit() else None
                }
                cleaned.append(cleaned_item)
            except (ValueError, KeyError) as e:
                print(f"数据清洗错误: {item}, 错误: {e}")
                continue
        return cleaned
    
    cleaned_data = clean_employee_data(raw_data)
    print(f"清洗后的数据: {cleaned_data}")

def combined_operations():
    """字典和列表的组合操作"""
    print("\n=== 字典和列表组合操作 ===")
    
    # 1. 分组操作
    students = [
        {"name": "Alice", "grade": "A", "subject": "Math"},
        {"name": "Bob", "grade": "B", "subject": "Math"},
        {"name": "Charlie", "grade": "A", "subject": "Physics"},
        {"name": "David", "grade": "B", "subject": "Physics"},
        {"name": "Eve", "grade": "A", "subject": "Math"}
    ]
    
    # 按科目分组
    by_subject = {}
    for student in students:
        subject = student["subject"]
        if subject not in by_subject:
            by_subject[subject] = []
        by_subject[subject].append(student)
    
    print("按科目分组:")
    for subject, student_list in by_subject.items():
        print(f"  {subject}: {[s['name'] for s in student_list]}")
    
    # 2. 数据聚合
    # 计算每个科目的平均成绩（A=90, B=80, C=70）
    grade_points = {"A": 90, "B": 80, "C": 70}
    
    subject_stats = {}
    for student in students:
        subject = student["subject"]
        grade = student["grade"]
        
        if subject not in subject_stats:
            subject_stats[subject] = {"total": 0, "count": 0}
        
        subject_stats[subject]["total"] += grade_points[grade]
        subject_stats[subject]["count"] += 1
    
    # 计算平均分
    for subject in subject_stats:
        stats = subject_stats[subject]
        stats["average"] = stats["total"] / stats["count"]
    
    print(f"\n各科目统计: {subject_stats}")
    
    # 3. 复杂数据结构操作
    # 处理API响应数据
    api_response = {
        "status": "success",
        "data": {
            "users": [
                {
                    "id": 1,
                    "name": "Alice",
                    "posts": [
                        {"id": 101, "title": "Hello World", "tags": ["greeting", "first"]},
                        {"id": 102, "title": "Python Tips", "tags": ["python", "programming"]}
                    ]
                },
                {
                    "id": 2,
                    "name": "Bob",
                    "posts": [
                        {"id": 201, "title": "Data Science", "tags": ["python", "data", "science"]}
                    ]
                }
            ]
        }
    }
    
    # 提取所有标签并统计
    all_tags = []
    for user in api_response["data"]["users"]:
        for post in user["posts"]:
            all_tags.extend(post["tags"])
    
    tag_count = Counter(all_tags)
    print(f"\n标签统计: {dict(tag_count)}")
    
    # 按用户统计文章数
    user_post_count = {
        user["name"]: len(user["posts"]) 
        for user in api_response["data"]["users"]
    }
    print(f"用户文章数: {user_post_count}")

# 性能和最佳实践
def performance_best_practices():
    """性能和最佳实践"""
    print("\n=== 性能和最佳实践 ===")
    
    # 1. 字典查找 vs 列表查找
    import time
    
    # 大数据集
    large_list = list(range(10000))
    large_dict = {i: f"value_{i}" for i in range(10000)}
    
    # 列表查找（慢）
    start_time = time.time()
    result = 9999 in large_list
    list_time = time.time() - start_time
    
    # 字典查找（快）
    start_time = time.time()
    result = 9999 in large_dict
    dict_time = time.time() - start_time
    
    print(f"列表查找时间: {list_time:.6f}秒")
    print(f"字典查找时间: {dict_time:.6f}秒")
    print(f"字典比列表快 {list_time/dict_time:.2f} 倍")
    
    # 2. 内存使用优化
    # 使用 __slots__ 减少内存使用
    class RegularClass:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    class OptimizedClass:
        __slots__ = ['x', 'y']
        def __init__(self, x, y):
            self.x = x
            self.y = y
    
    print("\n使用__slots__可以减少内存使用")
    
    # 3. 字典键的选择
    # 使用不可变对象作为键
    good_keys = {
        "string_key": "value1",
        42: "value2",
        (1, 2): "tuple_key",
        frozenset([1, 2, 3]): "frozenset_key"
    }
    
    print("好的字典键类型: 字符串、数字、元组、frozenset")

# 实战练习
def practical_exercises():
    """实战练习"""
    print("\n=== 实战练习 ===")
    
    # 练习1：学生成绩管理系统
    def grade_management_system():
        """成绩管理系统"""
        students = {}
        
        def add_student(name, subjects_grades):
            students[name] = subjects_grades
        
        def get_student_average(name):
            if name in students:
                grades = list(students[name].values())
                return sum(grades) / len(grades) if grades else 0
            return None
        
        def get_subject_average(subject):
            total = 0
            count = 0
            for student_grades in students.values():
                if subject in student_grades:
                    total += student_grades[subject]
                    count += 1
            return total / count if count > 0 else None
        
        def get_top_students(n=3):
            averages = [(name, get_student_average(name)) for name in students]
            return sorted(averages, key=lambda x: x[1], reverse=True)[:n]
        
        # 测试数据
        add_student("Alice", {"Math": 90, "Physics": 85, "Chemistry": 88})
        add_student("Bob", {"Math": 78, "Physics": 92, "Chemistry": 80})
        add_student("Charlie", {"Math": 95, "Physics": 89, "Chemistry": 91})
        
        print("=== 成绩管理系统 ===")
        print(f"Alice的平均分: {get_student_average('Alice'):.2f}")
        print(f"Math科目平均分: {get_subject_average('Math'):.2f}")
        print(f"前3名学生: {get_top_students(3)}")
    
    grade_management_system()
    
    # 练习2：日志分析
    def log_analysis():
        """日志分析示例"""
        # 模拟日志数据
        logs = [
            "2024-01-01 10:00:01 INFO User login: alice",
            "2024-01-01 10:01:15 ERROR Database connection failed",
            "2024-01-01 10:02:30 INFO User login: bob",
            "2024-01-01 10:03:45 WARNING Slow query detected",
            "2024-01-01 10:04:20 ERROR Database connection failed",
            "2024-01-01 10:05:10 INFO User logout: alice"
        ]
        
        # 分析日志
        log_levels = Counter()
        error_messages = []
        user_activities = defaultdict(list)
        
        for log in logs:
            parts = log.split(" ", 3)
            if len(parts) >= 4:
                date, time, level, message = parts
                
                log_levels[level] += 1
                
                if level == "ERROR":
                    error_messages.append(message)
                
                if "User" in message:
                    if "login:" in message:
                        user = message.split("login: ")[1]
                        user_activities[user].append(f"{time} login")
                    elif "logout:" in message:
                        user = message.split("logout: ")[1]
                        user_activities[user].append(f"{time} logout")
        
        print("\n=== 日志分析结果 ===")
        print(f"日志级别统计: {dict(log_levels)}")
        print(f"错误消息: {error_messages}")
        print(f"用户活动: {dict(user_activities)}")
    
    log_analysis()

# 主函数
def main():
    """主函数"""
    print("Python 字典和列表操作学习")
    
    # 列表操作
    list_operations_basic()
    list_operations_advanced()
    list_performance_tips()
    
    # 字典操作
    dict_operations_basic()
    dict_operations_advanced()
    dict_practical_examples()
    
    # 组合操作
    combined_operations()
    
    # 性能和最佳实践
    performance_best_practices()
    
    # 实战练习
    practical_exercises()

if __name__ == "__main__":
    main()

# 额外练习题
"""
练习题建议：

1. 基础练习：
   - 实现一个通讯录程序（使用字典存储联系人信息）
   - 编写函数处理嵌套列表的扁平化
   - 实现列表的去重，保持原始顺序

2. 进阶练习：
   - 实现一个简单的缓存系统（LRU Cache）
   - 编写数据分组和聚合函数
   - 实现配置文件的解析和验证

3. 实战练习：
   - 分析fintern项目中的数据结构使用
   - 处理API响应的复杂JSON数据
   - 实现数据的清洗和转换管道

4. 性能优化：
   - 比较不同数据结构的性能
   - 学习collections模块的各种数据结构
   - 研究内存优化技巧
"""