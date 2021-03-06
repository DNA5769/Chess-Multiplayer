class King:
  def __init__(self, color):
    self.color = color
    self.pos = (0 if self.color == 'B' else 7, 4)
    self.img = f'img/{color}K.png'

  def getPossibleMoves(self, board):
    moves = []
    r, c = self.pos

    # TODO: Prevent moving to a square which is attacked
    for x, y in [(-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]:
      posr = r+y
      posc = c+x

      if 0 <= posr <= 7 and 0 <= posc <= 7 and (board[posr][posc] is None or board[posr][posc].color != self.color):
        moves.append((posr, posc))

    return moves