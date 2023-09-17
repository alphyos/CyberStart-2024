# 🧾 Recibo - L01 C05

Agent 707, we think the employee in question has been using the digital receipts from the restaurant to move information out to a conspirator. Can you figure out which of these has been **tampered with**?

**Tip:** Find the receipt that's been tampered with, the flag will **prove** it has been **changed**.

```
💡 Hint: Typically a file is hashed when collected as evidence so that if it is tampered with later it is easy to prove that
   the file has changed. When a file is changed, even by a single byte, the mathematical hashing value also changes, identify
   this new value and enter as a flag.
```

## Step by Step

- Download all of the files on a Linux machine.
- Go to the terminal and run “`md5sum filename`" on each image.
- Compare the results with the text found in `MD5s.txt`.
- Only the 4th recibo has a different md5sum than what is on the text file.

![picture of the terminal output](/assets/recibo1.jpg)

- The flag is the md5sum result.
