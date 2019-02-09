# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 11:25:29


import jwt
import time

from config import secret as cfg
from util import rd_int_str
from .aes import (
    aiur_encode,
    aiur_decode,
)

def set_sig(key, val):
    obj = {
        'nonce': rd_int_str(),
    }
    obj[key] = val
    key = '{0}_{1}'.format(cfg.sig, val)
    return aiur_encode(key, obj)

def check_sig(secret, text):
    name, val = secret
    key = '{0}_{1}'.format(cfg.sig, val)
    status, res = aiur_decode(key, text)
    if not status:
        return status, res.getattr('log_message')
    else:
        if res[name] == val:
            return True, None
        else:
            return False, 'signature err'

def create_token(account, secret=cfg.jwt):
    payload = {
        'account': account.copy(),
    }
    payload['iat'] = int(time.time())
    payload['exp'] = int(time.time()) + 86400 * 7
    status, res = set_sig('iat', payload['iat'])
    if status:
        payload['sig'] = res
        token = jwt.encode(payload, secret, algorithm='HS256')
        return status, token
    else:
        return status, res

def verify_token(token, secret=cfg.jwt):
    try:
        payload = jwt.decode(token, secret, algorithms=['HS256'])
        status, res = check_sig(('iat', payload['iat']), payload['sig'])
        if status:
            return True, payload['account']
        else:
            return False, res
    except Exception as e:
        return False, 'token err'

if __name__ == '__main__':
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50Ijp7ImlkIjoxMDAwMywibmFtZSI6ImFyaXVzIn0sImlhdCI6MTU0ODU4NDMxMywiZXhwIjoxNTQ5MTg5MTEzLCJzaWciOiJISHprSWlMUGFiSG5QaW0vL3ExNHYzUjgzc1c4UTlaOW5kRU9zZFA2UHY4WUZibWpuNElIbXo3ZmN6UW02ak5ISzE0UnBBWkdMbXR1XG5pZDFseE1tVEZBPT1cbiJ9.qD1Tc-78vmhFRdF9WvI3ubGt4UyfOox-l8BCHDcw-Jw'
    print(verify_token(token))
