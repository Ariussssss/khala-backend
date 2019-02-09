# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 11:27:10


import redis

from util.singleton import SingletonMixin
from config import redis as cfg
from .redis.key_builder import KeyBuilder

class RedisClient(SingletonMixin):
    def __init__(self, host = cfg.host, port = cfg.port, db = cfg.db):
        self.pool = redis.ConnectionPool(host=host, port=port, db=db, decode_responses=True)

    def get_client(self):
        return redis.Redis(connection_pool=self.pool)
        
def getRedisClient():
    return RedisClient.instance().get_client()

if __name__ == '__main__':
    print(getRedisClient().spop(KeyBuilder.unrecv(1)))