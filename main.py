

import tkinter as tk

from coordinates import Point, Size


def render_piece(row, col, canvas: tk.Canvas):

    piece_size = Size(40, 70)

    upleft = Point(col * piece_size.width, row * piece_size.height)

    downright = Point(upleft.x + piece_size.width, upleft.y + piece_size.height)


    canvas.create_rectangle(
        upleft.to_tuple(),
        downright.to_tuple(),
        fill = '#E8533E'
        )

    render_left_polygon(canvas, upleft, piece_size)


def render_left_polygon(canvas, rectangle_upleft, piece_size):

    offset = 15

    polygon_upleft = Point(
        rectangle_upleft.x - offset,
         rectangle_upleft.y + offset)

    polygon_downleft = Point(
        polygon_upleft.x,
        polygon_upleft.y + piece_size.height)

    polygon_downright = Point(
        polygon_downleft.x + offset,
         polygon_downleft.y - offset)

    polygon_upright = Point(
        polygon_downright.x,
         polygon_downright.y - piece_size.height)

    canvas.create_polygon(
        polygon_upleft.to_tuple(),
        polygon_downleft.to_tuple(),
        polygon_downright.to_tuple(),
        polygon_upright.to_tuple(),
        fill = '#E8533E',
        outline='#000000'

    )


def main():

    width = 640
    height = 480
    bg = '#6e7482'

    ws = tk.Tk()
    ws.title('PythonGuides')
    ws.geometry(f'{width}x{height}')
    ws.config(bg=bg)

    canvas = tk.Canvas(
        ws,
        height=height,
        width=width,
        bg=bg,
        )
        
    canvas.pack()

    render_piece(1, 1, canvas)

    ws.mainloop()

if __name__ == '__main__':
    main()
