from Pice import Pice

class Queen(Pice):
    
    def __init__(self, id, side, figure, posX, posY, alive):
        super(Queen, self).__init__(id, side, figure, posX, posY, alive)