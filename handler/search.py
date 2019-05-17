# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-05-01 22:39:17


from . import BaseHandler
from config import code as cfg
from db.mysql.sql_builder import SqlBuilder as sql
from db.mysql_db import MysqlClient
from .model.usr import Usr

class SearchHandler(BaseHandler):

    def _post(self):
        key = self.get_argument('key')
        column = self.get_argument('column', None)
        q = sql.search(key)
        mc = MysqlClient.instance()
        code, server = mc.do(q)
        if code:
            res = server.all()
            return cfg.suc.code, {
                'res': [
                    {
                        'id': row[0],
                        'name': row[1],
                        'targetType': int(row[2]),
                    }
                    for row in res
                    if not column or int(column) == int(row[2])
                ],
            }
        else:
            return cfg.svr.code, {
                'err': cfg.svr.text,
            }

class UsrSearchHandler(BaseHandler):

    def _post(self):
        usr_model = Usr()
        key = self.get_argument('key')
        print(key)
        usr_info = usr_model.get_usr_by_name(key)
        if usr_info:
            return cfg.suc.code, {
                'usr_info': usr_info,
            }
        else:
            return cfg.svr.code, {
                'err': cfg.svr.text,
            }
        
