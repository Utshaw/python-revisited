#!/usr/bin/env python3

class Math:

    @staticmethod
    def add_five(x):
        return x + 5

print(Math.add_five(100))


class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1
        
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print('I dont know what I say')
    
class Fish(Pet):
    pass

class Dog(Pet): # inheriting upper level class Pet
    def speak(self):
        print('Bark')
    
class Cat(Pet): # inheriting upper level class Pet

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old & I'm of {self.color} color.")

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def set_grade(self):
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)




s1=  Student('Farhan', 18, 95)
s2 = Student('Tanvir', 19, 75)
s3 = Student('Utshaw', 19, 65)
course = Course("Science", 2)

course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())

p = Pet('Tim', 18)
c = Cat('Bill', 34, 'Brown')
c.show()
c.speak()
f = Fish('KUKU', 100)
f.speak()
p1 = Person('Farhan')
p2 = Person('Utshaw')
print(Person.get_number_of_people())