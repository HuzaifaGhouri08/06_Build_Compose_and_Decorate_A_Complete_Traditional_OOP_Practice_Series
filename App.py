# 1. Using self
# Assignment: Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")



# 2. Using cls
# Assignment: Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def show_count(cls):
        print(f"Objects created: {cls.count}")



# 3. Public Variables and Methods
# Assignment: Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand
    def start(self):
        print(f"{self.brand} is starting...")



# 4. Class Variables and Class Methods
# Assignment: Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Default Bank"
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name



# 5. Static Variables and Static Methods
# Assignment: Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b



# 6. Constructors and Destructors
# Assignment: Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger initialized.")
    def __del__(self):
        print("Logger destroyed.")



# 7. Access Modifiers
# Assignment: Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn



# 8. The super() Function
# Assignment: Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject



# 9. Abstract Classes and Methods
# Assignment: Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height



# 10. Instance Methods
# Assignment: Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says woof!")



# 11. Class Methods
# Assignment: Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1



# 12. Static Methods
# Assignment: Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32



# 13. Composition
# Assignment: Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine started")
class CarWithEngine:
    def __init__(self, engine):
        self.engine = engine
    def start_engine(self):
        self.engine.start()



# 14. Aggregation
# Assignment: Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, employee):
        self.employee = employee



# 15. MRO and Diamond Inheritance
# Assignment: Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("A.show")
class B(A):
    def show(self):
        print("B.show")
class C(A):
    def show(self):
        print("C.show")
class D(B, C):
    pass



# 16. Function Decorators
# Assignment: Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper
@log_function_call
def say_hello():
    print("Hello!")



# 17. Class Decorators
# Assignment: Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls
@add_greeting
class DecoratedPerson:
    pass



# 18. Property Decorators
# Assignment: Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value
    @price.deleter
    def price(self):
        del self._price



# 19. __call__ and callable
# Assignment: Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, value):
        return self.factor * value



# 20. Custom Exception
# Assignment: Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")



# 21. Custom Iterable
# Assignment: Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val
