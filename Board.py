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
            [{"p":Tower("tower","black",PhotoImage(file="./img/black_t.png"),True),"m":""},{"p":Horse("horse","black",PhotoImage(file="./img/black_h.png"),True),"m":""},{"p":Bishop("bishop","black",PhotoImage(file="./img/black_b.png"),True),"m":""},{"p":Queen("queen", "black",PhotoImage(file="./img/black_q.png"),True),"m":""},{"p":King("king","black",PhotoImage(file="./img/black_k.png"),True),"m":""},{"p":Bishop("bishop","black",PhotoImage(file="./img/black_b.png"),True),"m":""},{"p":Horse("horse","black",PhotoImage(file="./img/black_h.png"),True),"m":""},{"p":Tower("tower","black",PhotoImage(file="./img/black_t.png"),True),"m":""}],
            [{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True),"m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True),"m":""}],
            [{"p":Tower("tower","white",PhotoImage(file="./img/white_t.png"),True),"m":""},{"p":Horse("horse","white",PhotoImage(file="./img/white_h.png"),True),"m":""},{"p":Bishop("bishop","white",PhotoImage(file="./img/white_b.png"),True),"m":""},{"p":King("king","white",PhotoImage(file="./img/white_k.png"),True),"m":""},{"p":Queen("queen", "white",PhotoImage(file="./img/white_q.png"),True),"m":""},{"p":Bishop("bishop","white",PhotoImage(file="./img/white_b.png"),True),"m":""},{"p":Horse("horse","white",PhotoImage(file="./img/white_h.png"),True),"m":""},{"p":Tower("tower","white",PhotoImage(file="./img/white_t.png"),True),"m":""}]
        ]
        self.black_king_alive=True
        self.white_king_alive=True

    def contains_pice(self,posX,posY):
        return self.board[posY][posX]["p"]!=""

    def contains_possible_move(self, posX, posY):
        return self.board[posY][posX]["m"]!=""
    
    
    
