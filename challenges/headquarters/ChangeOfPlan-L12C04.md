# 🗺 Change of Plan - L12 C04

Our Agent on the inside has just received an email from one of the senior gang members. We think it's regarding a date being set for when the robot should arrive at the banks address - it's our belief that they know we are into them and so they would like to speed up their efforts in sending the robot to the bank!

We really need to confirm the exact date they want to send it, but at the moment we can't because the email came in the form of some encrypted text. We've had an agent working on it, and he's created a dictionary file and an unfinished Python script to try and crack it. He seems to have hit a dead end, maybe you could pick it up and finish breaking the encryption.

**Tip:** Crack the encryption to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: You'll need to find a way to determine if the output of the text is human readable to check automatically if you got the right answer. Remember, every ASCII character is actually a number.

</details>

## Files

- [code.py](/assets/changeofplan1.py)
- [words.txt](/assets/changeofplan2.txt)

<details><summary>

## Step by Step</summary>

- Download the files
- Modify the python code to match the following
- Make sure to change `words.txt` to the actual name of the wordlist

```python
# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

with open('words.txt', 'r', encoding='utf-8') as f: # added
    words = f.read().splitlines() # added
    for secret in words: # added
        if secret[-1:] == "\n":
            print("Error, new line character at the end of the string. This will not match!")
        elif len(secret.encode('utf-8')) >= 32:
            continue
        else:
            # create a cipher object using the secret
            cipher = AES.new(secret.encode('utf-8') + (BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING.encode(), AES.MODE_ECB) # changed
            # decode the encoded string
            decoded = decode_aes(cipher, encrypted)

            # added
            skip = False
            for c in decoded:
                if (ord(c) < 32 or ord(c) > 126):
                    skip = True
                    break

            if skip == True:
                continue

            if decoded != '':
                print('Decoded: '+decoded)
```

- The decoded string is the flag

`flag: iQmDIXlDT7N2YgReCOM`

</details>
