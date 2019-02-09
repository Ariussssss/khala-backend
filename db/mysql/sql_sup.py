# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 21:42:15


class SqlRes(object):
    def __init__(self, cursor, db):
        self._cursor = cursor
        self._db = db
    
    def last_id(self):
        return self._cursor.lastrowid
    
    def rowcount(self):
        return self._cursor.rowcount
    
    def description(self):
        return self._cursor.description

    def first(self):
        return self._cursor.fetchone()

    def all(self):
        return self._cursor.fetchall()
