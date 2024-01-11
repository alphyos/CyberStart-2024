# 〰 New Line Of Communication - L08 C01

When you were on the last level we discovered the aliens had been communicating with a human insider back on Earth, and by email of all things! Well, it seems that may have been a bit of a decoy as they're also exchanging secret encrypted messages from a server on one of the probe ships.

We need you to write a script which can connect over TCP to the following server ("localhost", 10000) and send 'GET' to retrieve the encrypted messages. You then need to decrypt them and send them back split by \n. We think you'll receive 3 sentences and they're encrypted with a caesar cipher that has a different random offset per sentence.

Finally, print the response after sending the decrypted messages to get the flag.

**Tip:** Remember, each encrypted message has a different random offset.

> 💡 Hint: You can only send the correct text back so you'll need some way to determine which is a real sentence.
>
> Try a search on letter goodness

## Answer

```python
#
# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#

import socket
import re

def caesar(st, n):

    ret = ""
    for c in st:
        i = ord(c)
        if (65 <= i and i < 91):
            ret += chr((i + n + 13) % 26 + 65)
        else:
            ret += c
    return ret

def crack_caesar(st):

    weight = [
      8.34, # A
      1.54, # B
      2.73, # C
      4.14, # D
      12.60,# E
      2.03, # F
      1.92, # G
      6.11, # H
      6.71, # I
      0.23, # J
      0.87, # K
      4.24, # L
      2.53, # M
      6.80, # N
      7.70, # O
      1.66, # P
      0.09, # Q
      5.68, # R
      6.11, # S
      9.37, # T
      2.85, # U
      1.06, # V
      2.34, # W
      0.20, # X
      2.04, # Y
      0.06  # Z
    ]
# weights are taken from: https://www.sttmedia.com/characterfrequency-english
    c = [0] * 26
    s = [0] * 26

    for i in st:
        x = ord(i) - 65
        if 0 <= x < 26:
            c[x] += 1


    for off in range(26):
        for i in range(26):
            s[off] += c[i] * weight[(i + off) % 26]

    return s.index(max(s))

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 10000))
clientsocket.send('GET'.encode())
data = clientsocket.recv(1024).decode()

st = re.split("\n", data)
rets = ""
for i in range(1,4):
    print(st[i])
    rets += caesar(st[i], crack_caesar(st[i])) + "\n"

print(rets)
clientsocket.send(rets.encode())
data = clientsocket.recv(1024).decode()
print(data)
```
