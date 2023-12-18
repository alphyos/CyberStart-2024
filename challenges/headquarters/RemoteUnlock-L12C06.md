# 🔓 Remote Unlock - L12 C06

Agent 707, it seems the robot the gang want to send to the bank will first need to undergo a series of tests which we are hoping will reveal more information about how they will activate the robot once it arrives at the bank.

They seem to be testing it with a server (which we've pointed services.cyberprotection.agency at, port 9999), which has a service running on it. When you connect it starts a timer and gives you three numbers. We think to unlock it you need to multiply the first two numbers together and then divide the result by the third number. But the integer result has to be sent to the server in under 1 second to gain access to the remote package. We haven't been able to find a way to do it. Can you?

**Tip:** Send the right answer in time to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Who could possibly answer this question fast enough? Only a computer, probably.
   You should definitely think about programming this one. It shouldn't be too many lines of code in Python.
   Look up socket programming in particular.
```

</details>

<details><summary>

## Step by Step</summary>

- Write a program which does the following

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initialize client
client.connect(("services.cyberprotection.agency", 9999)) # Connect

data = client.recv(1024) # Recv data

data = data.decode("utf-8") # Decode data
data = data.split("\n") # Split at newline

#Math
int1 = int(data[0]) * int(data[1])
int2 = int1 / int(data[2])

# Send back data
client.send(str(int(int2)).encode())
data = client.recv(1024)
print(data.decode("utf-8"))
```

`flag: 917035HrQ0PODo#`

</details>
