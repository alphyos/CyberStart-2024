# 🔬 Centrifuge Exposed - L09 C01

Agent 707, here's a test for you to show the rest of the team you deserve to be on this level.

One of the Spetzners associates, Alexei, runs a science equipment ecommerce site called Centrifuge. Our team knows that he's secretly been using it to sell the Spetzners mad scientists the equipment they need for their schemes, so we've been trying to get access for weeks, to no avail.

We've just had a bit of good news. When making an update to the site Alexei made a mistake which, for a few hours last night, left some of the sites PHP code exposed. We managed to grab the code when it was there. Take a look and see if you can use it to find a way in to the site.

**Tip:** Get access to the site to get the flag.

```txt
💡 Hint: This code we recovered is looking for a cookie with a certain name and value.
   Find out what it is and create it, then refresh the page.
```

## Step by Step

- Right click the page and click inspect to use inspect element to navigate to the applications tab where the cookie information is saved
- Create a new cookie by double tapping a name space and name that cookie `userLoggedIn` and edit the value to be `true`
- Reload the page to get the flag

`flag: MO5aRh2dtu1BfnqwBZrZ`
