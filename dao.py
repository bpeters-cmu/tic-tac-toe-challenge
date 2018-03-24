from game import Game

class GameDao:

    def __init__(self, redis):
        self.redis = redis

    def get_next_id(self):
        id = self.redis.incr('user:id', amount=1)
        return int(id)

    def save(self, game):
        self.redis.set('user:id', game.id)
        self.redis.hmset(game.id, game.to_json())
        key = str(game.id) + ':' + str(game.move)
        for i in game.board:
            self.redis.rpush(key, i)

    def get_saved_game(self, id):
        saved_game = self.redis.hmget(id, 'player1', 'player2', 'move', 'status', 'nextTurn')
        if not saved_game[0]:
            return None
        player1 = saved_game[0].decode('utf-8')
        player2 = saved_game[1].decode('utf-8')
        move = int(saved_game[2].decode('utf-8'))
        status = saved_game[3].decode('utf-8')
        next_turn = int(saved_game[4].decode('utf-8'))

        key = str(id) + ':' + str(move)
        board = []
        for i in self.redis.lrange(key, 0, 8):
            if(i.decode('utf-8') == 'None'):
                board.append(None)
            else:
                board.append(int(i))

        game = Game(id, player1, player2, board, status, move, next_turn)

        return game

    def get_all(self):
        game_list = []
        keys = [i + 1 for i in range(int(self.redis.get('user:id') or 0))]
        for sg in keys:
            game_list.append(self.get_saved_game(sg).to_json())
        return game_list
