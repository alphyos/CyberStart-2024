# 🎸 Secret Source - L03 C05

It looks like the gang has a lot of information we might find useful on their intranet; probably details of how they intend to break into their competitors' computer systems to look for the plans to their better felling machine. It would be especially useful if we could log in as their main developer, **Aksel**.

Sometimes developers can be a little bit lazy and leave **information** in the **source code** of a page that might be revealing. Perhaps you could take a look and see if there's anything Aksel left that might help you log in.

**Tip:** To get the challenge flag you need to successfully login.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Did you know that it's possible to view the source code of a page by using Developer Tools, or by right clicking on a page and selecting "View Source"? It looks like the developer Aksel is using some basic JavaScript to check whether the password is correct. However, he hasn't obfuscated his code at all so if you view the source code you should be able to see what the details are. Look for the code between the `<script></script>` tags.

</details>

<details><summary>

## Step by Step</summary>

- Use inspect element and click on any of the source code.

![image of the source code](/assets/secretsource1.png)

- Use Ctrl + F to search for `Aksel`.
- The username and password for the developer, Aksel should pop up.
- Logging in with those credentials should give you the flag.

</details>
