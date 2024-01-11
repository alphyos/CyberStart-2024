# 🤐 Vulnerable String - L08 C02

Agent, we're increasing our attack on the probe ship servers. We've identified a server that holds a compressed string, which we think might be some kind of unlock code to the mothership's entry system.

Write a script which can connect to the server localhost:10000 over TCP, and send 'GET_KEY' to download the string. The string is compressed using what we think is a very common form of compression used by many websites on Earth, so you'll need to decompress.

**Tip:** Download, decompress and print the string to get the flag.

> 💡 Hint: The string is compressed with gzip. Perhaps there's a module available that can decompress it?

## Answer

```python
#
# Write a script which can connect to the following server
# 'localhost', 10000 over TCP send 'GET_KEY' to download a string.
# The string is compressed with a common algorithm found in many
# websites. Decompress the string and print it to get the flag.
#

import socket
import gzip

host = 'localhost'
port = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((host, port))
  
  s.send(b'GET_KEY')
  data = s.recv(1024)
  
  with open('/tmp/test.gzip', 'wb') as file:
  file.write(data)
  
  with gzip.open('/tmp/test.gzip', 'rb') as f:
  file_content = f.read()
  
  print(file_content)
```
