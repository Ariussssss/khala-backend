# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 16:05:04

from random import randint

from .singleton import SingletonMixin

def name_log(f):
    def wrap(self, *args, **kwargs):
        print('\n%s.%s'%(self.__class__.__name__, f.__name__))
        return f(self, *args, **kwargs)
    return wrap

def rd_int_str(num=8):
    return [randint(0, 9) for p in range(0, 10)]

class Obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [Obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, Obj(b) if isinstance(b, dict) else b)

def random_str(length):
    random_str_base='1234567890qwertyuiopasdfghjklzxcvbnm'
    random_str_base_length = len(random_str_base) - 1
    return ''.join([random_str_base[randint(0, random_str_base_length)]
        for x in range(0, length)])