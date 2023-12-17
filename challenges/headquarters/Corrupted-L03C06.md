# 👹 Corrupted - L03 C06

An agent in the field managed to get access to an **XML file** that he believes belonged to one of The Chopper gang members. It looks **corrupted** so he's sent it to us for analysis.

Have a **look in the file** and see if you can get it working.

**Tip:** The flag to complete the challenge is on the last line of the file.

```txt
💡 Hint: Hmm, if you just open the file in your browser it shows an error.
   But maybe you don't need to actually see the output of the XML file.
   Perhaps try looking at the source code by using Developer Tools or right-clicking and
   selecting "View source".
```

## Step by Step

- Download the file and open it
- A website should pop up and right clicking it to view the source code will reveal the flag at the last line of code with the flag between `<flag> </flag>` tags.

![picture of the last line](/assets/corrupted1.png)
