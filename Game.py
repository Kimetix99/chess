from Board import *
from Chess import *
from Player import *

class Game:

    def __init__ (self,chess,board):
        self.chess = chess
        self.board = board
        self.player1 = Player('1','white')
        self.player2 = Player('2','black')
        self.turn = self.player1

    def start_game(self):
        self.chess.board.bind("<Button-1>", self.click_handler)

    def click_handler(self,event):
        posX = self.chess.size_to_x_coordinates(event.x)
        posY = self.chess.size_to_y_coordinates(event.y)
        if self.containsPlayerPice(posX,posY):
            print('Show me some moves')
        elif self.isMoveCell(posX,posY):
            print('I wana move')
        else:
            print('Yoyo, chill let me alone')
    
    def containsPlayerPice(self,posX,posY):
        return self.board.board[posY][posX]['p'] != '' and self.board.board[posY][posX]['p'].side == self.turn.side

    def isMoveCell(self,posX,posY):
        return self.board.board[posY][posX]['m'] != ''