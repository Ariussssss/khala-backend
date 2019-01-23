import jwt
import time

def create_token(account):
    payload = {
        'iss': 'create_token',
        'iat': int(time.time()),
        'exp': int(time.time()) + 86400 * 7,
        'sub': account['_id'],
        'username': account['username'],
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return True, {'access_token': token, 'account_id': account['_id']}
    

def verify_bearer_token(token):
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    if payload:
        return True, payload
    return False, token

if __name__ == '__main__':
    account = {
        '_id': 1,
        'username': 'Arius',
    }
    _, token = create_token(account)
    print(token)
    _, payload  = verify_bearer_token(token['access_token'])
    print(payload)
