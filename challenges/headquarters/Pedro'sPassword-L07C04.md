# 🗝 Pedro's Password - L07 C04

Agent 707, we've had access to a server used by one of the Chiquitoos' side businesses for a while and have an idea that one of the gang members, Pedro, might have moved his user account from an old version of Linux. SSH in and see if you can find his hashed password.

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.
These are the details you'll need:

**Username:** [given username] **Password:** [given password] **IP Address:** [given ip] **Port:** [given port]

**Tip:** The flag is in the same file as the password.

```txt
💡 Hint: Older versions of Linux kept hashed passwords in a file that every user account could access. You can print the contents of a file to the screen using the cat tool. Type $ man cat in the terminal to find out more.
```

## Step by Step

- Enter your command promp by running **Windows Key + R** and typing **"cmd"** or terminal on Linux
- Type `ssh [username]@[ip] -p [port number]`
- Type the given password in
- Run `cd /etc`
- Run `cat passwd`
- The flag should come up as the `first line in passwd`
