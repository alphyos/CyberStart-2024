﻿# 🌵 Still Hiding - L06 C11

Were you involved in the previous level when we needed someone to SSH into one of the Yakoottees' servers and take a look around? Well, we need to do it again. It seems they're becoming a little smarter about hiding their files. Take a look and see what you can find.

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

These are the details you'll need:
Username: [given username] Password: [given password] IP Address: [given ip] Port: [given port]

**Tip:** The flag is in a file somewhere on the server.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: There is a directory here that has been hidden in plain sight. Try comparing the output of $ ls with the output of $ ls in a different directory.

</details>

<details><summary>

## Step by Step</summary>

- Open up a Linux terminal
- Type `ssh [username]@[ip] -p [port number]`
- Type the given password in
- Run `cd ...`
- Run `ls`
- Run `cat camouflage`, the flag should appear

![picture of commands](/assets/stillhiding1.png)

</details>
