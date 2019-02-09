# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 21:48:15

from pypika import Query, Table, Field, Order
import time

from auth.aes import sha1
from config import tables as cfg

def sql_fmt(func):
    def wrap(self, *args, **kwargs):
        res = func(self, *args, **kwargs)
        return res.get_sql().replace('"', '`')
    return wrap

class SqlBuilder(object):

    @sql_fmt
    def login(name, pwd, arr):
        usr = Table(cfg.usr)
        q = Query.from_(usr).select(
                *arr
            ).where(
                usr.name == name
            ).where(
                usr.pwd == pwd
            )
        return q

    @sql_fmt
    def register(name, pwd):
        usr = Table(cfg.usr)
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        q = Query.into(usr).insert(
            None, name, pwd, now, now
        )
        return q

if __name__ == '__main__':
    print (SqlBuilder.register('aaa', 'bbb'))
