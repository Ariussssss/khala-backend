# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 15:29:05

from unittest import TestCase
import json

from util import name_log
from auth import (
    create_token,
    verify_bearer_token,
)
from auth.aes import (
    aiur_encode,
    aiur_decode,
)

class TestAuth(TestCase):

    @name_log
    def test_init(self):
        secret = '123'
        account = {
            '_id': 1,
            'username': 'sab',
        }
        status, res = create_token(account, secret)
        self.assertTrue(status)
        status, res = verify_bearer_token(res['token'], secret)
        self.assertTrue(status)
        if status:
            for k, v in account.items():
                self.assertEqual(res[k], v)

class TestAuthAes(TestCase):

    @name_log
    def test_aes(self):
        secret = '123'
        account = {
            '_id': 1,
            'username': 'sab',
        }
        status, text = aiur_encode(secret, account)
        self.assertTrue(status)
        status, res = aiur_decode('1', text)
        self.assertFalse(status)
        status, res = aiur_decode(secret, text)
        self.assertTrue(status)
        self.assertEqual(json.dumps(account), json.dumps(res))
