# 🚘 File Found - L05 C06

Whilst monitoring one of the gang, Ryosuke, we came across a file that he posted online. The problem is, the file doesn't seem to be opening. Take a look and see if you can work it out.

**Tip:** The flag is in the file.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Need help figuring out why the file won't open? Try going to the terminal and typing `$ man file`.
```

</details>

<details><summary>

## Step by Step</summary>

- Using a Linux terminal, navigate to the file’s location in the correct directory using `cd path/to/file`
- Run `file filename.xml` to give you the file information

![image of file output](/assets/filefound1.png)

- The file is actually a jpeg image.
- Change the file type by renaming the file to .jpeg and open it

![image of flag image.. with no flag](/assets/filefound2.jpeg)

</details>
