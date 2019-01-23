# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 11:27:23


import json

class ConCenter(object):
    def __init__(self):
        self._onLine = []
        self._chat = []

    def function():
        pass

    def blocast_chat(self, msg_info, to):
        if to == None:
            pass
        else:
            for con in to:
                con.write_message(msg_info)
        