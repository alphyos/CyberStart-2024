﻿# 📜 Encrypted - L08 C05

Quick extra project for you, recruit.

We have managed to gain access to a server, which is running The Chiquitoo gang's secure encryption service. We need the password they are using as the encryption key. Can you find out what it is for me?

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

These are the details you'll need:

Username: [given username] Password: [given password] IP Address: [given ip] Port: [given port]

**Tip:** The flag is the password.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The history file has been wiped this time but there may be another solution. How would you go about looking at all the processes that are running on a Linux system? Is there a way to get more detail about them all?

</details>

<details><summary>

## Step by Step</summary>

- Enter your terminal
- Type `ssh [username]@[ip] -p [port number]`
- Type the given password in
- Run `ps -aux | grep -i flag`
- The flag should show up

![demo](/assets/encrypted1.jpg)

</details>
