from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
from api import GameHandler
import tornado.web
import tornado.options
import redis
import config


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/api/games/?", GameHandler),
            (r"/api/games/([0-9]+)", GameHandler)
        ]
        tornado.web.Application.__init__(self, handlers)
        self.redis = redis.Redis(config.redis_host)

def main():
    app = Application()
    tornado.options.parse_command_line()
    app.listen(80)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
