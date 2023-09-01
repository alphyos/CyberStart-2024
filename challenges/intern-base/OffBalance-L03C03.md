# ⚖️ Off Balance - L03 C03

We're hot on the heels of catching this cyber gang but the closer we get, the more damage they try to inflict onto the Barcelona tourism industry!

This time, they've hacked into a large international bank's mobile application. Customers of the bank are complaining they can't see their current **balance** and these criminal masterminds need to be held to **account**. Intern, help customers retrieve their balances, so they can continue to spend their money during their well-earned holidays!

Helping our international friends will really help develop our **network**.

```
💡 Hint: If you check out the Network tab in the developer tools of your browser while you click on different pages in
the app, you can see there are requests being made to an API. Try using a Linux command line tool like curl to talk to
the API directly to see if you can get at the account balance that way.
```

## Step by Step

- Use Inspect element to go to “Console”.
- Enter “`getPage(”accounts”)`”.
- Go to the “Network” tab.
- Scroll all the way down until you get to “get-accounts”.
- Go into that log’s “Response” tab.

![picture of the response page](/assets/offbalance1.png)
