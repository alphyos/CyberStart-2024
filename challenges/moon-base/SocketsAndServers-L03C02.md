# 🔌 Sockets And Servers - L03 C02

```
💡 Hint:
```

## Answer

```python
import socket

# CHALLENGE 1: Write a TCP Client that will connect to 127.0.0.1 on
#              port 9990.
#              Your client must send "Knock, knock" to the server.
#              Then get the response, and print it out.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 9990))
clientsocket.send('Knock, knock'.encode())
data = clientsocket.recv(1024)
print(data)
```
