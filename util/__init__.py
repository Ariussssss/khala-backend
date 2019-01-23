# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 16:05:04

from .singleton import SingletonMixin

def name_log(f):
    def wrap(self, *args, **kwargs):
        print('\n%s.%s'%(self.__class__.__name__, f.__name__))
        return f(self, *args, **kwargs)
    return wrap

class Obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [Obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, Obj(b) if isinstance(b, dict) else b)
