# 🌱 Recruit List - L09 C12

Agent 707, the Spetzners are trying to recruit someone on the inside of the hidden weapons facility to help them get the access they need to steal the EMP. We believe one of the gang members has made a list of names of the people they want to target, and placed it on his own private web server.

We've found the login page for it, see if you can get access.

**Tip:** Bypass the login form to get the flag.

```txt
💡 Hint: Did you see the comment in the source code suggesting you take a look at "page.phps"?
   Take a look. What does urldecode do? Can you do the opposite of urldecode?
```

## Step by Step

- In the source code, there is a comment saying that login details are available at `page.phps`
- Change the url to `https://118.279.0.1/page.phps`
  - It is notable that the code does not check for inputted username inside the login page but rather an unrelated variable, `user` which needs to have the value `<root>`
  - The program also decodes `user` so an encoding of `<root>` is needed
- Change the url to `https://118.279.0.1/login?user=%3Croot%3E`
- The flag should appear

`flag: 9kGvib4hmWT1ffFvaMv1`
