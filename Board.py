from tkinter import *
from Pice import Pice
from Tower import Tower
from Bishop import Bishop
from Pawn import Pawn
from King import King
from Queen import Queen
from Horse import Horse
from Move import Move

class Board:

    def __init__(self):
        self.board=[
            [{"p":Tower("tower","black",PhotoImage(file="./img/black_t.png"),True,0,0),"m":""},{"p":Horse("horse","black",PhotoImage(file="./img/black_h.png"),True,0,1),"m":""},{"p":Bishop("bishop","black",PhotoImage(file="./img/black_b.png"),True,0,2),"m":""},{"p":Queen("queen", "black",PhotoImage(file="./img/black_q.png"),True,0,3),"m":""},{"p":King("king","black",PhotoImage(file="./img/black_k.png"),True,0,4),"m":""},{"p":Bishop("bishop","black",PhotoImage(file="./img/black_b.png"),True,0,5),"m":""},{"p":Horse("horse","black",PhotoImage(file="./img/black_h.png"),True,0,6),"m":""},{"p":Tower("tower","black",PhotoImage(file="./img/black_t.png"),True,0,7),"m":""}],
            [{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,0),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,1),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,2),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,3),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,4),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,5),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,6),"m":""},{"p":Pawn("pawn","black",PhotoImage(file="./img/black_p.png"),True,1,7),"m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""},{"p":"","m":""}],
            [{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,0),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,1),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,2),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,3),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,4),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,5),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,6),"m":""},{"p":Pawn("pawn","white",PhotoImage(file="./img/white_p.png"),True,6,7),"m":""}],
            [{"p":Tower("tower","white",PhotoImage(file="./img/white_t.png"),True,7,0),"m":""},{"p":Horse("horse","white",PhotoImage(file="./img/white_h.png"),True,7,1),"m":""},{"p":Bishop("bishop","white",PhotoImage(file="./img/white_b.png"),True,7,2),"m":""},{"p":King("king","white",PhotoImage(file="./img/white_k.png"),True,7,3),"m":""},{"p":Queen("queen", "white",PhotoImage(file="./img/white_q.png"),True,7,4),"m":""},{"p":Bishop("bishop","white",PhotoImage(file="./img/white_b.png"),True,7,5),"m":""},{"p":Horse("horse","white",PhotoImage(file="./img/white_h.png"),True,7,6),"m":""},{"p":Tower("tower","white",PhotoImage(file="./img/white_t.png"),True,7,7),"m":""}]
        ]
        self.black_king_alive=True
        self.white_king_alive=True

    def containsPlayerPice(self, posX, posY, turn):
        return self.board[posY][posX]['p'] != '' and self.board[posY][posX]['p'].side == turn.side

    def isMoveCell(self,posX,posY):
        return self.board[posY][posX]['m'] != ''
    
    def actualizeMoves(self, posX, posY):
        moves = self.board[posY][posX]['p'].get_possible_moves(self.board)
        for move in moves:
            self.board[move.destination[1]][move.destination[0]]['m'] = move
            
    def movePice(self, posX, posY):
        move = self.board[posY][posX]['m']
        self.move_to_destination(posX ,posY, move)
        self.check_init_pos(posX, posY, move)
        

    def move_to_destination(self, posX, posY, move):
        self.board[move.destination[1]][move.destination[0]]['p'] = self.board[move.origin[1]][move.origin[0]]['p']
        self.board[move.destination[1]][move.destination[0]]['p'].posX=move.destination[0]
        self.board[move.destination[1]][move.destination[0]]['p'].posY=move.destination[1]
        self.board[move.origin[1]][move.origin[0]]['p'] = ''

    def check_init_pos(self, posX, posY, move):
        if self.board[move.destination[1]][move.destination[0]]['p'].init_pos:
            self.board[move.destination[1]][move.destination[0]]['p'].init_pos = False