﻿# 🛥 Port Service - L08 C02

Recruit, another interesting one for you.

We found a service running on one of The Chiquitoos servers at services.cyberprotection.agency on port 5737. We're not entirely sure what it does but we think we should check it out. We know that it somehow grants a code but it's hidden in so much text that we can't find it. Can you see if you can find it?

**Tip:** Find the code, it's the flag!

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Netcat output can't be sent to a text file as normal. You will need to output both stdout and stderr to the text file in order to get the output of the connection written to a file.

</details>

<details><summary>

## Step by Step</summary>

- Open up a Linux terminal an run `netcat services.cyberprotection.agency 5737 | grep -i flag`
- This will match all of the received text against the string `flag` ignoring case
- The output will contain the flag

![result of grep](/assets/portservice1.png)

</details>
