
class Game:
    in_progress = 'In Progress'
    draw = 'Draw'
    win = 'Wins!'
    player1_marker = 1
    player2_marker = 0

    def __init__(self,id, player1, player2, board, status, move, next_turn):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.status = status
        self.move = move
        self.next_turn = next_turn

    def update_game(self):
        self.move += 1
        if(Game.check_status(self.board, self.next_turn)):
            self.status = self.next_turn + ' ' + Game.win
        elif(not None in self.board):
            self.status = Game.draw
        else:
            if self.next_turn == Game.player1_marker:
                self.next_turn = Game.player2_marker
            else:
                self.next_turn = Game.player1_marker

    def make_move(self, player, location):
        if self.status != Game.in_progress:
            return False, 'Game Over'
        if player != 0 and player != 1:
            return False, 'Player must be 0 or 1'
        if not 0 <= location <=8:
            return False, 'Location must be between 0 - 8'
        if self.board[location] is not None:
            return False, 'There is already a marker in that location'
        if player != self.next_turn:
            return False, 'It is not your turn!'

        self.board[location] = player
        return True, None


    def to_json(self):
        return {
            'id': self.id,
            'player1': self.player1,
            'player2': self.player2,
            'board': self.board,
            'move': self.move,
            'status': self.status,
            'nextTurn': self.next_turn
        }

    @staticmethod
    def invalid_move(msg):
        return {
            'error': 'invalid move - ' + msg
        }

    @staticmethod
    def check_status(board, xo):
        if board[0] == xo and board[1] == xo and board[2] == xo:
            return True
        if board[3] == xo and board[4] == xo and board[5] == xo:
            return True
        if board[6] == xo and board[7] == xo and board[8] == xo:
            return True
        if board[2] == xo and board[5] == xo and board[8] == xo:
            return True
        if board[1] == xo and board[4] == xo and board[7] == xo:
            return True
        if board[0] == xo and board[3] == xo and board[6] == xo:
            return True
        if board[0] == xo and board[4] == xo and board[8] == xo:
            return True
        if board[2] == xo and board[4] == xo and board[6] == xo:
            return True
        return False
