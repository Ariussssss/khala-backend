# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 11:27:29


import signal
from functools import partial
from tornado import (
    web,
    ioloop,
    httpserver,
)
import os

from shutdown import sig_handler
from web_socket import ChatHandler

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

class BaseHandler(web.RequestHandler):
    def __init__(self, arg):
        super(BaseHandler, self).__init__()
        self.arg = arg

class TornadoMain(web.Application):
    def __init__(self):
        web.Application.__init__(self, [
            (r'/chat', ChatHandler),
        ], **settings)
    
def main():
    app = TornadoMain()    
    server = httpserver.HTTPServer(app)
    server.listen(3154)
    signal.signal(signal.SIGTERM, partial(sig_handler, server))
    signal.signal(signal.SIGINT, partial(sig_handler, server))
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
