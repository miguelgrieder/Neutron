

import tkinter as tk
from tkinter.constants import OFF
from default_map import show_default_map

from renderer import Renderer, piece_size,offset


from piece_generator import DirectPieceGenerator, StorePieceGenerator

def main():

    width = 640
    height = 640
    bg = '#6e7482'

    ws = tk.Tk()
    ws.title('Mahjong')
    ws.geometry(f'{width}x{height}')
    ws.config(bg=bg)

    canvas = tk.Canvas(
        ws,
        height=height,
        width=width,
        bg=bg,
        )
        
    canvas.pack()

    renderer = Renderer(canvas)

    generator = StorePieceGenerator()

    show_default_map(generator)

    generator.render_pieces(renderer)

    sorted_pieces = sorted(generator.pieces, key= lambda x: x.floor, reverse=True)

    def on_click(event):

        for piece in sorted_pieces:

            rect = (
                piece.col * piece_size.width + piece.floor * offset,
                piece.row * piece_size.height - piece.floor * offset,
                piece_size.width,
                piece_size.height
            )

            if pointInRect((event.x, event.y), rect):
                print('piece: ', (piece.row, piece.col, piece.floor))
                piece.is_focused = True
                generator.render_pieces(renderer)
                break

    def pointInRect(point,rect):
        x1, y1, w, h = rect
        x2, y2 = x1+w, y1+h
        x, y = point
        if (x1 < x and x < x2):
            if (y1 < y and y < y2):
                return True
        return False



    canvas.bind("<Button-1>", on_click)

    ws.mainloop()









if __name__ == '__main__':
    main()
