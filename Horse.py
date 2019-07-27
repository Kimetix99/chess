from Pice import Pice

class Horse(Pice):
    
    def __init__(self, id, side, figure, posX, posY, alive):
        super(Horse, self).__init__(id, side, figure, posX, posY, alive)