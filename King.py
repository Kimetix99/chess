from Pice import Pice

class King(Pice):
    
    def __init__(self, id, side, figure, posX, posY, alive):
        super(King, self).__init__(id, side, figure, posX, posY, alive)