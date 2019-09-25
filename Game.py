class Game:

    def __init__ (self,chess):
        self.chess = chess

    def start_game(self):
        self.chess.board.bind("<Button-1>", self.click_handler)

    def click_handler(self,event):
        current_pos_x = self.chess.size_to_x_coordinates(event.x)
        current_pos_y = self.chess.size_to_y_coordinates(event.y)
        print(current_pos_x)
        print(current_pos_y)

