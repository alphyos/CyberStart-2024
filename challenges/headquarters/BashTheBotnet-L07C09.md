# 🔨 Bash The Botnet - L07 C09

We have managed to gain access to a server used by one of The Chiquittoos' side businesses. We think the gang use it to connect to their botnet, which we want to take down. The botnet is of course password protected but, if you can find the password we can log in and disable it!

Log into the server using these credentials and see if you can find the password.
SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

Time Left: 60 minutes

These are the details you'll need:

Username: [given username] Password: [given password] IP Address: [given ip] Port: [given port]

**Tip:** The flag is in the same file as the password.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: If the gang uses the terminal to connect to their botnet, they may have typed the password in there. Maybe look in the Linux command history?

</details>

<details><summary>

## Step by Step</summary>

- Open up a Linux terminal
- Type `ssh [username]@[ip] -p [port number]`
- Type the given password in
- Run `ls -la`
- Run `cat .bash_history`
- The flag should appear

![sending message](/assets/bashthebotnet1.png)

</details>
