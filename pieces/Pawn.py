class Pawn:
  def __init__(self, r, c, color):
    self.pos = (r, c)
    self.color = color
    self.img = f'img/{color}P.png'
