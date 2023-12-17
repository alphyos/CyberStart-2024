# 🖱️ Broken Click - L02 C06

Here's a weird one Agent 707, there's now a **link** on the Slootmaekers login page for an **admin login**. We wanted to take a look but the link **doesn't seem to work**. Can you figure out how to get to it?

**Tip:** **Get to the admin login page** to get the flag.

```txt
💡 Hint: How about looking at the source code of the site to see where the link is meant to be pointing to? You could then
   copy and paste it into the browser window URL field.
```

## Step by Step

- Use inspect element or look at the source code, click and use Ctrl + F to find `admin`.
  - This reveals where the login link is meant to be pointing to.
- Change the original url to: `https://www.slootmaekersbikefactory.com/adminarea/login`.
