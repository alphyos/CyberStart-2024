# 📝 Maggie’s File - L04 C06

Our field agent has managed to get some login details from one of the gang, Magdalina. We believe she uses the details to SSH into a remote server to view a particular file that might be important.

These are the details we have:

**IP address:** 192.162.132.199 **Username:** maggie **Password:** ubersecurepw

Why don't you try it yourself using the secure terminal we've provided and see what you find.

**Tip:** The terminal uses non-default implementation of OpenSSH and only accepts common formats. The flag is the name of the file.

```
💡 Hint: Never used SSH? Don't worry. Type `$ ssh user@ipaddress` from the command line in the terminal where user is the
   username and ipaddress is the IP address of course. Once you're in, you should see a file there. Its name is the flag.
```

## Step by Step

- Type `ssh [username]@[ip]`, this would be `ssh maggie@192.162.132.199`

![output of the terminal, the file is in /root/docs/secretz](/assets/maggiesfile1.png)

- Type the given password in. `ubersecurepw`
- Type `ls` to list contents in the directory and you will find the file/flag.
  - Remember, the file name itself is the flag, not the contents of the file. 
