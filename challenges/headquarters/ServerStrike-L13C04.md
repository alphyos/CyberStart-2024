# 🏹 Server Strike - L13 C04

Breakthrough - we have gained access to the gang's primary server! We found out because we recently took down a hacker from a rival gang that has previously managed to gain access to the system.

We think he left an exploit on the server. SSH in and see if you can use it to exploit the server.

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

These are the details you'll need:

**Username:** [given username] **Password:** [given password] **IP Address:** [given ip] **Port:** [given port]

**Tip:** weird.

**Warning:** Make sure to back up any files you are about to modify. There are no second chances!

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Always easier to work on your own machine
```

</details>

<details><summary>

## Step by Step</summary>

- Run the following commands
- `sudo scp -v -P [port] username@ip:/home/a2CJ7rXU8B/.../weird /any/directory/on/your/host/computer`
  - Type the given password in
- `sudo useradd user`
- `su user`
- Navigate to the directory you sent the program file to
  - `chmod +x weird`
  - Run `./weird`
- Running this program should give you the flag

`flag: 6pas0apcxasd7aswzzsapzla`

</details>
