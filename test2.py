class Square:

    square_list = []
    def __init__(self):
        self.square_list.append(self)
    
    def same(obj1, obj2):
        return obj1 is obj2


