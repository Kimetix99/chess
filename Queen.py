from Pice import Pice

class Queen(Pice):
    
    def __init__(self, id, side, figure, alive):
        super(Queen, self).__init__(id, side, figure, alive)

    def display_moves(self):
        print('Queen Moves')