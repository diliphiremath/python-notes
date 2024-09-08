# class method
# Example 1
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    
    @classmethod
    def extract_from_string(cls, book_str):
        name, author = book_str.split(" by ")
        return cls(name, author) #cls refers to actual class i.e Book in this example

# Example 2 
class Counter:
    count = 0

    def __init__(self):
        Counter.increase_count()
    
    @classmethod
    def increase_count(cls):
        cls.count += 1
    
    @classmethod
    def display_count(cls):
        print(cls.count)

# static method
class Person:
    def __init__(self, name, age):
        if not self.validate_age(age):
            raise ValueError("Invalid age")
        self.age = age
        self.name = name
    
    @staticmethod
    def validate_age(age):
        return 0 < age < 150


    
# Example 1
book1 = Book("Clean coder","Dilip")
print(book1.name)
print(book1.author)

book2 = Book.extract_from_string("Programmer by Dane")
print(book2.name)
print(book2.author)

# Example 2
counter1 = Counter()
counter2 = Counter()

Counter.display_count()

# static method
person1 = Person("Dilip",160)