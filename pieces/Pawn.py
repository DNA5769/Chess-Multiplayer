class Pawn:
  def __init__(self, r, c, color):
    self.pos = (r, c)
    self.first = True
    self.color = color
    self.img = f'img/{color}P.png'

  def getPossibleMoves(self, board):
    moves = []
    r, c = self.pos

    if self.color == 'W':
      if r != 0 and board[r-1][c] is None:
        moves.append((r-1, c))
      if self.first and board[r-2][c] is None:
        moves.append((r-2, c))
      if r != 0:
        if c != 0 and board[r-1][c-1] is not None and board[r-1][c-1].color != self.color:
          moves.append((r-1, c-1))
        if c != 7 and board[r-1][c+1] is not None and board[r-1][c+1].color != self.color:
          moves.append((r-1, c+1))
    else:
      if r != 7 and board[r+1][c] is None:
        moves.append((r+1, c))
      if self.first and board[r+2][c] is None:
        moves.append((r+2, c))
      if r != 7:
        if c != 0 and board[r+1][c-1] is not None and board[r+1][c-1].color != self.color:
          moves.append((r+1, c-1))
        if c != 7 and board[r+1][c+1] is not None and board[r+1][c+1].color != self.color:
          moves.append((r+1, c+1))

    return moves