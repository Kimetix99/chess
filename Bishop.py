from Pice import Pice

class Bishop(Pice):
    
    def __init__(self, id, side, figure, posX, posY, alive):
        super(Bishop, self).__init__(id, side, figure, posX, posY, alive)