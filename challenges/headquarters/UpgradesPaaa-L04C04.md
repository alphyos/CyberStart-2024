# 🌳 Upgrades? Paaa! - L04 C04

It looks like The Choppers know they need to improve their security set-up, as recently we've been unable to log in to their intranet and they've been making a few changes to their security.

They have rewritten their login form to use slightly improved JavaScript, but it doesn't seem to be much more secure. Maybe you could change some of the JavaScript on the login page to see if you can log us back in.

**Tip:** Log in successfully to get the flag.

```txt
💡 Hint: If you completed all the challenges on the previous level you'll remember that one required you
   to look at the source code for this login page, and the password was right there in the JavaScript.
   You'll need to do the same here, except make a few changes to the JavaScript to get it to run and
   output the password for you. Use that to log in and the flag is all yours!
```

## Step by Step

![picture of sourcecode](/assets/upgradespaaa1.png)

- Looking at the source code and finding the username and password requirements, var password is equal to the combination of two other variables with the assigned strings of `t1mberl4nd` and `-el33t` respectively.
- The username is `aksel` and the password is `t1mberl4nd-el33t`.
