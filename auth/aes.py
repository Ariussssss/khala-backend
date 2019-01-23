# -*- coding: utf-8 -*-
# @Author: Arius
# @Email: arius@qq.com
# @Date:   2019-01-23 15:08:40


import base64
import json
from Crypto.Cipher import AES

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)

def aiur_encode(key, obj):
    try:
        text = json.dumps(obj)
        aes = AES.new(add_to_16(key), AES.MODE_ECB)
        encrypt_aes = aes.encrypt(add_to_16(text))
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8').replace('\0','') 
        return True, encrypted_text
    except Exception as e:
        return False, e

def aiur_decode(key, text):
    try:
        aes = AES.new(add_to_16(key), AES.MODE_ECB)
        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
        decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','') 
        return True, json.loads(decrypted_text)
    except Exception as e:
        return False, e
