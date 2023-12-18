# 🏉 Catch and Throw - L12 C10

Agent 707, we've just stumbled on something we think could be very important. We know the gang have been working on getting their trojan horse robot into the bank, and we also know they're trying to communicate with it and use it to get access to the banks servers from the inside. But until now we didn't know if they had the codes they'd need once they'd made the connection. Well, it seems they might.

We've received an anonymous tip from one disgruntled gang member about two web pages, the second of which he claims, has a list of access codes the gang would need to get in. If we could see those codes we'd know whether the risk was real, but here's the thing - on the first web page there's just a number which keeps changing. On the second page, nothing, except for an error message. We think to open up access to the second page you need to pass the value from the first page to the cookie on the second page. Give it a try.

**Tip:** Change the value of the cookie on the second page correctly to show the codes. The last code is the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: You'll need to automate this to be fast enough. You can use CURL to send cookie values.
```

</details>

<details><summary>

## Step by Step</summary>

- Copy the code down below and run it to get the flag

```python
import requests
from bs4 import BeautifulSoup

# Make request
resp = requests.get('https://bulldoghax.com/secret/spinner')
# Read request and get body contents
body = str(resp.content)

# Use bs4 to parse through the html code
soup = BeautifulSoup(body, "html.parser")
# Get the value of the cookie to put into the second page
cookie = soup.find("div", class_="number").text

# Make request to second page with cookie
cookies = {"timelock" : cookie}
resp = requests.post('https://bulldoghax.com/secret/codes', cookies=cookies)
print(resp.content)
```

`flag: 7463547834`

</details>
