# 〰 New Line Of Communication - L08 C01
When you were on the last level we discovered the aliens had been communicating with a human insider back on Earth, and by email of all things! Well, it seems that may have been a bit of a decoy as they're also exchanging secret encrypted messages from a server on one of the probe ships.

We need you to write a script which can connect over TCP to the following server ("localhost", 10000) and send 'GET' to retrieve the encrypted messages. You then need to decrypt them and send them back split by \n. We think you'll receive 3 sentences and they're encrypted with a caesar cipher that has a different random offset per sentence.

Finally, print the response after sending the decrypted messages to get the flag.

**Tip:** Remember, each encrypted message has a different random offset.

```
💡 Hint: You can only send the correct text back so you'll need some way to determine which is a real sentence.

   Try a search on letter goodness
```

## Answer

```python
#
# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#

import socket
import string

letters = 'abcdefghijklmnopqrstuvwxyz'

letterGoodness = dict(zip(string.ascii_uppercase,
                        [.0817,.0149,.0278,.0425,.1270,.0223,.0202,
                         .0609,.0697,.0015,.0077,.0402,.0241,.0675,
                         .0751,.0193,.0009,.0599,.0633,.0906,.0276,
                         .0098,.0236,.0015,.0197,.0007]))

trans_tables = [ str.maketrans(string.ascii_uppercase,
                 string.ascii_uppercase[i:]+string.ascii_uppercase[:i])
                 for i in range(26)]

def sendData(data, s):
  s.send(data.encode())
  
  hasReq = False
  while not hasReq:
    data = s.recv(1024)
    hasReq = True
  
  return data

def goodness(msg):
    return sum(letterGoodness.get(char, 0) for char in msg)

def all_shifts(msg):
    msg = msg.upper()
    for trans_table in trans_tables:
        txt = msg.translate(trans_table)
        yield goodness(txt), txt
  
host = 'localhost'
port = 10000

dataList = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((host, port))
  
  s.send('GET'.encode())
  
  data = s.recv(1024)
  
  data = str(data).strip('b').strip('\'')
  strings = data.split('\\n')
  
  strings.pop(0)
  for i in range(len(strings) - 1):
    message = strings[i]
    print('Message ' + str(i + 1) + '\n' + message + '\n========================================')
    print(max(all_shifts(message)))

    decoded = max(all_shifts(message))[1]
    print('Decoded: ' + decoded)

    print('\n')
    
    dataList = dataList + decoded + '\n'
    
  print(dataList)
  data = sendData(dataList, s)
  print(data)
```
