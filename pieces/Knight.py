class Knight:
  def __init__(self, r, c, color):
    self.color = color
    self.pos = (r, c)
    self.img = f'img/{color}H.png'