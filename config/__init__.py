# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 16:10:52


from util import Obj

mysql = Obj({
    'host': '127.0.0.1',
    'usr': 'archbishop',
    'pwd': 'ForAiur!1',
    'db': 'Khala',
})

redis = Obj({
    'host': '127.0.0.1',
    'port': '6379',
    'db': 9,
})

# default config

secret = Obj({
    'jwt': 'aiur_world',
    'sig': 'link',
})

tables = Obj({
    'usr': 'User',
    'room': 'Room',
    'join': 'Join',
})

code = Obj({
    'suc': {
        'code': 200,
        'text': '',
    },'aut': {
        'code': 403,
        'text': 'no auth',
    },'mis': {
        'code': 400,
        'text': 'error request',
    }, 'svr': {
        'code': 500,
        'text': 'server error',
    }, 'na': {
        'code': 503,
        'text': 'account or pwd not correct',
    },
})

msg = Obj({
    'type': {
        'text': 0,
        'pic': 1,
        'meme': 2,
        'code': 3,
    }, 
    'send': {
        'usr': 0,
        'group': 1,
        'system': 2,
    },
    'action': {
        'join_group': 0,
        'leave_group': 1,
        'not_roommate': 2,
    }
})
