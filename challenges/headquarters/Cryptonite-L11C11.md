# 💠 Cryptonite - L11 C11

Yesterday our uncover agent let us know about an encryption tool one of the gang built called Cryptonite. It runs on one of the Bulldogs private servers and we think it might be vulnerable.

See if you can use it to get access to the server and look for any files that might be worth investigating. We think the gang member who built it, Percy Pinkly, is involved in the gangs efforts to circumvent the banks main security alarms, so he might have been storing files on the server related to blueprints or the security system.

**Tip:** There's a file on the server containing the flag.

```
💡 Hint: Focus more on the -n argument and see if you can take advantage of it.
```

## Step by Step

- To view all possible arguments with Cryptonite, type “`cryptonite -h`"
- Type “`cryptonite -n;ls`"
- Type “`cryptonite -n;cat security-blueprints.txt`"
- The flag should appear

`flag: 28ISToBLzwZlTmUqnVep`
