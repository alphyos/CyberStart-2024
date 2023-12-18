# 🎎 Matryoshka - L10 C05

Agent 707, know anything about man pages?

Log into this SSH server using the details below. We've received word that the gang has been using this public server to pass messages through the use of man pages. We need to see if they've used a particular code word (matryoshka) which they're using to say when to start implementing their plan. See if you can find it.

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

**Time Left:** 60 minutes

These are the details you'll need:

**Username:** [given username] **Password:** [given password] **IP Address:** [given ip] **Port:** [given port]

**Tip:** Find the code word to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Agent, can you find a way to search the man database?
```

</details>

<details><summary>

## Step by Step</summary>

- Open up a Linux terminal
- Type “`ssh [username]@[ip] -p [port number]`”
- Type the given password in
- Run `man -K "matryoshka"`
- The flag should appear

`flag: 4XAEhDJvZBuine9CCzmzcYmR`

</details>
