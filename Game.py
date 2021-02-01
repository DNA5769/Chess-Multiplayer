from pieces.Pawn import Pawn
from pieces.King import King
from pieces.Queen import Queen
from pieces.Bishop import Bishop
from pieces.Knight import Knight

class Game:
  def __init__(self):
    self.board = self.getBoard()

  def getBoard(self):
    return [
      [None, Knight(0, 1, 'B'), Bishop(0, 2, 'B'), Queen('B'), King('B'), Bishop(0, 5, 'B'), Knight(0, 6, 'B'), None],
      [Pawn(1, c, 'B') for c in range(8)],
      [None]*8,
      [None]*8,
      [None]*8,
      [None]*8,
      [Pawn(6, c, 'W') for c in range(8)],
      [None, Knight(7, 1, 'W'), Bishop(7, 2, 'W'), Queen('W'), King('W'), Bishop(7, 5, 'W'), Knight(7, 6, 'W'), None],
    ]