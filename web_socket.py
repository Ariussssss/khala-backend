# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-22 19:41:19


from tornado import web, websocket

class ChatHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        print('join')

    def on_close(self):
        print('leave')

    def on_message(self, message):
        print('send ' + message)
