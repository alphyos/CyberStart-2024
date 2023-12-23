# 🔑 Unlocking the Message - L04 C04

Agent 707, we're using a simple web API to listen for the alien signals, but we need to find a way to get past a numerical API key that's required to get a response. See if you can manage it.

Some instructions:

We're listening at http://127.0.0.1:8082
You need to send an HTTP GET request with the correct x-api-key header.
We have narrowed down the key to be in the range of 5500 to 5600
**Tip:** Write a script which runs each possible combination until you get a response to get the flag.

> 💡 Hint: Try a google search on sending a custom header with urllib.request.

## Answer

```python
#
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout. If this occurs try narrowing
# down your search
#

import urllib.request, urllib.parse, urllib.error

for i in range(5500, 5601):
  req = urllib.request.Request("http://127.0.0.1:8082", headers={"x-api-key": str(i)})
  resp = urllib.request.urlopen(req)
  print(resp.read())
```
