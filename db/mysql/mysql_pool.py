# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 21:45:12


import threading
import pymysql

from util.singleton import SingletonMixin
from config import mysql as cfg

class MysqlPool(SingletonMixin):
    def __init__(self, host=cfg.host, username=cfg.usr, pwd=cfg.pwd, dbname=cfg.db):
        self.pool = {}
        self.host = host
        self.username = username
        self.pwd = pwd
        self.dbname = dbname

    def get_instance(self):
        name = threading.current_thread().name
        if name not in self.pool:
            conn = pymysql.connect(self.host, self.username, self.pwd, self.dbname)
            self.pool[name] = conn
        return self.pool[name]
