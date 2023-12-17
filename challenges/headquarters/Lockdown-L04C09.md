# 🔐 Lockdown - L04 C09

It looks like The Choppers might know we're trying to get into their intranet.

They've currently got it locked down by disabling the login form. We still have a correct username and password - can you find a way to get in?

**Tip:** Log in successfully and you'll get the flag.

```txt
💡 Hint: Hmm, it looks like they didn't lock down the login form entirely; all they've done is disable the form's input
   button. Could you maybe use Developer Tools to get around that?
```

## Step by Step

- Hover over the login submit button and right click to `inspect`.
- Source code should pop up for the button and the original text says `disabled`.
- Replacing this with `enabled` like the photo below will make the button work.

![picture of the source code](/assets/lockdown1.png)
