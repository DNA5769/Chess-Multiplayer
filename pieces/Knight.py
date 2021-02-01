class Knight:
  def __init__(self, r, c, color):
    self.color = color
    self.pos = (r, c)
    self.img = f'img/{color}H.png'

  def getPossibleMoves(self, board):
    moves = []
    r, c = self.pos

    for x, y in [(-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2), (2, 1), (1, 2)]:
      posr = r+y
      posc = c+x
      
      if 0 <= posr <= 7 and 0 <= posc <= 7 and (board[posr][posc] is None or board[posr][posc].color != self.color):
        moves.append((posr, posc))

    return moves