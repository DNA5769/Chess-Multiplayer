class Queen:
  def __init__(self, color):
    self.color = color
    self.pos = (0 if self.color == 'B' else 7, 3)
    self.img = f'img/{color}Q.png'