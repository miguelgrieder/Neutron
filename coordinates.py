
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x , self.y)

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height
