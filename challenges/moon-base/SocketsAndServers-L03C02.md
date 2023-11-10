# 🔌 Sockets And Servers - L03 C02

So Agent 707, now the Moon Base is on high alert it's time to start teaching you some slightly more challenging topics. You'll need them to help the other CPA agents deal with whatever is sending us those strange signals!

Let's start with sockets, a way of sending data over a network.

```
💡 Hint: Don't forget to print the data you receive, or save it to a variable and print that.
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
