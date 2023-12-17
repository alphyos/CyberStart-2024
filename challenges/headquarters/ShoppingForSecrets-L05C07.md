# 🛒 Shopping For Secrets - L05 C07

An agent on Level 05 has told us about another big hack he's working on. Apparently someone broke into a popular shopping site, stole all the usernames and passwords and was going to post them online. Luckily, we got to them first and recovered the details. Why is this important? Well, it seems one of the Yakoottees was a member of that site.

He typically uses one of these three usernames: kazuya, kaz_whizz, kazuya99. We've put the recovered data on one of our servers. We've given you access, so see if you can find him on there. If we knew the password he uses maybe we can use that later.

**Tip:** The flag is his password.

```txt
💡 Hint: Forgotten how to SSH? Search for `$ man ssh` on google for some help. You might also want to take a look at grep.
   Search for `$ man grep` on google for some information on how to use it.
```

## Step by Step

- Run `ls`
- Run `grep "kazuya" 182k_accounts_rip.txt`

![image of terminal](/assets/shoppingforsecrets1.png)
