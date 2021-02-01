from pieces.Pawn import Pawn
from pieces.King import King
from pieces.Queen import Queen
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Rook import Rook

import copy

class Game:
  def __init__(self):
    self.board = self.getBoard()
    self.turn = 'W'
    self.state = 0

  def getBoard(self):
    return [
      [Rook(0, 0, 'B'), Knight(0, 1, 'B'), Bishop(0, 2, 'B'), Queen('B'), King('B'), Bishop(0, 5, 'B'), Knight(0, 6, 'B'), Rook(0, 7, 'B')],
      [Pawn(1, c, 'B') for c in range(8)],
      [None]*8,
      [None]*8,
      [None]*8,
      [None]*8,
      [Pawn(6, c, 'W') for c in range(8)],
      [Rook(7, 0, 'W'), Knight(7, 1, 'W'), Bishop(7, 2, 'W'), Queen('W'), King('W'), Bishop(7, 5, 'W'), Knight(7, 6, 'W'), Rook(7, 7, 'W')],
    ]

  def getPossibleMoves(self, r, c):
    moves = self.board[r][c].getPossibleMoves(self.board)
    moves = [move for move in moves if self.isLegalMove((r, c), move)]
    return moves

  def isLegalMove(self, piece, target):
    temp_piece = copy.deepcopy(self.board[piece[0]][piece[1]])
    temp_target = copy.deepcopy(self.board[target[0]][target[1]])

    self.board[target[0]][target[1]] = self.board[piece[0]][piece[1]]
    self.board[target[0]][target[1]].pos = target
    self.board[piece[0]][piece[1]] = None

    # Find our king
    king = self.getKing(temp_piece.color)

    # Check if king in danger
    legal = True
    for row in self.board:
      if not legal:
        break

      for col in row:
        if col is not None and col.color != temp_piece.color and king.pos in col.getPossibleMoves(self.board):
          legal = False
          break

    self.board[piece[0]][piece[1]] = temp_piece
    self.board[target[0]][target[1]] = temp_target

    return legal

  def getKing(self, color):
    for row in self.board:
      for col in row:
        if col is not None and type(col) == King and col.color == color:
          return col

  def move(self, piece, target):
    self.board[target[0]][target[1]] = self.board[piece[0]][piece[1]]
    self.board[target[0]][target[1]].pos = target
    self.board[piece[0]][piece[1]] = None

    self.turn = 'B' if self.turn == 'W' else 'W'

    # Find enemy King
    king = self.getKing(self.turn)

    # Check if king in danger
    check = False
    for row in self.board:
      if check:
        break

      for col in row:
        if col is not None and col.color != self.turn and king.pos in col.getPossibleMoves(self.board):
          check = True
          break

    if check:
      self.state = -1 if self.turn == 'W' else 1
    else:
      self.state = 0

    if type(self.board[target[0]][target[1]]) == Pawn and abs(target[0]-piece[0]) == 2:
      self.board[target[0]][target[1]].first = False