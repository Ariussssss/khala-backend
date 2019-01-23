import base64
from Crypto.Cipher import AES

def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes

def encrypt_oracle():
    key = '123456'
    text = 'abc123def456'
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    encrypt_aes = aes.encrypt(add_to_16(text))
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
    print(encrypted_text)

def decrypt_oralce():
    key = '123456'
    text = 'qR/TQk4INsWeXdMSbCDDdA=='
    aes = AES.new(add_to_16(key), AES.MODE_ECB)
    base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\0','') 
    print(decrypted_text)

if __name__ == '__main__':
    encrypt_oracle()
    decrypt_oralce()
