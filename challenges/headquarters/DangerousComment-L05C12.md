# 🚁 Dangerous Comment - L05 C12

One of the Yakoottees, Haruka, recently created a site where she posts photos of her favourite cars. We think it might be a front to store files containing their plans to break into the Superspin factory. Each page has a form on it where you can post comments. Try and use the form on this particular page to use command injection and find any files hidden in the same directory. Remember, to inject code you need to include two commands by including a semi-colon.

**Tip**: One of the files has the flag in it.

```txt
💡 Hint: Try using a semi-colon in the comment box, followed by the code you want to run.
   So, perhaps try ;ls first to get a list of files.
```

## Step by Step

- Scroll down to the comment section query and send `;ls`

![picture of the input box and command execution](/assets/dangerouscomment1.png)

- Send `;cat escape_plan.txt`
- The flag should appear
