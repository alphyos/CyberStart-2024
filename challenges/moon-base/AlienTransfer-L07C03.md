# 👽 Alien Transfer - L07 C03

We've noticed that the aliens are sending messages between their ships, we think they're using XOR to encrypt the messages, and we've intercepted a key.

Set up a server listening on localhost, port 10000, to intercept one of the alien messages. When you do, perform a bitwise XOR on the message with the key "attackthehumans" and then respond with the encrypted data.

**Tip:** Read the response to get the flag.

> 💡 Hint: You'll need to write your own Python function to perform a bitwise XOR of strings.  Python doesn't have one by default. If you're really stuck, see if anyone online has made one before (hint, they have)

## Answer

```python
#
# Setup server listening on ('localhost', 10000)
# receive data then send data back after XORing with the key
# attackthehumans
#
# If you get an address already in use error then try again in a few
# moments.
#

import socket

def bxor(ba1, ba2):
  return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

host = 'localhost'
port = 10000

key = 'attackthehumans'.encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen(5)

while True:
  conn, addr = s.accept()
  data = conn.recv(1024)
  xor_data = bxor(data, key)
  conn.send(xor_data)
  data = conn.recv(1024)
  print(data)
  conn.close()
  break


def debugMsg(msg):
  # Use this function if you need any debug messages
  with open("/tmp/userdebug.log", "a") as myfile:
  myfile.write(msg + "\\n")
```
