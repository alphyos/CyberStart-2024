# 🧭 Lost But Not Forgotten - L04 C10

We've recovered a bunch of .gif files from an old hard drive one of the gang members threw out. We thought they were innocent enough until we started wondering whether they were all actually GIF files.

Check your email, download the files and see if you can find out what's going on.

**Tip:** The flag is in one of the files.

```txt
💡 Hint: Can we be sure they're all really .gif files? In previous cases the CPA have solved we've seen gang members change
   the extension on files so it looks like something different. Perhaps try opening the files in a text editor to see if they
   are actually all .gifs.
```

## Step by Step

- Download all of the gifs.
- Open up a linux terminal and use “`cd`” to change directories until you get the one with all of the gifs downloaded.
- Run `file *`
- It shows the real file type of all of the .gif files, in this case, `cat-gif-06` is actually a `.txt` file.

![picture of what comes up when file is run](/assets/lostbutnotforgotten1.png)

- Either rename the file to end with `.txt` or change the file type some other way.
- The text file contains the flag.
