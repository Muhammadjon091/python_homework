import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  

    def area(self):
        return math.pi * self.radius ** 2  

    def perimeter(self):
        return 2 * math.pi * self.radius  

circle1 = Circle(5)
print(circle1.area())       # 78.54
print(circle1.perimeter())  # 31.42



from datetime import date
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  
    def age(self):
        today = date.today()
        birth_year = int(self.dob.split("-")[0])  
        return today.year - birth_year  
name = input("Enter your name: ")
country = input("Enter your country: ")
birth_date = input("Enter your birth date (yyyy-mm-dd): ")
person1 = Person(name, country, birth_date)
print(person1.age())  # Yoshini hisoblaydi



class Calculator:
    def add(self, a, b):
        return a + b  
    def subtract(self, a, b):
        return a - b  
    def multiply(self, a, b):
        return a * b  
    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b  
calc = Calculator()
print(calc.add(10, 5))       # 15
print(calc.divide(10, 2))    # 5.0


import math
class Shape:
    def area(self):
        pass  
    def perimeter(self):
        pass  
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side
circle = Circle(5)
square = Square(4)
print(circle.area())   # 78.54
print(square.area())   # 16


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    def _insert(self, current, value):
        if value < current.value:
            if current.left:
                self._insert(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert(current.right, value)
            else:
                current.right = Node(value)
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, current, value):
        if not current:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search(current.left, value)
        else:
            return self._search(current.right, value)
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print(bst.search(15))  # True
print(bst.search(7))   # False


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty!"
    def is_empty(self):
        return len(self.stack) == 0
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.pop())  # 20
print(stack.pop())  # 10


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  # 30 -> 20 -> 10 -> None


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Mahsulot nomi -> narx
    def add_item(self, name, price):
        if name in self.items:
            self.items[name] += price
        else:
            self.items[name] = price
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} savatchada yo'q!")
    def total_price(self):
        return sum(self.items.values())
    def display_cart(self):
        if not self.items:
            print("Savatcha bo‘sh!")
        else:
            for item, price in self.items.items():
                print(f"{item}: ${price}")
            print(f"Jami narx: ${self.total_price()}")
cart = ShoppingCart()
cart.add_item("Olma", 3)
cart.add_item("Banan", 2)
cart.display_cart()  # Olma: $3, Banan: $2, Jami narx: $5
cart.remove_item("Banan")
cart.display_cart()  # Olma: $3, Jami narx: $3


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack bo‘sh!"
    def is_empty(self):
        return len(self.stack) == 0
    def display(self):
        print("Stack:", self.stack[::-1])
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Stack: [30, 20, 10]
stack.pop()
stack.display()  # Stack: [20, 10]


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue bo‘sh!"
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        print("Queue:", self.queue)
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # Queue: [1, 2, 3]
queue.dequeue()
queue.display()  # Queue: [2, 3]


class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance  
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} hisobingizga qo‘shildi. Joriy balans: ${self.balance}")
        else:
            print("Noto‘g‘ri miqdor!")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount} yechildi. Yangi balans: ${self.balance}")
        else:
            print("Yetarli mablag‘ yo‘q yoki noto‘g‘ri miqdor!")
    def get_balance(self):
        return f"{self.name} hisobidagi balans: ${self.balance}"
# Hisob ochamiz
ali_account = BankAccount("Ali", 100)
ali_account.deposit(50)     # $50 qo‘shildi
ali_account.withdraw(30)    # $30 yechildi
print(ali_account.get_balance())  # Ali hisobidagi balans: $120


