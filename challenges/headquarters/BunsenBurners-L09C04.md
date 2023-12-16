# 🔥 Bunsen Burners - L09 C04

Agent 707, we've been looking into the different ways the Spetzners have been communicating with each other about their plans, and one of them is a science forum called Bunsen Burners. We want to see if the site is vulnerable in such a way that would allow us to serve our own JavaScript to one of the gang when they view it.

We've created an account for you and made a test forum page called "Hack Trick". Though it looks like input is sanitised, the alert function is still available. See if you can submit some malicious JavaScript and get an alert box to appear on the page saying "Kaboom!".

**Tip:** Get the site to output an alert with the right text and you'll get the flag!

💡 **Hint:** The technique you need to use is called Cross Site Scripting (XSS),
   and involves finding a way to run some JavaScript code on the computer of any user who views the page.
   Think about how you would do it if you were building the website yourself?

## Step by Step

- Type “`<script>alert("Kaboom!")</script>`” into the comment box and press enter.
- An alert box should pop up, dismissing it will reveal the flag.

`flag: 2rbNcnO1fuvaSW5dEnui`
