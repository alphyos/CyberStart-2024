# 🏴‍☠️ Dear John - L10 C12

Ok, a really important task for you, Agent 707. We need access to the main Spetzner database! We think it's the only way to not only bring the gang down, but also gather the amount of incriminating evidence we'll need to prosecute.

We have a word list and a binary. The binary has been pre-programmed with the hashed password for their database server. When provided a word list it will attempt to crack the password.

Unfortunately, the word list doesn't have the password on there, we think it may be a similar word though. Another agent mentioned a program called "john" which can alter word lists to make minor changes, can you look into that and see if you can use it to establish the password?

**Tip:** Get access to the database to get the flag!

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Taking a word list and changing it is called word mangling.
   The password for the database server isn’t in the word list we’ve provided, we know that much,
   but if it’s a variant, using John to mangle the words in the wordlist might produce results.
```

</details>

## Files

- [program-x86](/assets/dearjohn1)
- [words.txt](/assets/dearjohn2.txt)

<details><summary>

## Step by Step</summary>

- Download the files
- Use `john --wordlist=[wordlist name] --rules --stdout > new_words.txt` to generate a mangled wordlist or `--rules=Jumbo` if that does not work
- Run `chmod +x [program name]`
- Run `./[program name] new_words.txt`
- This will find the correct password `roronoa7` and spit out the flag

`flag: CG3GPtycLfxdzYyi2xp`

</details>
