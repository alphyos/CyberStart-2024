# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

with open('words.txt', 'r', encoding='utf-8') as f:
    words = f.read().splitlines()
    for secret in words:
        if secret[-1:] == "\n":
            print("Error, new line character at the end of the string. This will not match!")
        elif len(secret.encode('utf-8')) >= 32:
            print("Error, string too long. Must be less than 32 bytes.")
        else:
            # create a cipher object using the secret
            cipher = AES.new(secret.encode('utf-8') + (BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING.encode(), AES.MODE_ECB)
            # decode the encoded string
            decoded = decode_aes(cipher, encrypted)

            if decoded.startswith('FLAG:'):
                print("\n")
                print("Success: "+secret+"\n")
                print(decoded+"\n")
                break
            else:
                print('Wrong password')
