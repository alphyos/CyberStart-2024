# 🧙‍♂️ Rezapped - L06 C01

Remember ChatZap from a previous challenge? We need to get back in but it looks like they've changed their security. Take a look.

**Tip:** Log back in to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Hmm, it looks like the page uses a JavaScript based security check, but there's no relevant javascript on the page. Maybe it's in a separate file?

</details>

<details><summary>

## Step by Step</summary>

- Use inspect element and navigate to the “Sources” tab.
  - Dropdown from assets.
  - Dropdown challenge folder in assets.
  - Dropdown W0066/assets from the previous folder.
    - Dropdown challenge once again.
    - Click on the file starting with `kuro`. It should have the login information.
![picture of the files](/assets/rezapped1.png)
- Log into the account to get the flag
  - Username: `kanako`
  - Password: `wdJKg4f45h98.Lfuiohr`

</details>
