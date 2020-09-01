# python-revisited
## Classes
- Two types of variables
- Every class inherits from parent class Object
### Class Variables
- Belongs to object and the object's class
### Instance Variable
- Belong to object
```
class Rectangle(Shape):

    recs = [] # class variable

    def __init__(self, width, length):
        self.width = width # instance variable
        self.length = length # instance variable
        self.recs.append((self.width, self.length))

    def calculate_perimeter(self):
        return (self.width + self.length) * 2
    
    def __repr__(self): # magic method
        return "Rectangle(Length: {}, Width: {})".format(self.length, self.width)

```
## is keyword
```

class Person:
    def __init__(self):
        self.name = "Utshaw"

utshaw = Person()
farhan = utshaw
print(farhan is utshaw) # True

newPerson = Person()
print(newPerson is utshaw) # False
```

## Iterables
<img src="3.png">

## Docstring
https://www.datacamp.com/community/tutorials/docstrings-python

## Acknowledgement
https://www.rokomari.com/book/101763/python-porichiti

# Programming Paradign (Style of Programming)
## Procedural Programming
- Instructs a device on how to finish a task in logical steps
- Linear top down approach 
- Treats data and procedures (functions/ routines) in two different entities

## OOP Programming
- Encapsulating data and behaviour into objects.
### Five pillars of OOP
#### Encapsulation
- Objects group variables, which hold state, and methods that alter state
- Hiding a clien't internal data to prevent the client from directly accessing it (Client: Code outside of the class that uses the object)
- Name of variable/method that starts with '_' shouldn't be accessed outside of the class (It is private)
#### Abstraction
- Taking away or removing characteristics from something to reduce it to a set of essential characteristics
#### Polymorphism
- Present the same interface in different data types
#### Inheritance
- Classes can inherit methods and variables from another class
- Class that is inherited from is parent class
- Class that inherits is child class

## Functional Programming
- Passing data from function to function to get result
- Functions are treated as data, you can use them as parameters, return them, build functions from other functions , and build custome functions
- Functions should be pure functions, they should avoid shred state, side effects and data should be immutable
- not dependent on local or global state

## Package Manager
- A program that installs or manages other programs. 
- pip is a package manager for Python
- package is a software meant for distribuion 
- package includes files that make up the actual program, meta data (software name, version number & dependencies)
```
sudo pip3 install Flask==0.12.2
```
