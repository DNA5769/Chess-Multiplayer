class King:
  def __init__(self, color):
    self.color = color
    self.img = f'img/{color}K.png'
    self.pos = (0, 4) if self.color == 'B' else (7, 4)

  def possib_moves(self):
    moves = []
    for i in [-1, 0, 1]:
      for j in [-1, 0, 1]:
        if i != j != 0 and 0 <= self.pos+i <= 7 and 0 <= self.pos+j <= 7:
          moves.append((self.pos+i, self.pos+j))

    return moves
