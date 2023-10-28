# 🧿 Out of Sight - L05 C04

Well, that's a bit of luck. We've managed to get our hands on some details that allowed us to SSH into one of the Yakoottees private servers. They're a sophisticated gang, so they've probably hidden a few files in there. We've got you into their server, have a look and see if you can find anything.

**Tip:** The flag is in a file somewhere on the server.

```
💡 Hint: There is a hidden directory on the server, try searching for `$ man ls` on Google to see how to view hidden directories.
```

## Step by Step

- Run `ls -la` This will reveal hidden directories
- Run `cd .secret-files` This will change directories to the hidden one
- Run `ls` This will show the flag text file
- Run `cat flag.txt` This will read the text in the file and print the flag

![image of terminal](/assets/outofsight1.png)
