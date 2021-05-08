from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
# pip3 install eciespy
class CryptUtil:
    def __init__(self):
        pass

    def generateEciesKey(self):
        eth_key = generate_eth_key()
        return eth_key

    def encrypt(self, publickey_hex, bytesdata):
        return encrypt(publickey_hex, bytesdata)

    def decrypt(self, secretkey_hex, encrypt_str_bytes, ):
        return decrypt(secretkey_hex, encrypt_str_bytes)