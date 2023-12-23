# 🛫 Start Line Setback - L05 C01

Well, that wasn't a promising start. On our very first review, we found an image file on one of the company's servers which doesn't look quite right. We think whoever left it there has used a tool to add a passphrase to it and hide something inside. Take a look and see what you think.

**Tip:** Open the file to find the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: You need to identify the passphrase and use it to extract the hidden file.
   Can you think of any tools to find the passphrase within a file?
```

</details>

## Files

- [runner.jpg](/assets/startlinesetback1.jpg)

<details><summary>

## Step by Step</summary>

- Download the image
- Run `strings filename`

[output](/assets/startlinesetback2.jpg)

- The last line tells you the password for steghide is `givemetheflag`
- Use `steghide --extract -sf filename` and enter the password
- The extracted file `flag.txt` contains the flag

`flag: QQPhgns98&"!`

</details>
