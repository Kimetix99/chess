from Pice import Pice

class Pawn(Pice):
    
    def __init__(self, id, side, figure, alive):
        super(Pawn, self).__init__(id, side, figure, alive)
        self.init_pos=True

    def display_moves(self,posX, posY, board):
                    
        board=self.moves(board, posX, posY)    
        board=self.kill_moves(board, posX, posY)
        
        return board
    
    def kill_moves(self,board,posX,posY):
        if self.side=='black':
            if (posY+1) < len(board.board):         
                if board.board[posY+1][posX-1]['p']!='':
                    board.board[posY+1][posX-1]["m"]=[posY,posX]
                if board.board[posY+1][posX+1]['p']!='':
                    board.board[posY+1][posX+1]["m"]=[posY,posX]
        else:
            if posY-1 >= 0:
                if board.board[posY-1][posX-1]['p']!='':
                    board.board[posY-1][posX-1]["m"]=[posY,posX]
                if board.board[posY-1][posX+1]['p']!='':
                    board.board[posY-1][posX+1]["m"]=[posY,posX]
            
        return board

    def moves(self,board,posX,posY):
        if(self.side=='black'):
            if(self.init_pos):
                if board.board[posY+1][posX]["p"] == "" and board.board[posY+2][posX]["p"] == "":
                    board.board[posY+1][posX]["m"]=[posY,posX]
                    board.board[posY+2][posX]["m"]=[posY,posX]
                if board.board[posY+1][posX]["p"] == "" and board.board[posY+2][posX]["p"] != "":
                    board.board[posY+1][posX]["m"]=[posY,posX]
            else:
                if (posY+1) < len(board.board):
                    if board.board[posY+1][posX]["p"] == "":
                            board.board[posY+1][posX]["m"]=[posY,posX]  
        else:
            if(self.init_pos):
                if board.board[posY-1][posX]["p"] == "" and board.board[posY-2][posX]["p"] == "":
                    board.board[posY-1][posX]["m"]=[posY,posX]
                    board.board[posY-2][posX]["m"]=[posY,posX]
                if board.board[posY-1][posX]["p"] == "" and board.board[posY-2][posX]["p"] != "":
                    board.board[posY-1][posX]["m"]=[posY,posX]
            else:
                if posY-1 >= 0:
                    if board.board[posY-1][posX]["p"] == "":
                            board.board[posY-1][posX]["m"]=[posY,posX]
        return board