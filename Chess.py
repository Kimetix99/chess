from tkinter import *

class Chess:

    def __init__(self,window):
        self.window=window

    def create_board(self):
        
        BOARD_HEIGHT=800
        BOARD_WIDTH=800
        NUM_X_CELLS=8
        NUM_Y_CELLS=8
        
        board=Canvas(window, height=BOARD_HEIGHT, width=BOARD_WIDTH)
        
        cell_height=BOARD_HEIGHT/NUM_Y_CELLS
        cell_width=BOARD_WIDTH/NUM_X_CELLS

        current_height=0
        current_width=0

        for i in range (0,NUM_Y_CELLS):
            for j in range (0,NUM_X_CELLS):
                if i%2==0:
                    if j%2==0:
                        board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#61b0ff")
                    else:
                        board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#ff9661")
                else:
                    if j%2==0:
                        board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#ff9661")
                    else:
                        board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#61b0ff")
                current_width+=cell_width
            current_height+=cell_height
            current_width=0
        board.pack()
        
    def create_pices(self):
        pass


if __name__ == "__main__":
    window = Tk()
    window.title("Chess")
    chess = Chess(window)
    chess.create_board()
    window.mainloop()

