from pieces.Pawn import Pawn
from pieces.King import King
from pieces.Queen import Queen

class Game:
  def __init__(self):
    self.board = self.getBoard()

  def getBoard(self):
    return [
      [None, None, None, Queen('B'), King('B'), None, None, None],
      [Pawn(1, c, 'B') for c in range(8)],
      [None]*8,
      [None]*8,
      [None]*8,
      [None]*8,
      [Pawn(6, c, 'W') for c in range(8)],
      [None, None, None, Queen('W'), King('W'), None, None, None],
    ]