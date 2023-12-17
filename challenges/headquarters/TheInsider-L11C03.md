# 🚪 The Insider - L11 C03

One of the other agents needs your help. He's been trying to open a file we intercepted which we believe might have special insider information about the bank the Bulldogs are targeting. The agent thought opening the file was going to be simple, but it's not working. Can you help?

**Tip:** Get the password and open the file to get the flag.

```txt
💡 Hint: Take a look at man strings. Can you think of a reason that the string may not show up using the default settings?
   It may be that you have to use some custom settings with strings.
```

## Files

- [program-x86](/assets/theinsider2)

## Step by Step

- Download the file and run `cat filename`

![cat command](/assets/theinsider1.png)

- The password is `Reck1t`, make sure to do the following
  - `sudo chmod +x filename`
  - `./filename`
- Typing the password when it is prompted should produce the flag

`flag: hvMjw1CLRDcZZzTqO2k`
