﻿# 🎮 Shipping Lanes - L08 C10

Recruit, we've been monitoring the web traffic of one of the gang members and he's visited a page, which has made us very suspicious. Why? Two reasons: first, it's called "shipping-lanes-target" (so we think he's using it to monitor the ship) and second, we can't get access to it! Whatever we try, it just won't work.

Take a look at the page, maybe have a dig around the source code and see if you can get us access to it.

**Tip:** Get access to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Look at the page source (the javascript in particular). What do those numbers mean when you look them up as JavaScript character codes?

</details>

<details><summary>

## Step by Step</summary>

- Use inspect element or view the source code to see this script

![konami code js](/assets/shippinglanes1.png)

- If you look closely, when you press a key while on the website, there is a number assigned to it and that gets put into an array. The script is comparing that to the `keySeq` array and will give you the flag if they match.
- You can figure out what the correct keys are by looking up the js keyCode values or looking at the console output
- The correct sequence uses the arrow keys aswell as A and B: `Up Up Down Down Left Right Left Right B A`
- Reload the page until you get the sequence right or keep pressing other keys until you see `<empty string>` in the consoles output and then try again

</details>
