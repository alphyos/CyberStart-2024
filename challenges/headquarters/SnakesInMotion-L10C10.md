# 🐍 Snakes in Motion - L10 C10

Agents have intercepted some vital information we'd like you to look at. We've sent you an email with some encrypted text, a dictionary file and a Python script to help you extract what we believe might be the password to a cloud storage solution the Spetzners use to store their criminal documents. One problem, unfortunately, the Python script is incomplete.

Can you finish it off so that it runs each line in the dictionary against the encrypted text to decrypt it? Hurry agent, the Spetzners might know we are on to them and could transfer their documents elsewhere!

**Tip:** Decrypt the text, that's the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: You will need to open the dictionary file, loop through each line, save the text in the code and run the decryption for each line. We know you can do it Agent 707!

</details>

## Files

- [dict.py](/assets/snakesinmotion1.py)
- [words.txt](/assets/snakesinmotion2.txt)

<details><summary>

## Step by Step</summary>

- Download the files
- Modify the code in the python file to match the following

```python
# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "uqX82PBZ8pi1fvt4GLHYgLs50ht8OQlrR1KHL2teppQ=" # changed

def decode_aes(c, e):
  return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

# removed secret = "password"

with open('words.txt', 'r', encoding='utf-8') as f: # added
  words = f.read().splitlines() # added
  for secret in words: # added
    if secret[-1:] == "\n":
    print("Error, new line character at the end of the string. This will not match!")
    elif len(secret.encode('utf-8')) >= 32:
    print("Error, string too long. Must be less than 32 bytes.")
    else:
    # create a cipher object using the secret
    cipher = AES.new(secret.encode('utf-8') + (BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING.encode(), AES.MODE_ECB) # changed
    # decode the encoded string
    decoded = decode_aes(cipher, encrypted)

    if decoded.startswith('FLAG:'):
      print("\n")
      print("Success: "+secret+"\n")
      print(decoded+"\n")
      break # added
    else:
      print('Wrong password')
```

- Run the script and make sure to change `words.txt` to the actual file name of the word list
- This should find the correct password `Serenity` and spit out the decrypted text which is the flag

`flag: ozZdCrFTsOMoC4m5FMd`

</details>
