# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 18:07:05


from unittest import TestCase
import json

from util import name_log
from db.redis_db import getRedisClient
from db.mysql_db import getDBCursor

class TestRedis(TestCase):

    @name_log
    def test_getRedisClient(self):
        import time
        a, b = getRedisClient(), getRedisClient()
        req = str(time.time())
        a.set('test', req)
        res = b.get('test')
        self.assertEqual(req, res)

# todo threading test