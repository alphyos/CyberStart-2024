# 🤷‍♂️ Encrypted - L13 C09

Good news Agent 707, another intercepted file for you to analyze that we think contains the access code to a safe the gang have on their boat - our undercover agent thinks he can get physical access to it, so we need the code as soon as possible.

We've tried executing the file and it loads the encrypted access code into memory. That's as far as we've got, give it a try and see if you can decrypt the code.

**Tip:** strings, gdb, try to catch a break.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Very stupid encryption method

</details>

## Files

- [program-x86](/assets/encrypted1)

<details><summary>

## Step by Step</summary>

- Download the program and run `strings filename`
- There is a suspicious line that has been encoded
  - `swi&CNJCtPVbCyyAmNG8PqFZsYpyXegEQRGt`

```python
a = "03 09 0e 02 09 08 0b 15 13 03 01 02 05 05"
m = [int(x, 16) for x in a.split()]
s = "swi&CNJCtPVbCyyAmNG8PqFZsYpyXegEQRGt"
print([s[i] for i in m], end='')
```

- Running it through this decryption method will produce the flag
- each hex value in `a` can be found by disassembling the main function of the binary (in gdb)

`flag: &PyiPtbq8&wiNN`

</details>
