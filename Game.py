from Pawn import Pawn

class Game:
  def __init__(self):
    self.board = getBoard()

  def getBoard(self):
    return [
      [None]*8,
      [Pawn(1, c, 'B') for c in range(8)],
      [None]*8,
      [None]*8,
      [None]*8,
      [None]*8,
      [Pawn(6, c, 'W') for c in range(8)],
      [None]*8,
    ]