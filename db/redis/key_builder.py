# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-02-09 17:55:56


class KeyBuilder(object):

    @staticmethod
    def create_redis_key(arr):
        return '.'.join([str(x) for x in arr])

    @staticmethod
    def unrecv(to):
        return KeyBuilder.create_redis_key(['unrecv',to])

if __name__ == '__main__':
    print(KeyBuilder.unrecv(1))