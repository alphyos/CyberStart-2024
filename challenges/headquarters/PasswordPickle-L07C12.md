# 🥒 Password Pickle - L07 C012

Hmm, these Chiquitoos are clever. We've intercepted a program that takes a password in and generates some output. We found the correct password (it's "password") but it still won't let us in. The other agents are stumped. Can you take a look and see if you can figure out how to get the output?

**Tip:** Get it right and you get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: It seems the password is time sensitive; you must enter it under a certain time limit or
   else the program will not allow you in.
   Try to find a command that will output whatever you type back to you.
   Then see what happens when you pipe that command into the program.
```

</details>

<details><summary>

## Step by Step</summary>

- Download the program on a Linux machine
- Open up a terminal, go to where the program is located and run `chmod +x filename.exe`
- Run `echo password | ./filename.exe`
- The flag should come up

</details>
