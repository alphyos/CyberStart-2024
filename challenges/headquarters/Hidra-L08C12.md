﻿# 🚀 Hidra - L08 C12

Well, this is interesting. We've finally been able to get access to a messaging app (called Hidra) that The Chiquitoo gang is using to communicate. Within an hour of looking at the messages, they've already given us some great intel.

For example, FTP login details to the gang's main server! One small issue: they mention the address and the username but not the password. See if you can find a way in.

**Tip:** Find the password for the user account. The flag is in a file which you get from connecting to the FTP server via a PASV connection. If you are inside the VM, you can use ftp -p.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: You might want to consider using a tool to crack the FTP login. It will need a wordlist; one has been provided in your email.

</details>

## Files

- [words.txt](/assets/hidra3.txt)

<details><summary>

## Step by Step</summary>

- Download the word list from the email attachment in the email tab
- Open up a Linux terminal
- Run `hydra -l secure_user -P words.txt services.cyberprotection.agency -s 2121 ftp`
  - The password should show up

    ![hydra command](/assets/hidra1.png)

- Run `ftp -p services.cyberprotection.agency 2121`
- Enter `mutineers` as the password

  ![fpt command](/assets/hidra2.png)

- Run `get Flag.txt`
- A file called `Flag.txt` should show up on your machine, the flag is inside

</details>
