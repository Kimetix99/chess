class Pice:

    def __init__(self,id,side,figure,alive):
        self.id=id
        self.side=side
        self.figure=figure
        self.alive=alive

    def is_pawn(self):
        if self.id=="pawn":
            return True
        else:
            return False
