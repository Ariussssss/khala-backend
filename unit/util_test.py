# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 16:59:33


from unittest import TestCase

from util import name_log
from util.singleton import SingletonMixin

class TestUtilSingleton(TestCase):

    @name_log
    def test_singletonMixin(self):
        class A(SingletonMixin):
            def __init__(self, x):
                self.x = x
        a, a2 = A.instance(1), A.instance(2)
        self.assertEqual(a, a2)
        self.assertEqual(a.x, 1)
        self.assertEqual(a2.x, 1)
        a.x = 3
        self.assertEqual(a2.x, 3)
        