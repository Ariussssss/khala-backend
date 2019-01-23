# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 17:46:37


from util import Obj

mysql = Obj.instance({
    'host': '127.0.0.1',
    'usr': 'root',
    'pwd': 'root',
    'db': 'test',
})

redis = Obj.instance({
    'host': '127.0.0.1',
    'port': '6379',
    'db': 0,
})
