# 🛑 Junya Who? - L06 C08

Recruit, I need a favour. We've just had some intel about one of the gang members. His first name is Junya, but we can't find his surname. We know we have it on record, but it could be in any one of a huge set of files. Perhaps you could SSH into our server and see if you can find his surname for me?

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

These are the details you'll need:

Username: [given username] Password: [given password] IP Address: [given ip] Port: [given port]

**Tip:** Find "Junya" mentioned in the files and his surname will follow. That's the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: You may want to look at the grep tool. Type $ man grep in the terminal to see how to use it.

</details>

<details><summary>

## Step by Step</summary>

- Open up a Linux terminal
- Type `ssh [username]@[ip] -p [port number]`
- Type the given password in
- Run `ch /etc`
- Run `cat passwd`
- The flag should come up as the `first line in passwd`

</details>
