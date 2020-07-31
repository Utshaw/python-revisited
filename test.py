#!/usr/bin/env python3

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print('Bark')
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age 


    def set_age(self, age):
        this.age = age

    def set_name(self, name):
        self.name = name

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