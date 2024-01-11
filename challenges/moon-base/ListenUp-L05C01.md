# 🦻 Listen Up - L05 C01

The aliens seem to be trying to make direct contact, so it's time for us to properly listen. We need you to write a server that accepts incoming connections and monitors the commands sent to it.

Some instructions for you:

- Write a server that listens on localhost at port 10000.
- Write the data you receive to /tmp/aliensignallog.txt.

**Tip:** Listen correctly to get the flag.

> 💡 Hint: You'll need to brush up on your sockets and files for this one.
>
> Why not try Level 3 Challenges 1 and 2 again?

## Answer

```python
#
# The aliens seem to be trying to make direct contact, so it's time
# for us to properly listen.
# Write a server that listens on ('localhost', 10000).
# The flag will be sent to that address.
# Record signal to /tmp/aliensignallog.txt
#
# If you get an address already in use error then try again in a few
# moments.
#
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 10000))
serversocket.listen(10)

while True:
  connection, address = serversocket.accept()
  data = connection.recv(1024).decode()
  if len(data) > 0:
    with open('/tmp/aliensignallog.txt', 'w') as rec:
      rec.write(data)
      connection.close()
    break

serversocket.close()
```
