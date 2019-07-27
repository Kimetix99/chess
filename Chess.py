from tkinter import *
from turtle import *
from Pice import Pice
from Tower import Tower
from Bishop import Bishop
from Pawn import Pawn
from King import King
from Queen import Queen
from Horse import Horse

class Chess:

    def __init__(self,window):
        self.window=window
        self.BOARD_HEIGHT=480
        self.BOARD_WIDTH=480
        self.NUM_X_CELLS=8
        self.NUM_Y_CELLS=8
        self.board=Canvas(window, height=self.BOARD_HEIGHT, width=self.BOARD_WIDTH)

    #Create the board
    def create_board(self):
        
        cell_height=self.BOARD_HEIGHT/self.NUM_Y_CELLS
        cell_width=self.BOARD_WIDTH/self.NUM_X_CELLS

        current_height=0
        current_width=0

        for i in range (0,self.NUM_Y_CELLS):
            for j in range (0,self.NUM_X_CELLS):
                if i%2==0:
                    if j%2==0:
                        self.board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#61b0ff")
                    else:
                        self.board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#ff9661")
                else:
                    if j%2==0:
                        self.board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#ff9661")
                    else:
                        self.board.create_rectangle(current_width, current_height, current_width+cell_width, current_height+cell_height, fill="#61b0ff")
                current_width+=cell_width
            current_height+=cell_height
            current_width=0
        self.board.pack()
        
    
    def create_black_pices(self):
        
        return [Tower("black_left_tower","black",PhotoImage(file="./img/black_t.png"),1,8,True),
                Horse("black_left_horse","black",PhotoImage(file="./img/black_h.png"),2,8,True),
                Bishop("black_left_bishop","black",PhotoImage(file="./img/black_b.png"),3,8,True),
                Queen("black_queen", "black",PhotoImage(file="./img/black_q.png"),4,8,True),
                King("black_king","black",PhotoImage(file="./img/black_k.png"),5,8,True),
                Bishop("black_right_bishop","black",PhotoImage(file="./img/black_b.png"),6,8,True),
                Horse("black_right_horse","black",PhotoImage(file="./img/black_h.png"),7,8,True),
                Tower("black_right_tower","black",PhotoImage(file="./img/black_t.png"),8,8,True),
                Pawn("black_pawn_1","black",PhotoImage(file="./img/black_p.png"),1,7,True),
                Pawn("black_pawn_2","black",PhotoImage(file="./img/black_p.png"),2,7,True),
                Pawn("black_pawn_3","black",PhotoImage(file="./img/black_p.png"),3,7,True),
                Pawn("black_pawn_4","black",PhotoImage(file="./img/black_p.png"),4,7,True),
                Pawn("black_pawn_5","black",PhotoImage(file="./img/black_p.png"),5,7,True),
                Pawn("black_pawn_6","black",PhotoImage(file="./img/black_p.png"),6,7,True),
                Pawn("black_pawn_7","black",PhotoImage(file="./img/black_p.png"),7,7,True),
                Pawn("black_pawn_8","black",PhotoImage(file="./img/black_p.png"),8,7,True)]

    def create_white_pices(self):
        
        return [Tower("white_left_tower","white",PhotoImage(file="./img/white_t.png"),1,1,True),
                Horse("white_left_horse","white",PhotoImage(file="./img/white_h.png"),2,1,True),
                Bishop("white_left_bishop","white",PhotoImage(file="./img/white_b.png"),3,1,True),
                King("white_king","white",PhotoImage(file="./img/white_k.png"),4,1,True),
                Queen("white_queen", "white",PhotoImage(file="./img/white_q.png"),5,1,True),
                Bishop("white_right_bishop","white",PhotoImage(file="./img/white_b.png"),6,1,True),
                Horse("white_right_horse","white",PhotoImage(file="./img/white_h.png"),7,1,True),
                Tower("white_right_tower","white",PhotoImage(file="./img/white_t.png"),8,1,True),
                Pawn("white_pawn_1","white",PhotoImage(file="./img/white_p.png"),1,2,True),
                Pawn("white_pawn_2","white",PhotoImage(file="./img/white_p.png"),2,2,True),
                Pawn("white_pawn_3","white",PhotoImage(file="./img/white_p.png"),3,2,True),
                Pawn("white_pawn_4","white",PhotoImage(file="./img/white_p.png"),4,2,True),
                Pawn("white_pawn_5","white",PhotoImage(file="./img/white_p.png"),5,2,True),
                Pawn("white_pawn_6","white",PhotoImage(file="./img/white_p.png"),6,2,True),
                Pawn("white_pawn_7","white",PhotoImage(file="./img/white_p.png"),7,2,True),
                Pawn("white_pawn_8","white",PhotoImage(file="./img/white_p.png"),8,2,True)]        

    def display_pices(self,white_pices,black_pices):
        for pice in white_pices:
            self.board.create_image(self.x_coordinates_to_size(pice.posX),self.y_coordinates_to_size(pice.posY),image=pice.figure)
            self.board.pack()
        for pice in black_pices:
            self.board.create_image(self.x_coordinates_to_size(pice.posX),self.y_coordinates_to_size(pice.posY),image=pice.figure)
            self.board.pack()
    
    def x_coordinates_to_size(self,x):
        return (x*(self.BOARD_WIDTH/self.NUM_X_CELLS))-((self.BOARD_WIDTH/self.NUM_X_CELLS)/2)
                
    def y_coordinates_to_size(self,y):
        return (y*(self.BOARD_HEIGHT/self.NUM_Y_CELLS))-((self.BOARD_HEIGHT/self.NUM_Y_CELLS)/2)


if __name__ == "__main__":
    window = Tk()
    window.title("Chess")
    chess = Chess(window)
    chess.create_board()
    white_pices=chess.create_white_pices()
    black_pices=chess.create_black_pices()
    chess.display_pices(white_pices,black_pices)
    window.mainloop()

    



