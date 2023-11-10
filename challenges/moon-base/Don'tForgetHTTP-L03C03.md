# 🎖️ Don't Forget HTTP - L03 C03

Sockets aren't the only way to make network connections you know, you can use Python to make HTTP requests easily as well. Time to have a go at that I think.

```
💡 Hint: This one is easy as long as you remember to use .read() on the response. See if you can re-use any of the example code.
```

## Answer

```python
import urllib.request, urllib.error, urllib.parse

# CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
#              the response.
response = urllib.request.urlopen("http://127.0.0.1:8080/winning")
html = response.read()
print(html)
```
