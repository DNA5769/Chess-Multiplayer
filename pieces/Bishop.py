class Bishop:
  def __init__(self, r, c, color):
    self.color = color
    self.pos = (r, c)
    self.img = f'img/{color}B.png'

  def getPossibleMoves(self, board):
    moves = []
    r, c = self.pos

    # Moving top right
    for i in range(1, 8):
      posr = r-i
      posc = c+i
      
      if 0 <= posr <= 7 and 0 <= posc <= 7:
        if board[posr][posc] is None:
          moves.append((posr, posc))
        elif board[posr][posc].color != self.color:
          moves.append((posr, posc))
          break
        else:
          break
      else:
        break

    # Moving top left
    for i in range(1, 8):
      posr = r-i
      posc = c-i
      
      if 0 <= posr <= 7 and 0 <= posc <= 7:
        if board[posr][posc] is None:
          moves.append((posr, posc))
        elif board[posr][posc].color != self.color:
          moves.append((posr, posc))
          break
        else:
          break
      else:
        break

    # Moving bottom right
    for i in range(1, 8):
      posr = r+i
      posc = c+i
      
      if 0 <= posr <= 7 and 0 <= posc <= 7:
        if board[posr][posc] is None:
          moves.append((posr, posc))
        elif board[posr][posc].color != self.color:
          moves.append((posr, posc))
          break
        else:
          break
      else:
        break

    # Moving bottom left
    for i in range(1, 8):
      posr = r+i
      posc = c-i
      
      if 0 <= posr <= 7 and 0 <= posc <= 7:
        if board[posr][posc] is None:
          moves.append((posr, posc))
        elif board[posr][posc].color != self.color:
          moves.append((posr, posc))
          break
        else:
          break
      else:
        break

    return moves