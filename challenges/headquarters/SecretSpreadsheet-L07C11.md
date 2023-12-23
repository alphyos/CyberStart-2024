# 🥜 Secret Spreadsheet - L07 C11

Agent 707, we've stumbled upon something. We think it might really help in getting us closer to the Chiquitoos' plan to steal the shipment of Cola. They've created a spreadsheet listing all the containers they intend to target. Luckily for us, they've posted it online for other gang members to see and update. But, of course, being the clever cyber criminals they are, they've put it behind a particularly clever password system.

If you visit the page where it exists the ciphered password is there but it changes every two seconds; too fast for us to decipher and use. One of our engineers has been working on a Python script to try and get around it. Have a look at the script and see if you can make some changes to get it working.

**Tip:** Run the correct script to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The script needs to look at the page, grab the password, reverse it and then feed it back to log in.

</details>

<details><summary>

## Step by Step</summary>

- Download the script and open it up in an editor such as VSCode
- Edit it so the the original response from the page without the code gets reversed and put back into the urls as the code

```python
import urllib.request, urllib.error, urllib.parse

link = "http://www.chiquitooenterprise.com/password"
# Missing a whole chunk of code here!

resp = urllib.request.urlopen(link)
string = resp.read().decode()
revString = string[::-1]

answer = "http://www.chiquitooenterprise.com/password?code=" + revString
response = urllib.request.urlopen(answer)
response = response.read()
print(response.decode('utf-8'))
```

</details>
