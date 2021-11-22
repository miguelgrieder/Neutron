

import tkinter as tk
import PIL

def render_piece(row, col, canvas: tk.Canvas):

    piece_width = 40
    piece_height = 70

    upleft_x = col * piece_width
    upleft_y = row * piece_height

    downright_x = upleft_x + piece_width
    downright_y = upleft_y + piece_height


    canvas.create_rectangle(
        upleft_x,
        upleft_y,
        downright_x,
        downright_y,
        fill = '#E8533E'
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

    render_piece(0, 0, canvas)
    render_piece(0, 1, canvas)
    render_piece(0, 2, canvas)
    render_piece(0, 3, canvas)

    render_piece(1, 0, canvas)
    render_piece(1, 1, canvas)
    render_piece(1, 2, canvas)
    render_piece(1, 3, canvas)

    ws.mainloop()

if __name__ == '__main__':
    main()
