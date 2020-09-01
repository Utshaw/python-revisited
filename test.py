
class Shape:
    def what_am_i(self):
        print("I am a shape")


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


class Square():
    square_list = [] # class variable


    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)
    
    def calculate_perimeter(self):
        return self.s1 * 4

    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)


class Person:
    def __init__(self):
        self.name = "Utshaw"

utshaw = Person()
farhan = utshaw
print(farhan is utshaw) # True

newPerson = Person()
print(newPerson is utshaw) # False

sq = Square(10)
print(Square.square_list)
# rc = Rectangle(10, 20)

# print(rc)
# sq.what_am_i()
# rc.what_am_i()
