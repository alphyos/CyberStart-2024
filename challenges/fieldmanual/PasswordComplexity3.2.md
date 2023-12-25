### CRYPTOGRAPHY
# Password complexity

<div align="center">
  <video src="" width="800" />
</div>

# Passwords are everywhere

Passwords are used in websites, apps, devices, tools and many other contexts. While new authentication mechanisms like touch-based or face recognition are gaining in popularity because of their usability, passwords are still everywhere and likely will be for some time in the future.

To us all, passwords are a well-known concept; but in spite of this many will still engage in poor password practices. It is also the case that recommended practices change from time to time, yet people hold on to outdated ideas such as a 'strong 8-character password' when this is no longer effective and hasn't been for years now.

>You can use strong encryption like AES-256 (see Symmetric encryption); but if the password is weak (such as password123) then you have little security due to a poor choice of password.

Using a common password, for example Password123, is another big problem. Using data gathered from many previous hacks and breaches, hackers can generate huge lists of valid usernames, email addresses and a smaller selection of common passwords. These can be tried in random combinations against one or more sites in what is known as **password spraying**.

When a user sets a password there is the danger of password re-use, where the same password is used on many sites by a single user. One of them is breached and the password discovered, meaning that an attacker now has valid login credentials for any site the user belongs to.

Even if your password hasn't been breached, often what may seem like a strong password can be easy for the cyber criminals to break with powerful and fast automated tools. These tools often crack encrypted passwords offline with brute force methods, or guess the password with login attempts, often aided with lists of common passwords. Humans commonly think they are being clever and unique, but actually find they're being staggeringly predictable and actually making life easy for cyber criminals.

# Breaking passwords

There's a lot of assumptions made about how computers crack passwords and depending on the situation the implementation can vary. Most people, when they first encounter the idea of a password being cracked by a computer, think of it as trying sequences one after the other until success, e.g.

`AAA, AAB, AAC, AAD, {..}, BAA, BAB, BAC, BAD, {..}, PASS, PAST`

This brute force style of breaking a password works in a predictable order and slowly tries ever longer combinations. If you add symbols or upper/lower case to the range of possible characters there is an explosion in the number of permutations it must try, and so it takes a lot longer. Even so, an average computer today can attempt tens of thousands of guesses per second and short passwords are revealed in very little time.

Attackers can further increase their chances of success with simple tactics such as looking at the password requirements on the registration page. If a password needs an uppercase and lowercase letter, a number and at least 12 characters, a huge list of passwords can be refined to try with automated tools, focusing their efforts by matching the specifics they know your password will have.

You can search online for password strength tools. Try a few out, you might be surprised that what you thought was a secure password can actually be cracked or guessed easily.

>If we know someone used the password Barkley1994 and had to add a symbol, we can have a computer try adding the typical choices after the base password, such as `!.<>\';#$`. Not sure of the year? We could have a computer take the base word `Barkley` and try to guess the years and symbols. It's extremely quick to try a huge number of variations!

These days, cracking a weak password is made even simpler with easy access to tools such as [Hashcat](https://hashcat.net/hashcat/) and [John the Ripper](https://www.openwall.com/john/).

# Quickly generating passwords on Linux

We'd recommend using a password manager to store all your passwords. Simply set one master password for the app and let it take care of the rest. A good password manager will generate the complex passwords for you, to avoid you creating any that are weak. However, if you need generate a quick secure credential and perhaps also specify the properties, you could use a Linux tool like `pwgen`. Some example properties provided to it may be:

`pwgen -s 12 1 - Generates one password of 12 characters
pwgen -s 16 1 - Generates one password of 16 characters
pwgen -y -s 12 1 - Generates one password of 12 characters, including the use of symbols
pwgen -s 16 12 - Generates 12 passwords of 16 characters`

`pwgen` does support the ability to pick sequences that are likely 'pronounceable' to make it easier to read them out, or memorise them if you really must. It's quite a popular tool and with a lot of options for customising to your liking.

However, the latest advice in the industry is to avoid very hard to type passwords and instead use a "passphrase" (a collection of 4-5 randomly picked words). The "xkcd" series of comics summed up this thinking nicely [xkcd password](https://xkcd.com/936/) strength. You could take a look at [pwgen-passphrase](https://pypi.org/project/pwgen-passphrase/) which can return a number of words that are hard to guess and easy to remember if you need to generate a passphrase.

# Forced password resets

It's starting to become industry accepted best practice to avoid enabling forced resets (eg every 30/60/90 days the user must set a new password). People are busy and also predictable, so if they've a password of `b1cycLe3`, it's likely next time they'll use `b1cycLe4`, or perhaps the name of the company or service, or the name of their pet, or the current season and year. Password resets are implemented with good intention but it has been found they don't really make a difference to security and, if anything, lower it.