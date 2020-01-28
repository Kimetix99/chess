from Pice import Pice
from Move import Move

class Pawn(Pice):
    
    def __init__(self, id, side, figure, alive, posY, posX):
        super(Pawn, self).__init__(id, side, figure, alive, posY, posX)
        self.init_pos=True

    def get_possible_moves(self, board):
        moves=[]
        self.move_forward(moves, board)
        self.kill_move(moves, board)
        return moves

    def move_forward(self, moves, board):
            if self.init_pos:
                    moves.append(Move((self.posX, self.posY), (self.posX, self.check_side(self.side, self.posY, 2))))
                    moves.append(Move((self.posX, self.posY), (self.posX, self.check_side(self.side, self.posY, 1))))
            else:
                    moves.append(Move((self.posX,self.posY), (self.posX,self.check_side(self.side, self.posY, 1))))

    def kill_move(self, moves, board):
        if self.can_kill_left(board):
            moves.append(Move((self.posX, self.posY), (self.posX-1, self.check_side(self.side, self.posY, 1))))
        if self.can_kill_right(board):
            moves.append(Move((self.posX, self.posY), (self.posX+1, self.check_side(self.side, self.posY, 1))))

    def can_kill_left(self, board):
        return board[self.posX-1][self.check_side(self.side, self.posY,1)]['p'] != ''

    def can_kill_right(self, board):
        return board[self.posX+1][self.check_side(self.side, self.posY,1)]['p'] != ''
    
    def check_side(self, side,pos,value):
        if side == 'black': 
            return pos-value 
        else: 
            return pos+value 
    
       