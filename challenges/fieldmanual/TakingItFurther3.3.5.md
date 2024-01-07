## CRYPTOGRAPHY
# Taking it Further

# Next steps
There are a huge number of tools, articles, and resources to learn more about cryptography. We have just touched on a few ways of encrypting and decrypting data.

One of the wonderful things about the crypto discipline in cyber security is that there are many widely published and available resources. Indeed, academic papers are constantly published challenging or validating the implementation that protects all the data in our modern world. The major benefit of this is if you are interested in taking it further, there are lots of great resources!

You could also take some time to play with [pycrypto](https://pypi.org/project/pycrypto/): a Python module which provides access to cryptographic routines and ciphers for you to try with minimal coding. For example, you can install it and then encrypt some data using AES!
```bash
$ pip3 install Crypto
```
```py
from Crypto.Cipher import AES

# Set plaintext message
msg = "This data needs to be protected at all costs with strong security"

# Input strings must be a multiple of 16 in length, so pad out with X chars
msgPadded = msg
while len(bytes(msgPadded, encoding='utf-8')) % 16 != 0:
     msgPadded = msgPadded + 'X'

# Encryption
obj = AES.new('WhAt a C00L K3Y!', AES.MODE_CBC, 'WHAT AN IV!!!!!!')
ciphertext = obj.encrypt(msgPadded)

# Decryption (including cutting down to original message size)
obj2 = AES.new('WhAt a C00L K3Y!', AES.MODE_CBC, 'WHAT AN IV!!!!!!')
output = obj2.decrypt(ciphertext)[0:len(msg)]
```

If you would like to read more about applied cryptography, or the amazing history of how it changed the world, consider these books:

- Understanding Cryptography by Christof Paar
- The Code Book by Simon Singh
- An Introduction to Mathematical Cryptography by Jeffrey Hoffstein
- Applied Cryptography by Bruce Schneier (an older book, but wonderful review of functioning principles)
This subject is undoubtedly one that requires more structured analysis and maths than other areas of cyber security, but it is also a supporting pillar of the modern world!
