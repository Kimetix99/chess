from Pice import Pice

class Pawn(Pice):
    
    def __init__(self, id, side, figure, alive, posY, posX):
        super(Pawn, self).__init__(id, side, figure, alive, posY, posX)
        self.init_pos=True

    def get_possible_moves(board):
        moves=[]
        self.move_forward(moves, board)

    def move_forward(moves, board)
        pass