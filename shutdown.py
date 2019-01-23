# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 11:27:35


import signal
import time
import tornado.web
import tornado.ioloop
import logging

MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3

def sig_handler(server, sig, frame):
    io_loop = tornado.ioloop.IOLoop.instance()

    def stop_loop(deadline):
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            logging.info('Waiting for next tick')
            io_loop.add_timeout(now + 1, stop_loop, deadline)
        else:
            io_loop.stop()
            logging.info('Shutdown finally')

    def shutdown():
        logging.info('Stopping http server')
        server.stop()
        logging.info('Will shutdown in %s seconds ...',
                     MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)
        stop_loop(time.time() + MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)

    logging.warning('Caught signal: %s', sig)
    io_loop.add_callback_from_signal(shutdown)
    
