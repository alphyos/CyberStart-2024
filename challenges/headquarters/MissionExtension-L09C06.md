# 🛍 Mission Extension - L09 C06

Agent, those Spetzners are really trying to test our patience! We have someone on the inside that managed to quickly take a copy of one of the gang's hard drives. But just to make it really hard to figure out what they're doing they've removed all file extensions - from every file!

We know there's a Jpeg in there somewhere with an image of the particular EMP they're trying to steal, but it's taking the team forever to find it. Can you think of a quicker way?

SSH sessions only last 60 minutes, after that you will need to reload the page to get a new one.

**Time Left:** 47 minutes

These are the details you'll need:

**Username:** [given username] **Password:** [given password] **IP Address:** [given ip] **Port:** [given port]

**Tip:** Find the Jpeg, it contains a serial number (SN), that's the flag!

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Consider using the "file" command to find what file type a file is. See "man file" for more information. How would you find the file type of all the files in the directory? Then following on from that, how would you sort through that information to find the one jpg?

</details>

<details><summary>

## Step by Step</summary>

- Enter your command prompt by running **Windows Key + R** and typing **cmd** Or **terminal** on Linux.
- Type `ssh [username]@[ip] -p [port number]` and login with the given password.
- Run `ls` followed by the command `cd Contents`
- Run `file *` This will list all the files in Contents and what type they are.
- `M5KDAN44` is the name of the jpeg file we are looking for.
- Bring up a separate terminal.
- In the 2nd terminal, run `scp -p [port number] [username]@[ip]:/home/[username]/Contents/M5KDAN44 .`
  - (`.` can be any file path you may choose from but for simplicity, `.` means the file will be directed to the home directory.)
- Open the jpeg file from where it is stored, the image should look like the one below.
- The serial number is `0207F9`.

![serial number in the image](/assets/missionextension1.jpg)

`flag: 0207F9`

</details>
