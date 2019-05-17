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
from .model.usr import Usr


class LoginHandler(BaseHandler):

    def _post(self):
        usr = self.get_argument('usr').strip()
        pwd = sha1(self.get_argument('pwd').strip())
        usr_model = Usr()
        usr_info = usr_model.login(usr, pwd)
        if usr_info:
            status, res = create_token(usr_info)
            if status:
                return cfg.suc.code, {
                    'account': usr_info,
                    'token': res.decode('utf-8'),
                }
            else:
                return cfg.svr.code, {
                    'err': str(res),
                }
        else:
            return cfg.na.code, {
                'err': cfg.na.text,
            }

class RegisHandler(BaseHandler):

    def _post(self):
        SELECT_COLUMN = ('id', 'name')
        usr = self.get_argument('usr').strip()
        pwd = sha1(self.get_argument('pwd').strip())
        usr_model = Usr()
        if usr_model.create(usr, pwd):
            usr_info = usr_model.login(usr, pwd)
            status, res = create_token(usr_info)
            if status:
                return cfg.suc.code, {
                    'account': usr_info,
                    'token': res.decode('utf-8'),
                }
            else:
                return cfg.svr.code, {
                    'err': str(res),
                }
        else:
            return cfg.mis.code, {
                'err': cfg.mis.text,
            }

class CheckHandler(BaseHandler):

    def _post(self):
        key = self.get_argument('key').strip()
        q = sql.check_exist_by_name(key)
        mc = MysqlClient.instance()
        code, server = mc.do(q)
        if code and server.first()[0]:
            return cfg.mis.code, {
                'err': 'key exist',
            }
        else:
            return cfg.suc.code, {
                'msg': 'ok',
            }