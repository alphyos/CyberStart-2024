# ⚡ Zapped - L05 C05

The gang have been using a lesser-known chat app called ChatZap to communicate. We know one of the usernames (kanako) but not the password. If we could get access we might be able to see what they're saying.

It's not a great site and the security is average at best. Look at the login page - they do SHA1 hash their passwords but leave them in plain sight in the source code. See if you can use that to get in.

**Tip:** Gain access to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: SHA1 hashed passwords are not reversible but a lot of the hashes for commonly used passwords have been put
   online. Maybe we got lucky and they are using a simple password?
```

</details>

<details><summary>

## Step by Step</summary>

- Look at the page’s source code. The encoded password is `36ABC61C95B4B4F2BF7568BA4A62386176AF46A0`

![image of sourcecode](/assets/zapped1.png)

- Use a [SHA1 password decrypter](https://hashtoolkit.com/decrypt-hash/?hash=36ABC61C95B4B4F2BF7568BA4A62386176AF46A0)
- Login with the username and decoded password to get the flag

</details>
