from Pice import Pice

class Pawn(Pice):
    
    def __init__(self, id, side, figure, alive):
        super(Pawn, self).__init__(id, side, figure, alive)
        self.init_pos=True

    def display_moves(self,posX, posY, board):
        if(self.side=='black'):
            if(self.init_pos):
                if board.board[posY+1][posX]["p"] == "" and board.board[posY+2][posX]["p"] == "":
                    board.board[posY+1][posX]["m"]=[posY,posX]
                    board.board[posY+2][posX]["m"]=[posY,posX]
            else:
                if board.board[posY+1][posX]["p"] == "":
                    if posY+1 < len(board.board) and posX < len(board.board[posY]):
                        board.board[posY+1][posX]["m"]=[posY,posX]
        else:
            if(self.init_pos):
                if board.board[posY-1][posX]["p"] == "" and board.board[posY-2][posX]["p"] == "":
                    board.board[posY-1][posX]["m"]=[posY,posX]
                    board.board[posY-2][posX]["m"]=[posY,posX]
            else:
                if board.board[posY-1][posX]["p"] == "":
                    if posY+1 < len(board.board) and posX < len(board.board[posY]):
                        board.board[posY-1][posX]["m"]=[posY,posX]
        return board
    