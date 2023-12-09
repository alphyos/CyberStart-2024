# ⛵ Hidden Boats - L07 C02

Those Chiquitoos are a busy gang and they run a number of legitimate and criminal operations. One of their legitimate businesses is a small boating company that transports workers to the offshore wind farm. Their website has a page, which lists all the scheduled trips out, but we think there might be more that they're not making public. Our inside informant tells us they're stored in a file called "extra.txt". Have a look at the site and see if you can get access to it.

**Tip:** The flag is the boat number of the last one in the secret list.

```
💡 Hint: Look at the page URL and how it's being used to load the list of scheduled trips.
   Is there any way you could change that to show the extra trips file?
```

### Step by Step

- Modify the default url by adding `?file=extra.txt` at the end of it
- Final url should look like this: `https://www.boatcabs.com/scheduled?file=extra.txt`
- The website should change, look for the last boat’s number

![image of the extra trips](/assets/hiddenboats1.png)
