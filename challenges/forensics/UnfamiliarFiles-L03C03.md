# 📂 Unfamiliar Files - L03 C03

Here's a strange one for you, agent. Our team was able to recover a hard drive owned by one of the hackers and found all kinds of interesting things on it. Unfortunately, some of the files **don't seem to work** and we're not sure what they are. Can you take a look at this one and see if you can figure it out.

**Tip:** Open the file to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Did you know Linux has a built-in file identification command called 'File'?
```

</details>

## Files

- [artwork.exe](/assets/unfamiliarfiles2.exe)

<details><summary>

## Step by Step</summary>

- Download the file on a Linux machine
- Run `file filename`
- Change the extentsion type from .exe to `.png`
- Looking at the image, the flag is in plain text

![artwork.png](/assets/unfamiliarfiles1.png)

`flag: 9enfsu!`

</details>
