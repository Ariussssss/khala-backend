# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 11:25:29


import jwt
import time

def create_token(account, secret):
    payload = account.copy()
    payload['iat'] = int(time.time())
    payload['exp'] = int(time.time()) + 86400 * 7
    token = jwt.encode(payload, secret, algorithm='HS256')
    return True, {'token': token, 'account_id': account['_id']}

def verify_bearer_token(token, secret):
    payload = jwt.decode(token, secret, algorithms=['HS256'])
    if payload:
        return True, payload
    return False, token
