# 📝 Text and Text - L10 C03

Agent 707, yesterday one of our field agents was able to snoop on a meeting between several gang members planning out their attack on the weapons facility.

One of them mentioned to the other that he'd send over the lock code to one of the doors on the facility. If we knew the code, we'd know how they got it (because the codes are only given to certain people) and where exactly on the facility they planned to get access.

Well, this morning we intercepted an email between the two expecting to see the code, but instead they just sent over two large text files. Weird. Can you find the code?

**Tip:** Find the code, that's the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Investigate a way to identify changes between two files.

</details>

## Files

- [locks](/assets/textandtext2)
- [locks_old](/assets/textandtext3)

<details><summary>

## Step by Step</summary>

- Download both files
- Run `diff [file1] [file2]` to get the difference between the files
- The flag is the only change that was made (the part after `<`)

![image showing the difference](/assets/textandtext1.jpg)

`flag: NCE54L8D`

</details>
