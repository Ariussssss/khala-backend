# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-05-08 18:50:54

from db.mysql_db import MysqlClient

class OrmBase(object):
    _mc = MysqlClient.instance()
