from Board import *
from Chess import *

class Game:

    def __init__ (self,chess,board):
        self.chess = chess
        self.board = board

    def start_game(self):
        self.chess.board.bind("<Button-1>", self.click_handler)

    def click_handler(self,event):
        current_pos_x = self.chess.size_to_x_coordinates(event.x)
        current_pos_y = self.chess.size_to_y_coordinates(event.y)
        if(self.board.contains_pice(current_pos_x,current_pos_y) and not self.board.contains_possible_move(current_pos_x,current_pos_y)):
            self.board=self.board.board[current_pos_y][current_pos_x]["p"].display_moves(current_pos_x,current_pos_y,self.board)
            self.chess.display_pices(self.board)
        elif(not self.board.contains_pice(current_pos_x,current_pos_y) and self.board.contains_possible_move(current_pos_x,current_pos_y)):
            self.move_pice(current_pos_x,current_pos_y)
        elif(not self.board.contains_pice(current_pos_x,current_pos_y) and not self.board.contains_possible_move(current_pos_x,current_pos_y)):
            self.reset_board()
        else:
            self.board.board[current_pos_y][current_pos_x]['p'].alive=False
            self.move_pice(current_pos_x,current_pos_y)

    def move_pice(self, posX, posY):
        pos=self.board.board[posY][posX]["m"]
        if self.board.board[pos[0]][pos[1]]["p"].is_pawn():
            if self.board.board[pos[0]][pos[1]]["p"].init_pos:
                self.board.board[pos[0]][pos[1]]["p"].init_pos=False
        self.board.board[posY][posX]["p"]=self.board.board[pos[0]][pos[1]]["p"]
        self.board.board[pos[0]][pos[1]]["p"]=""
        self.reset_board()
    
    def reset_board(self):
        self.clean_moves()
        self.chess.create_board()
        self.chess.display_pices(self.board)
    
    def clean_moves(self):
        for row in self.board.board:
            for cell in row:
                if cell["m"] != "":
                    cell["m"] = ""