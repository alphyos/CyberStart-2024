# 💂‍♀️ File Hunt - L09 C09

Agent 707, we have SSH access to one of the gang's servers that contains lots of files and we need to find one in particular.

One of the gang, Stanislav, created the file on 22 Nov 2015 at 8.00pm (we know because we were monitoring him!). Can you find that particular file, we think it contains important information concerning the whereabouts of several gang members.

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

**Time Left:** 60 minutes

These are the details you'll need:

**Username:** [given username] **Password:** [given password] **IP Address:** [given ip] **Port:** [given port]

**Tip:** Find the file, it contains the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: One of the other agents mentioned you should perhaps try using the "find" command for this,
   you can view more information with "man find".
```

</details>

<details><summary>

## Step by Step</summary>

- Enter your command prompt by running **Windows Key + R** and typing **cmd** Or terminal on Linux
- Type `ssh [username]@[ip] -p [port number]`
- Type the given password in
- Run `find / -type f -newermt 2015-11-22 ! -newermt 2015-11-23`
  - All of the entries should show as having a "find:" prefix with denials except for one entry, `/etc/protocol`
- Run `cat /etc/protocol`
- The flag should appear

`flag: 5iF4fG0vnsRHEdGfzMLSvXyQ`

</details>
