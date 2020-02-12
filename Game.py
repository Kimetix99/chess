#!/usr/bin/python3
#-*- coding:utf-8 -*-
#######################################################################
# Copyright 2020 Joaquim Picó Mora

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#######################################################################

from Board import *
from Chess import *
from Player import *

class Game:

    def __init__ (self,chess,board):
        self.chess = chess
        self.board = board
        self.player1 = Player('1','white')
        self.player2 = Player('2','black')
        self.turn = self.player1

    def start_game(self):
        self.chess.board.bind("<Button-1>", self.click_handler)

    def click_handler(self,event):
        posX = self.chess.size_to_x_coordinates(event.x)
        posY = self.chess.size_to_y_coordinates(event.y)
        if self.board.containsPlayerPice(posX, posY, self.turn) and not self.board.isMoveCell(posX,posY):
            self.clean_board_moves()
            self.board.actualizeMoves(posX, posY)
        elif self.board.isMoveCell(posX,posY) and not self.board.containsPlayerPice(posX, posY, self.turn):
            self.board.movePice(posX,posY)
            self.clean_board_moves()
            self.changeTurn()
        elif self.board.containsPlayerPice(posX, posY, self.turn) and self.board.isMoveCell(posX,posY):
            self.board.movePice(posX,posY)
            self.clean_board_moves()
            self.changeTurn()
        else:
            self.clean_board_moves()
        if self.check_end_of_game():
            self.chess.window.destroy()
        self.reset_board()
    
    def changeTurn(self):
        if self.turn.equals(self.player1):
            self.turn = self.player2
        else:
            self.turn = self.player1

    def reset_board(self):
        self.chess.create_board()
        self.chess.display_pices(self.board)

    def clean_board_moves(self):
        for row in self.board.board:
            for cell in row:
                cell['m'] = ''

    def check_end_of_game(self):
        return not self.board.check_kings_alive()