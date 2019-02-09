# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 11:26:50


from util.singleton import SingletonMixin
from .mysql.sql_sup import SqlRes
from .mysql.sql_builder import SqlBuilder
from .mysql.mysql_pool import MysqlPool

class MysqlClient(SingletonMixin):
    __pool = MysqlPool.instance()

    def s(self):
        return self.__pool.get_instance()

    def do(self, sql):
        db = self.__pool.get_instance()
        cursor = db.cursor()
        # sql_str = sql
        sql_str = sql.replace('"', '`')
        try:
            cursor.execute(sql_str)
            db.commit()
            return True, SqlRes(cursor, db)
        except Exception as e:
            db.rollback()
            return False, e
