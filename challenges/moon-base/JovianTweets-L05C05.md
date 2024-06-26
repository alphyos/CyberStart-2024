# 🐦 Jovian Tweets - L05 C05

This is a bit weird, but looking at the files the aliens are sending would suggest they are trying to find a way to post messages on social media back on Earth. Maybe it's part of a coordinated attack to spread panic. We better figure out how they are doing it, and the best way is probably to try it yourself using the protocols they seem to be using.

Some instructions:

- Write a script that uses a web API to create a social media post.
- There is a Tweet Bot API listening at http://127.0.0.1:8082. If you perform a GET method request to that URL it will return basic info about the API.
- To create the social media post, send a POST method request to the API, with a header containing x-api-key:tweetbotkeyv1 and querystring data containing user=tweetbotuser and status-update=alientest.

**Tip:** Read the response to get the flag.

> 💡 Hint: You need to send a POST request here with a custom header.  You can use urllib.request for this one and remember - it's OK to Google for coding help!

## Answer

```python
import urllib.request, urllib.parse, urllib.error

data = urllib.parse.urlencode({"user":"tweetbotuser","status-update":"alientest"})
data = data.encode("ascii")
url = "http://127.0.0.1:8082"

req = urllib.request.Request(url, headers={"x-api-key":"tweetbotkeyv1"}, data=data)

response = urllib.request.urlopen(req)
print(response.read())
```
