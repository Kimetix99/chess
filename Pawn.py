from Pice import Pice

class Pawn(Pice):
    
    def __init__(self, id, side, figure, alive):
        super(Pawn, self).__init__(id, side, figure, alive)
        self.init_pos=True

    def display_moves(self,posX,posY):
        if(self.side=='black'):
            if(self.init_pos):
                return [[posX,posY+1],[posX,posY+2]]
            else:
                return [[posX,posY+1]]
        else:
            if(self.init_pos):
                return [[posX,posY-1],[posX,posY-2]]
            else:
                return [[posX,posY-1]]