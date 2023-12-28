# 💻 Corrupted Corruption - L08 C11

Agent 707, there's another quick task I need your help with. One of the agents intercepted a zip file from The Chiquitoos, but it looks like it's corrupted. I know you've helped us with this kind of thing before. Can you take a look and see if you can get it working?

**Tip:** Open the file to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Within most file types there is a header which is a sequence of bytes near the start of the file. It helps act as a signature to identify the type of data contained within the rest of the file. The file header is also sometimes known as the "magic bytes" of a file. Search online for this, or "hex headers" to find out more and try adding those bytes back into the zip file.

</details>

## Files

- [masterkey-x86](/assets/corruptedcorruption2.zip)

<details><summary>

## Step by Step</summary>

- Download the zip file on a Linux System
- Use a hex editor such as HxD or [hexed.it](https://hexed.it/) to prepend bytes to the start of the zip file
  - If you are using hexed.it, copy the bytes and paste them at the very beginning of the file while specifying insert data
![image of the file in hexed.it](/assets/corruptedcorruption1.png)  
- Add the bytes `50 4B 03 04`
  - Make sure to **ADD** the bytes back in at the beginning, not replacing any existing bytes
- The zip file should now extract and open properly
- There is a program in the extracted zip, run `sudo chmod +x filename`
- Run it using `./filename` in the terminal
- The flag should show up after some time

</details>
