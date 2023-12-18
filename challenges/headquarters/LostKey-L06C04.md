# 🔑 Lost Key - L06 C04

Our agent on the ground noticed a USB key discarded outside The Yakoottees' garage and he's just uploaded the files for analysis. It's probably nothing important; they just look like innocent jpg files. One looks corrupt, however. Can you take a look just to be sure we don't miss anything?

**Tip:** The flag is in the file.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Are you sure it's a Jpeg?
```

</details>

## Files

- [file.jpg](/assets/lostkey2.jpg)

<details><summary>

## Step by Step</summary>

- Download the file and open up a Linux terminal
- Use `cd` to change to the directory where the file is located
- Run `file filename.jpg`
![running the file command](/assets/lostkey1.png)
- The actual file is a pdf, change the file extension to .pdf
- The flag is in the pdf

</details>
