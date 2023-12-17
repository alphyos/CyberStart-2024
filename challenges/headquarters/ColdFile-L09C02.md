# ⛄ Cold File - L09 C02

Agent, quick task for you if you have a few minutes to spare. We have an old program one of our previous agents used that we can't get into. Can you get into it for me?

**Tip:** Run the program, find the password, input it into the program to get the flag.

```txt
💡 Hint: Agent, you may want to look into using a tool called 'Strings', it's built into most Linux systems.
   Learn more by typing "man strings" in your terminal window.
```

## Files

- [program-x86](/assets/coldfile1)

## Step by Step

- Download the program in a Linux system and open terminal.
- Navigate to the file location and run `chmod +x filename.exe`
- Run `strings filename.exe`
- The password is in the strings: `Sh3n4n1g4ns`
- Run `./filename.exe`
- Enter the password, you will get the flag in return

`flag: HQJmCZf3ol6mOdxakBz`
