class Game:
  def __init__(self):
    self.board = getBoard()

  def getBoard(self):
    board = []

    for i in range(8):
      board.append([])
      for j in range(8):
        board[i].append([(i,j)])

    return board