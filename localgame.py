import ai.utils as utils
import ai.template as template

class Game:
  def __init__(self):
    self.board = utils.generate_init_state()
    self.AI = template.PlayerAI()

  def play(self, src, dst):
    if 0 <= src[0] < 6 and 0 <= src[1] < 6 \
      and 0 <= dst[0] < 6 and 0 <= dst[1] < 6 \
        and self.board[src[0]][src[1]] == 'W' \
          and self.board[dst[0]][dst[1]] != 'W' \
            and dst[0] - src[0] == -1 and abs(dst[1] - src[1]) <= 1:
      self.board[src[0]][src[1]] = '_'
      self.board[dst[0]][dst[1]] = 'W'
      return self.print_state()
    else:
      return "Invalid move!"
  
  def play_AI(self):
    move = self.AI.make_move(self.board)
    self.board = utils.state_change(self.board, move[0], move[1])
    return self.print_state()

  def print_state(self):
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
    return any(self.board[0][i] == 'W' for i in range(6)) or \
      any(self.board[5][i] == 'B' for i in range(6))