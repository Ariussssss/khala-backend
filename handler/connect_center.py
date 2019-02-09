# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-07 19:50:58

from util.singleton import SingletonMixin

class CnCenter(SingletonMixin):
    def __init__(self):
        self._onLine = {}
        self._chat = {}

    @property
    def all_connection(self):
        return list(self._onLine.values())

    @property
    def all_members(self):
        return list(self._onLine.keys())

    def get_connection(self, key):
        key = str(key)
        if key in self.all_members:
            return self._onLine[key]
        else:
            return None

    def add(self, key, con):
        self._onLine[str(key)] = con

    def remove(self, key):
        del self._onLine[str(key)]

    def blocast_chat(self, msg_info, to):
        if to == None:
            pass
        else:
            for con in to:
                con.write_message(msg_info)
        