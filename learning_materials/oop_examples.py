# 面向对象编程学习素材和练习

# 1. 基础类和对象
class Person:
    """人员基础类"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我叫{self.name}，今年{self.age}岁"
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name}过生日了！现在{self.age}岁")

# 2. 继承示例
class Employee(Person):
    """员工类，继承自Person"""
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age)  # 调用父类构造函数
        self.employee_id = employee_id
        self.department = department
        self.projects = []
    
    def add_project(self, project_name):
        self.projects.append(project_name)
    
    def get_work_info(self):
        return f"员工{self.name}，工号{self.employee_id}，部门{self.department}"

class Developer(Employee):
    """开发者类，继承自Employee"""
    def __init__(self, name, age, employee_id, department, programming_languages):
        super().__init__(name, age, employee_id, department)
        self.programming_languages = programming_languages
    
    def write_code(self, language):
        if language in self.programming_languages:
            return f"{self.name}正在用{language}编程"
        else:
            return f"{self.name}不会{language}编程语言"

# 3. 封装示例（私有属性和方法）
class BankAccount:
    """银行账户类 - 展示封装概念"""
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # 私有属性
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"存款{amount}元成功，余额：{self.__balance}元"
        return "存款金额必须大于0"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"取款{amount}元成功，余额：{self.__balance}元"
        return "取款失败：金额不足或无效"
    
    def get_balance(self):
        return self.__balance
    
    def __validate_transaction(self, amount):
        """私有方法"""
        return amount > 0

# 4. 多态示例
class Animal:
    """动物基类"""
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "汪汪"

class Cat(Animal):
    def make_sound(self):
        return "喵喵"

class Bird(Animal):
    def make_sound(self):
        return "啾啾"

def animal_concert(animals):
    """多态演示：不同动物发出不同声音"""
    for animal in animals:
        print(f"{animal.__class__.__name__}: {animal.make_sound()}")

# 5. 特殊方法（魔术方法）
class Book:
    """书籍类 - 展示特殊方法"""
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        """字符串表示"""
        return f"《{self.title}》 - {self.author}"
    
    def __repr__(self):
        """开发者友好的字符串表示"""
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self):
        """返回页数"""
        return self.pages
    
    def __eq__(self, other):
        """比较两本书是否相同"""
        if isinstance(other, Book):
            return (self.title == other.title and 
                   self.author == other.author)
        return False

# 练习题
if __name__ == "__main__":
    print("=== 面向对象编程练习 ===")
    
    # 练习1：创建对象并调用方法
    person = Person("张三", 25)
    print(person.introduce())
    
    # 练习2：继承
    dev = Developer("李四", 28, "DEV001", "技术部", ["Python", "Java"])
    print(dev.get_work_info())
    print(dev.write_code("Python"))
    
    # 练习3：封装
    account = BankAccount("123456", 1000)
    print(account.deposit(500))
    print(account.withdraw(200))
    
    # 练习4：多态
    animals = [Dog(), Cat(), Bird()]
    animal_concert(animals)
    
    # 练习5：特殊方法
    book1 = Book("Python编程", "张作者", 300)
    book2 = Book("Python编程", "张作者", 300)
    print(f"书籍信息: {book1}")
    print(f"书籍页数: {len(book1)}")
    print(f"两本书相同吗: {book1 == book2}")