# 🎣 Grand Old Ruble - L09 C07

Ok, we need you to step into the shoes of the Spetzners best hackers for a while. We've received some intel that the gang have identified a vulnerability on the Grand Ruble Bank's website that allows them to perform actions only an admin should be able to.

Take a look and see if you can do the same so we can help the bank fix their security.

**Tip:** Transfer 1000 rubles to a user called cpa to get the flag.

💡 **Hint:** You will need to perform a Cross Site Request Forgery (CSRF) attack here agent.
   Simply put, you don't have access to the button that is grayed out, but the admins do.
   Find a link you could send to the admins that will automatically perform the action under their account
   if they click the link.

## Step by Step

- What you are trying to do is actually create a phishing email as seen on the second tab to the left below “Website”.
- When attempting to send “cpa” “1000” rubles, it does try to send you to the transfer screen with a flash of a url like the one seen below. It does not complete this however.

![url](/assets/grandoldruble1.png)

- By copying everything after .com, aka “`/transfer?amount=1000&recipient=cpa`”  You can paste this into the following email box.

![email](/assets/grandoldruble2.png)

- Sending the email will give you the flag.

`flag: xTx6TowS5YqBeFTqoqqQ`
