class Queen:
  def __init__(self, color):
    self.color = color
    self.pos = (0 if self.color == 'B' else 7, 3)
    self.img = f'img/{color}Q.png'

  def getPossibleMoves(self, board):
    moves = []
    r, c = self.pos

    # Moving right
    for i in range(1, 8):
      posr = r
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

    # Moving left
    for i in range(1, 8):
      posr = r
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

    # Moving up
    for i in range(1, 8):
      posr = r-i
      posc = c
      
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

    # Moving down
    for i in range(1, 8):
      posr = r+i
      posc = c
      
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