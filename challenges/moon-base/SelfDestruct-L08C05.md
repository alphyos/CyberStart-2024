# 🤯 Self Destruct - L08 C05

Ok agent, one more challenge for you to finally defeat these aliens. We now have access to the core part of the alien mothership and have figured out how to set the ship to self-destruct. The only way the aliens can turn off the self-destruct is to get a million miles away from Earth, so if you can do this we think they'll be in a hurry to leave!

You need to write a script which makes HTTP requests to the server http://127.0.0.1:8082/selfdestruct. That site randomly generates two numbers with a small chance of the numbers matching. To turn on the self-destruct you need to make those two numbers match!

**Tip:** Make the numbers match and read the response, that's the flag!

> 💡 Hint: First make the connection and view the HTML response.
>
> Is there something you could match against so that you know it has failed?
>
> Match against it, and as soon as that string doesn't appear in the response, print out the HTML.

## Answer

```python
#
# Write a script that makes HTTP requests to the server
# http://127.0.0.1:8082/selfdestruct until the numbers match
# and read the response to get the flag.
# You can easily run out of execution time in this challenge.
# You will need to check the response and stop your attack
# once you see the flag.
#

import urllib.request

url = "http://127.0.0.1:8082/selfdestruct"
yes = True

while yes:
  req = urllib.request.urlopen(url)
  resp = req.read().decode()

  list = resp.split("\n")

  if list[21] == list[24]:
  print(resp)
  yes = False
```
