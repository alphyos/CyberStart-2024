# 💨 A Way Back In - L06 C03

Agent, we need to start fighting back, and we think we have a way in. See if you can write a script that will start a connection to the below IP address, which we think is what the alien probe ship is using. It will give us the ability to run commands on their machine and see the results. Once in, read the files on the system in the /tmp directory.

**IP:** 127.0.0.1 ,**port:** 10000

**Tip:** The flag will be sent when you send the correct command to the above IP address and port.

> 💡 Hint: Think about what command you could send that would list the files on the filesystem. Remember the file is in the /tmp directory.

## Answer

```python
#
# Write a script that connects to 'localhost' port 10000
# You then need to send a command to list the files in the /tmp directory
#

import socket

host = "localhost"
port = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((host, port))
  s.send(b"ls /tmp")
  data = s.recv(1024)
  s.close()
  
print(data)
```
