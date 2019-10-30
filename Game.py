from Board import *

class Game:

    def __init__ (self,chess,board):
        self.chess = chess
        self.board = board

    def start_game(self):
        self.chess.board.bind("<Button-1>", self.click_handler)

    def click_handler(self,event):
        current_pos_x = self.chess.size_to_x_coordinates(event.x)
        current_pos_y = self.chess.size_to_y_coordinates(event.y)
        if(self.board.contains_pice(current_pos_x,current_pos_y)):
            self.display_possible_moves(current_pos_x,current_pos_y)
        
        if(self.board.contains_possible_move(current_pos_x,current_pos_y)):
            pass
        
        if(self.board.contains_nothing(current_pos_x,current_pos_y)):
            pass
        
    def display_possible_moves(self, posX, posY):
        pass

