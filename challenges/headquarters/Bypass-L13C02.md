# 🍀 Bypass - L13 C02

Agent 707, we've found a TCP service the gang are using, but we can't seem to get access. It's services.cyberprotection.agency on port 13880 See if you can bypass the login screen and begin exploring.

Tip: Good LUKS

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Googling "LUKS vulnerability" may prove to be useful.
```

</details>

<details><summary>

## Step by Step</summary>

- Run `nc services.cyberprotection.agency 13880`
- **LUKS** has an old exploit where if you enter the password incorrectly **93** times, it will fall back into intramfs mode
- You can use this to gain a root level shell on a machine
- Enter the password **incorrectly 93 times** (just enter is enough), then you can use the command `flag` to get the flag

![after bypassing the password](/assets/bypass1.png)

`flag: ZhSX9onhPC7y1LTqhE`

</details>
