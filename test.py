
class Shape:
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2


class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1
    
    def calculate_perimeter(self):
        return self.s1 * 4


sq = Square(10)
rc = Rectangle(10, 20)
sq.what_am_i()
rc.what_am_i()
