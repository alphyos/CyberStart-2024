# 💬 Chatz With Semyon - L10 C06

Agent 707, we need your urgent help.

One of the gang, Semyon, has been using a Skype equivalent called Chirp to make calls. We know he made a call this morning to an associate of the gang that's planning to help as a getaway driver when they steal the EMP. We want to pick him up before he can help, so we need to know his phone number (which will help give us his location).

See if you can crack into the Chirp site. If you do you'll see the calls Semyon made today, we're looking for the one to Yury. Oh, and luckily one of the other agents has managed to get the PHP source code to the page, that might help.

**Tip:** The flag is Yury's phone number.

```txt
💡 Hint: You should read up on what extract() does.
   Can you find a way to set both the $key and $password variables by taking advantage of extract()?
```

## Step by Step

- Replace the url with the following url instead
  - `https://www.letschirp.com/login?key=''&password=''`
- The page should change to the correct log page, this is because `extract()` uses the insecure field, `$_GET`

`flag: 007 987 352 5373`
