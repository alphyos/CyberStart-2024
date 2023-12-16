# 📏 Bogdan’s Data - L09 C08

Agent 707, a possible breakthrough that we need your help with. We've found a server run by the gang, it's at services.cyberprotection.agency:3166 and it seems to be protecting some data. The gang member who we think administers it, Bogdan, is one of the key members behind the plans to steal the EMP. We think it might have even been his suggestion in the first place. In short, we need access to the data on that server.

Fortunately we've been able to recover some source code for it. Take a look at the source code and see if you can get access to the server.

**Tip:** Get access to the server to get the flag.

```
💡 Hint: Looking at the source code, what does eval() do? What are the requirements for getting the flag,
   can you make the if statement true without knowing the value of firstNum?
```

## Step by Step

- Examine the source code given, specifically look at the `if` conditional.

```c
clientsock.send("Welcome to Maths_Server 1.0\n")

try:
    clientsock.send("Enter the first number, so I can EVALuate it:\n")
    firstNum = eval(clientsock.recv(1024))
    firstNum = firstNum + firstNum + ord(flag[4]) + ord(flag[8]) + ord(flag[5])
    clientsock.send("Enter the second number, so I can EVALuate it:\n")
    secondNum = eval(clientsock.recv(1024))
    if secondNum == firstNum:
        clientsock.send("The flag is: " + flag + "\n")
        firstNum = 0
        secondNum = 0
except:
    pass

clientsock.close()
```

- Open a Linux terminal.
- Run “`netcat services.cyberprotection.agency 3166`”
- Type any number and press enter.
- Type “`firstNum`" and press enter.
- The flag should appear.
- This works because pythons built-in `eval` function parses the input string and compiles it to bytecode which is then evaluated as a python expression and returned by the function. that means it will return the value of `firstNum` and trigger the `if secondNum == firstNum:`.

![terminal example](/assets/bogdansdata1.png)

`flag: ROCTrOPlAclukelAShuENWaCEleCTO`
