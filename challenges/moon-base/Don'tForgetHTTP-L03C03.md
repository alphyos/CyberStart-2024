# 🎖️ Don't Forget HTTP - L03 C03

```
💡 Hint:
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
