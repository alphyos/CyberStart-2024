# 🎰 Account Roulette - L12 C03

Agent 707, remember the social media website from the previous level where Bulldog gang member Darren Greggs posted that cryptic message? If we could log in as Darren we could post messages as him and confuse other gang members. Unfortunately we don't have his login details, but we're sure you can find another way to log in as him using a possible vulnerability we think exists.

We have logged in as a random test user that we created and have gone to an old message Darren posted. See if you can use that access to log in to other accounts, then check the response to see who you are logged in as, aiming to find access Darren's account (his username is thedazman).

**Tip:** Understand what identifies the users logged in state to start.

```txt
💡 Hint: Can you find an ID for the logged-in user?
   You’ll need to cycle through all the possible values and check which account you’re logged in as,
   to try to find Darren’s account (thedazman). It’s possible to automate this with CURL or Python.
```

## Step by Step

- To find which account belongs to thedazman, use this bash script: `for i in {0..100}; do echo $i; curl -s -b "speek_sess_id=$i" https://wespeektogether.com/thedazman/status/74635478354 | grep "as thedazman"; done`
- Once the grep command was successful press ctr + c to stop the script, `49` should be the number showing up right before the grep result
- Use inspect element to go to the “Application” tab to edit cookies.
- Alter cookie called `speek_sess_id` to hold the value `49`
- Reload the page and the flag will show

`flag: l5r6P2qys2w6M3bEvk8p`
