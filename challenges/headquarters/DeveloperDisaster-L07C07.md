# 📄 Developer Disaster - L07 C07

Agent 707, quick job for you. We've been using the shipping company website to keep an eye on which ships have been coming in and out of port. However, it looks like their developer pushed an update to the site, which has broken it and then he went home for the day!

There's an error message on the site. See if you can find a way around it to get us back in.

**Tip:** Get back in to get the flag.

```txt
💡 Hint: POST data is not stored in the URL like GET data, so it is harder to work with.
   You can use curl to send POST data, go to your terminal and type $ man curl for more information.
```

## Step by Step

- Type `curl --data UserID=0 https://slowlaneshipping.com/latest`
