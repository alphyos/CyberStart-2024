# 🕵️ Hidden Report - L01 C08

One of the ways we've been investigating the gang and their bike shop is by actually buying products from them online. We've spotted a piece of functionality that we think might be exploitable, allowing us to get more information on other customers (some of which we think might actually be helping them with their plans to steal the eBikes).

Have a look at our account page on the site, it allows you to **generate a report** of your transactions. See if you can find a way to view a transaction report for the very **first user** of the site.

**Tip:** Find the **report for the first user** of the site and you'll get the flag.

```
💡 Hint: Try creating your report first. Is there anything about the URL you could potentially change to see other users
   reports?
```

### Step by Step

- Click “**Generate Report**”.
- Click on the url and change `user-456` to `user-1`.
- The flag should appear in the transaction report.

![image of the transaction report](/assets/hiddenreport1.png)
