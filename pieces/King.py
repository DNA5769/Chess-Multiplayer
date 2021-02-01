class King:
  def __init__(self, color):
    self.color = color
    self.pos = (0 if self.color == 'B' else 7, 4)
    self.img = f'img/{color}K.png'