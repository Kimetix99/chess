from tkinter import *
from Pice import Pice
from Tower import Tower
from Bishop import Bishop
from Pawn import Pawn
from King import King
from Queen import Queen
from Horse import Horse

class Board:

    def __init__(self):
        self.board=[
            [Tower("black_left_tower","black",PhotoImage(file="./img/black_t.png"),True),Horse("black_left_horse","black",PhotoImage(file="./img/black_h.png"),True),Bishop("black_left_bishop","black",PhotoImage(file="./img/black_b.png"),True),Queen("black_queen", "black",PhotoImage(file="./img/black_q.png"),True),King("black_king","black",PhotoImage(file="./img/black_k.png"),True),Bishop("black_right_bishop","black",PhotoImage(file="./img/black_b.png"),True),Horse("black_right_horse","black",PhotoImage(file="./img/black_h.png"),True),Tower("black_right_tower","black",PhotoImage(file="./img/black_t.png"),True)],
            [Pawn("black_pawn_1","black",PhotoImage(file="./img/black_p.png"),True),Pawn("black_pawn_2","black",PhotoImage(file="./img/black_p.png"),True),Pawn("black_pawn_3","black",PhotoImage(file="./img/black_p.png"),True),Pawn("black_pawn_4","black",PhotoImage(file="./img/black_p.png"),True),Pawn("black_pawn_5","black",PhotoImage(file="./img/black_p.png"),True),Pawn("black_pawn_6","black",PhotoImage(file="./img/black_p.png"),True),Pawn("black_pawn_7","black",PhotoImage(file="./img/black_p.png"),True),Pawn("black_pawn_8","black",PhotoImage(file="./img/black_p.png"),True)],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            [Pawn("white_pawn_1","white",PhotoImage(file="./img/white_p.png"),True),Pawn("white_pawn_2","white",PhotoImage(file="./img/white_p.png"),True),Pawn("white_pawn_3","white",PhotoImage(file="./img/white_p.png"),True),Pawn("white_pawn_4","white",PhotoImage(file="./img/white_p.png"),True),Pawn("white_pawn_5","white",PhotoImage(file="./img/white_p.png"),True),Pawn("white_pawn_6","white",PhotoImage(file="./img/white_p.png"),True),Pawn("white_pawn_7","white",PhotoImage(file="./img/white_p.png"),True),Pawn("white_pawn_8","white",PhotoImage(file="./img/white_p.png"),True)],
            [Tower("white_left_tower","white",PhotoImage(file="./img/white_t.png"),True),Horse("white_left_horse","white",PhotoImage(file="./img/white_h.png"),True),Bishop("white_left_bishop","white",PhotoImage(file="./img/white_b.png"),True),King("white_king","white",PhotoImage(file="./img/white_k.png"),True),Queen("white_queen", "white",PhotoImage(file="./img/white_q.png"),True),Bishop("white_right_bishop","white",PhotoImage(file="./img/white_b.png"),True),Horse("white_right_horse","white",PhotoImage(file="./img/white_h.png"),True),Tower("white_right_tower","white",PhotoImage(file="./img/white_t.png"),True)]
        ]
        self.black_king_alive=True
        self.white_king_alive=True

    def contains_pice(self,posX,posY):
        return self.board[posX][posY]!=""
    
    def kings_alive(self):
        return self.black_king_alive and self.white_king_alive