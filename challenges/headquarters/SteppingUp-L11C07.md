# 📈 Stepping Up - L11 C07

Finally, some good news! We've had an agent undercover with the Bulldogs for a while now, but the gang is quite large and it's very hard to get access to the elite group that are planning to rob the bank. However, we've just received word from our counterparts in Spain that they've arrested one of that elite group whilst he was on a trip there. He was their best hacker and now they need to replace him quickly otherwise their attack on the bank won't work.

The elite group have decided to select someone from the rest of the gang by issuing them with a hacking challenge. Whoever cracks it first gets to go with them on the robbery. If we could get our undercover agent into that group we'd almost certainly be able to disrupt their plans. The challenge is tough - there's a file and you need to overwrite the buffer to make the secret variable read: de4dc0de. Do you think you can be the first to break it?

**Tip:** Overflow the buffer to get the flag.

```txt
💡 Hint: You will need to consider how to make the secret read "de4dc0de".
   It can be written in hexadecimal form with "\x" prefixes; for example "\xde\x4d" and so on.
   Can you fill the buffer with the hexadecimal notation of "de4dc0de"? What does the secret read when you do?
   You may need to look up the difference between Little Endian and Big Endian notation.
```

## Files

- [program-x86](/assets/steppingup1)

## Step by Step

- Download the program and navigate to its location within the terminal.
- Run `chmod +x filename`
- Run .`/filename $(printf "aaaaaaaaaaaaaaaa1\xde\xc0\x4d\xde")`
  - You’ll notice if you try to run the code in the right seeming order, the `c0` and `4d` get swapped.

`flag: IilDCuiVBmySueH37tB`
