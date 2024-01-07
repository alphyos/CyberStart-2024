# 🛵 Start-Up Troubles - L02 C03

A successful new start-up that sells electric scooters has discovered a handful of their customers' accounts have been hacked - guess who we believe might be behind it? Yep, you guessed it, the Yakoottees! Having only just entered the market and keen to maintain their otherwise excellent reputation, this business needs our help to run a security audit of their login system. Can you **spot any security holes**, perhaps some **leaked data**?

**Tip:** Successfully login to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: As there's nothing useful in the interface, check out the page source. You'll find are some JavaScript variables being used and if the page can use them, it's possible we can too! Perhaps open your browser developer tools, particularly the console and try outputting those variables.

</details>

<details><summary>

## Step by Step</summary>

- Right click the page to bring up inspect element
- From there, navigate to the console tab and type `email`, then hit enter
- This should give you the email enclosed by ‘s, copy this into the login’s email form and then do the same but by typing `password` into the console.
    - Email: `bonita@zip-zap-rides.com`
    - Password: `abc123`
- Enter the correct details into the login page and submit to get the flag


