# 💫 Code Attack - L09 C10

We need your programming skills Agent 707, and from what you've demonstrated so far we think you're definitely up for the challenge.

You need to write a simple script from scratch to crack into another program that takes an argument (a 4 digit numerical pin code) and outputs a result.

**Tip:** If you enter the right argument into the program you get the flag.

```
💡 Hint: You will need to write a script for this one, or you'll be at it for a very long time.
   You can use Python, or it may be even easier to use a BASH script.
   Your script will need to include at least one loop to make this work. If you're using BASH you might consider a while loop.
```

## Files

- [program-x86](/assets/codeattack1)

## Step by Step

- Download the file
- Run `chmod +x [filename]`
- Run `python -c 'for i in range(9999): print(str(i).zfill(3))' | xargs -I {} [filename] "{}"
`
- This will print all 4 digit combinations in a format like this ..., 0012, 0013 ... using python and redirect the ouput of each line to the program as a password
- The flag will appear once the correct pin was found, press `ctr+c` when that happens to make it easier to copy

`flag: 8YBqF1vjnplFDCRomom`
