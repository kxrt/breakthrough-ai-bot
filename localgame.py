import ai.utils as utils
import ai.template as template

class Game:
  def __init__(self):
    self.board = utils.generate_init_state()
    self.AI = template.PlayerAI()

  def play(self, src, dst):
    '''
    Plays a move for the player, and returns the new state.
    Checks if the move is valid, and if so, makes the move.

    The following conditions must be met for a move to be valid:
      - The source and destination are on the board.
      - The source is occupied by a white piece.
      - The destination is not occupied by a white piece.
      - The destination is one row above the source.
      - The destination is one column to the left, right, or in the same column as the source.
      - If the destination is in the same column as the source, the destination is not occupied by a piece.
    '''
    if 0 <= src[0] < 6 and 0 <= src[1] < 6 \
      and 0 <= dst[0] < 6 and 0 <= dst[1] < 6 \
        and self.board[src[0]][src[1]] == 'W' \
          and self.board[dst[0]][dst[1]] != 'W' \
            and dst[0] - src[0] == -1 and abs(dst[1] - src[1]) <= 1 \
              and (dst[1] != src[1] or self.board[dst[0]][dst[1]] == '_'):
      self.board[src[0]][src[1]] = '_'
      self.board[dst[0]][dst[1]] = 'W'
      return self.print_state()
    else:
      return "Invalid move!"
  
  def play_AI(self):
    '''
    Plays a move for the AI, and returns the new state.
    '''    
    move = self.AI.make_move(self.board)
    self.board = utils.state_change(self.board, move[0], move[1])
    return self.print_state()

  def print_state(self):
    '''
    Modified version of utils.print_state(board), to be used in Discord. 
    Wraps the output in a code block, and adds row/col numbers for accessibility.
    '''
    COL = 6
    output = '```'
    horizontal_rule = '+' + ('-'*5 + '+') * COL
    for i in range(len(self.board)):
        output += '\n' + horizontal_rule
        output += '\n' + '|  ' +  '  |  '.join(' ' if self.board[i][j] == '_' else self.board[i][j] for j in range(COL)) + '  |' + ' ' + str(i)
    output += '\n' + horizontal_rule
    output += '\n' + ''.join('   ' + str(i) + '  ' for i in range(COL))
    output += '```'
    return output

  def is_over(self):
    ''' 
    Checks if the game is over.
    '''
    return any(self.board[0][i] == 'W' for i in range(6)) or \
      any(self.board[5][i] == 'B' for i in range(6))