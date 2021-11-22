
from tkinter.constants import NONE
from coordinates import Point, Size

offset = 15

piece_size = Size(40, 70)
#class Renderer(canvas)
class Renderer:

    def __init__(self, canvas):
        self.canvas = canvas
        self.floor = 0


    def render_piece(self, row, col, color = None, with_polygon = True):

        if color is None:
            self.color = '#E8533E'
        else:
            self.color = color


        upleft = Point(col * piece_size.width, row * piece_size.height)

        upleft = upleft.to_up(offset * self.floor).to_right(offset * self.floor)

        downright = upleft.to_down(piece_size.height).to_right(piece_size.width)


        self.canvas.create_rectangle(
            upleft.to_tuple(),
            downright.to_tuple(),
            fill = self.color
            )

        if with_polygon:

            self.render_left_polygon(upleft, piece_size)

            self.render_down_polygon(upleft, piece_size)


    def render_left_polygon(self, rectangle_upleft, piece_size):

        polygon_upleft = rectangle_upleft.to_left(offset).to_down(offset)

        polygon_downleft = polygon_upleft.to_down(piece_size.height)

        polygon_downright = polygon_downleft.to_up(offset).to_right(offset)

        polygon_upright = polygon_downright.to_up(piece_size.height)

        self.canvas.create_polygon(
            polygon_upleft.to_tuple(),
            polygon_downleft.to_tuple(),
            polygon_downright.to_tuple(),
            polygon_upright.to_tuple(),
            fill = self.color,
            outline='#000000'

        )

    def render_down_polygon(self, rectangle_upleft, piece_size):

        polygon_upleft = rectangle_upleft.to_down(piece_size.height)
        
        polygon_downleft = polygon_upleft.to_left(offset).to_down(offset)

        polygon_downright = polygon_downleft.to_right(piece_size.width)

        polygon_upright = polygon_downright.to_right(offset).to_up(offset)

        self.canvas.create_polygon(
            polygon_upleft.to_tuple(),
            polygon_downleft.to_tuple(),
            polygon_downright.to_tuple(),
            polygon_upright.to_tuple(),
            fill = self.color,
            outline='#000000'

        )

