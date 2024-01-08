## CRYPTOGRAPHY

# Salts

## Salting your hash

While encouraging good plaintext input from users is highly
recommended, there is another common solution (though less preferred
today), which involves a **salt**. There is where you have
some extra random text (ideally random per user), that you prefix,
postfix or otherwise mix into a user's plaintext. Both the salt and the
hash are stored for future validation. Let's look at an example:

```console
$ echo -n "password123:ah37272" | md5sum
8a3bb4724649745925ee0971ef13b304
```

Above we've got the users' plaintext of `password123`, we have a randomly generated salt value of `ah37272` and a `:`
 character to seperate them (completely optional, but visual separation
can be useful). MD5'ing that whole string produces the hash `8a3bb4724649745925ee0971ef13b304` which you won't find online, as overall, it's hash for a fairly unique string. We store both the salt, colon and hash value `ah37272:8a3bb4724649745925ee0971ef13b304` in the database. Now when the user returns in the future to login and enters their password of `password123`, we can separate the salt portion `ah37272` of the value stored in the database, and again MD5 hash the whole string `<user login password>:ah37272`. This should match the hash value stored in the database after the colon - `8a3bb4724649745925ee0971ef13b304` - if they entered the correct password.

While this doesn't enforce good password choices on the user and
allows them to still use a weak password (highly advised against),
salting your hashes can provide extra security compared to not salting
them. Salts are not a real "secret" (it's why they can be stored in a
database in their plaintext form) but they can be used, figured out how
to use them (perhaps prefixed, postfixed or mixed somehow?) and common
passwords attempted using these possibilities. It makes the brute force
attacks harder to get right, but not vastly harder. Some of these brute
force tools include [Hashcat](https://hashcat.net/hashcat/) and [John the Ripper](https://www.openwall.com/john/).

We've really just covered some basics of hashing with the above and
previous pages of the Field Manual and highly encourage you to research
more online about this fascinating and critical area of cryptography!

[← Previous: 3.04.02 - Collisions and poor use](https://play.cyberstart.com/field-manual/5b1d071b-d7eb-11eb-89e6-0242ac140009)
[Next: 3.05.01 - ASCII →](https://play.cyberstart.com/field-manual/8faa18d4-d7eb-11eb-aa93-0242ac140009)
