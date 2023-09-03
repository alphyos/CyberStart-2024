# 🏁 610enC0de'd Password - L02 C04

Agents believe they have found a server belonging to a gang called the Yakoottees. If we can get access to it who knows what information we can gather on them! So far the Yakoottees have been very successful hiding their activities by **encoding** everything they do. We've found their server but **don't have the password** and so can't login. Can you help, Agent 707?

**Tip:** Login to the server to get the flag.

```
💡 Hint: Inside the big waving flag it looks like encoded information, maybe it contains a message that will help us?
   Notice this encoding has similar groupings of 4 characters, there's `\x` followed by a couple of letters or numbers.
   See if you can search online to find out what sort of encoding uses that format. Once you know, you'll need to copy
   all the characters inside the flag and run them through a tool to decode the message
```

## Step by Step

- Hold down right click and hover over all of the slashes and numbers, use Ctrl + C to copy this.

![highlighting of the numbers](/assets/610enc0dedpassword1.png)

- Enter these numbers into a [Hex to Ascii converter](https://www.dcode.fr/ascii-code).
    - The phrase should decode to: `Welcome to the 610enC0de server. The server password is [password] - great decoding BTW, laterz!`
- Enter the server password back into the website and hit enter to get the flag.
