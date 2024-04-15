"""

Databases

"""

class GameBoard():
   def __init__(self):
      #Board 8x8, the elements has two characyers b/w(represents chess color),
      #The second character represents the type of the piece 'K','Q','R','B', 'N', 'P',
      #"--" an empty space.
      self.board = [
         ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
         ["bp", "bp", "bp", "bp", "bp" ,"bp", "bp", "bp"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["--", "--", "--", "--", "--", "--", "--", "--"],
         ["wp", "wp", "wp", "wp", "wp" ,"wp", "wp", "wp"],
         ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
      ]
      self.whiteToMove = True
      self.moveLog = []