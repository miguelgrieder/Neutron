#class Point(x,y), class Size(width, height)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_up(self, offset):
        return Point(
            self.x,
            self.y - offset
        )

    def to_down(self, offset):
        return Point(
            self.x,
            self.y + offset
        )

    def to_left(self, offset):
        return Point(
            self.x - offset,
            self.y,
        )

    def to_right(self, offset):
        return Point(
            self.x + offset,
            self.y,
        )


    def to_tuple(self):
        return (self.x , self.y)

    

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height
