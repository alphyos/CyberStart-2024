# 🧪 Hidden Centrifuge - L09 C03

Agent 707, we've been looking through the Centrifuge ecommerce site, run by one of the Spetzners associates Alexei. It contains thousands of pages, so one of the ways we've been doing that is simply by using a search engine, which has indexed all the pages.

The team have been starting to wonder whether there are other pages that we've not seen. Can you see if you can find them.

**Tip:** Find the hidden page to get the flag.

```txt
💡 Hint: Hmm, what would make a page invisible from search engines?
```

## Step by Step

- A way to find pages that are typically **hidden by search engines** is to look for a file called `robots.txt`.

![robots.txt](/assets/hiddencentrifuge1.png)

- Typing this in allows us to view what page urls are hidden such as `/testtubes.html`.
- Copy this into the end of the url after .com and you will find the flag on this new page.

![testtubes.html](/assets/hiddencentrifuge2.png)

`flag: 2B8vYSrQrHq1MPJgh584`
