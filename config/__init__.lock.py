# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 17:46:37


from util import Obj

mysql = Obj({
    'host': '127.0.0.1',
    'usr': 'root',
    'pwd': 'root',
    'db': 'test',
})

redis = Obj({
    'host': '127.0.0.1',
    'port': '6379',
    'db': 0,
})

# default config

secret = Obj({
    'jwt': 'aiur_world',
    'sig': 'link',
})

tables = Obj({
    'usr': 'User',
})

code = Obj({
    'suc': {
        'code': 200,
        'text': '',
    }, 'ser': {
        'code': 400,
        'text': '',
    }, 'na': {
        'code': 503,
        'text': 'account or pwd not correct',
    },
})