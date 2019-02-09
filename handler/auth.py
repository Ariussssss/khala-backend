# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-24 18:53:29

from . import BaseHandler
from config import code as cfg
from db.mysql.sql_builder import SqlBuilder as sql
from db.mysql_db import MysqlClient
from auth.aes import (
    sha1,
    aiur_encode,
    aiur_decode,
)
from auth import create_token

class LoginHandler(BaseHandler):

    def _post(self):
        arr = ('id', 'name')
        usr = self.get_argument('user').strip()
        pwd = sha1(self.get_argument('pwd').strip())
        q = sql.login(usr, pwd, arr)
        mc = MysqlClient.instance()
        code, server = mc.do(q)
        if code and server.rowcount() > 0:
            r = dict(zip(arr, server.first()))
            status, res = create_token(r)
            if status:
                return cfg.suc.code, {
                    'account': r,
                    'token': res.decode('utf-8'),
                }
            else:
                return cfg.svr.code, {
                    'err': res,
                }
        else:
            return cfg.na.code, {
                'err': cfg.na.text,
            }

class RegisHandler(BaseHandler):

    def _post(self):
        usr = self.get_argument('user').strip()
        pwd = sha1(self.get_argument('pwd').strip())
        q = sql.register(usr, pwd)
        mc = MysqlClient.instance()
        print(q)
        code, server = mc.do(q)
        print(code)
        print(server)
        print(server.rowcount)
        print(server.first())
