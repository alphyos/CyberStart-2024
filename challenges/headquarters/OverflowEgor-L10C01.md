# 🧠 Overflow Egor - L10 C01

Right, Agent 707, it's time we tested your skills against the Spetzners finest.

One of their gang, Egor, is a master scientist and skilled programmer. He's written a program which we think is vulnerable to buffer overflow. See if you can crack it.

**Tip:** Overflow the buffer to get the flag.

```txt
💡 Hint: This program is vulnerable to a buffer overflow, the programmer does not check the
   size of the user's input before assigning it to a variable.
   Can you exploit this to overwrite the next memory addresses with your own content?
```

## Step by Step

- Download the file and give it executable permissions with:
  - `$ chmod +x program-x86`
- Running the program gives a prompt to put in a password
- Knowing the goal is to exploit a buffer overflow vulnerability, we try typing a lot of random characters
- This gives a segmentation fault but no flag, this probably means we typed too many characters
- We try again but with less characters
- It works

![buffer overflow in action](/assets/overflowegor1.png)

`flag: AYGtKy5Nbc5RukjAxkB`
