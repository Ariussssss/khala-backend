# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-05-08 18:42:27


from db.mysql.sql_builder import SqlBuilder as sql
from . import OrmBase

class Usr(OrmBase):

    def login(self, usr, pwd):
        SELECT_COLUMN = ('id', 'name')
        q = sql.login(usr, pwd, SELECT_COLUMN)
        code, server = self._mc.do(q)
        if code and server.rowcount() > 0:
            return dict(zip(SELECT_COLUMN, server.first()))
        else:
            return {}

    def create(self, usr, pwd):
        SELECT_COLUMN = ('id', 'name')
        q = sql.register(usr, pwd)
        code, _ = self._mc.do(q)
        return code

    def get_usr(self, id):
        SELECT_COLUMN = ('id', 'name')
        q = sql.get_usr(id)
        code, server = self._mc.do(q)
        res = server.first()
        if code and res:
            return dict(zip(SELECT_COLUMN, res))
        else:
            return {}

    def get_usr_by_name(self, key):
        SELECT_COLUMN = ('id', 'name')
        q = sql.searchUsr(key)
        print(q)
        code, server = self._mc.do(q)
        res = server.first()
        if code and res:
            return dict(zip(SELECT_COLUMN, res))
        else:
            return {}

