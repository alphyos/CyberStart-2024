## CRYPTOGRAPHY

# Collisions and poor use

## Collisions are a possibility

A great hash algorithm will mean that the slightest change to an
input causes a hugely different output. For example, using the MD5
hashing algorithm, input text `ABCDEF` has the hash value `8827a41122a5028b9808c7bf84b9fcf6` and `ABCXEF` (just a single character changed from before), has the hash value `58ce9f83020af6d05a7c1877f92ab4f0`. It's wildly changed, due to what's known as the **avalanche effect**.
 Without this drastic change, you could potentially work out original
inputs from other similar hashes, so is a crucial aspect to have in a
hashing algorithm.

Note that not all hashing algorithms are perfect and some have come
to be considered "cryptographically broken". While MD5 has a hash length
 of 32 hexadecimal characters and so can cater for a huge number of
variations, has been found to produce the same hash for two different
input values. It's extremely rare to find these "collisions", but as
soon as one is found, all trust in using it for validation has to be
lost. The same is true of another popular hashing algorithm called
SHA-1, which has a hash length of 40 characters. Both MD5 and SHA-1 are
still very useful today (keeping in mind the slight weakness of a
potential collision), but are considered less secure than newer, more
robust algorithms.

Naturally, trying to have unique values in small fixed length hashes
such as 32 or 40 characters will always have the potential for
collisions, given the infinite number of inputs you might put through it
 and a finite number of hashes possible (however huge the range of
possibilities). Newer hashes have different properties to get around
this, such as **Bcrypt**, which imposes a **cost** to hash something (ie, it's computationally **expensive**).
 That means it can take a few extra milliseconds to produce the hash;
not noticeable by humans, but mass hashing carried out by attackers
happens far slower, so they can test far fewer hash variations per
second and so far less likely to determine the plaintext via brute
force.

## Incorrect or inappropriate usage

Collisions in cryptography are rarely found and a far bigger worry is
 when a developer has incorrectly used a hashing algorithm, or the user
chose an inappropriate plaintext such as a poor password choice. We
actually demonstrated the latter above - the string `password123` produces the MD5 hash `482c811da5d5b4bc6d497ffa98491e38`. While MD5 isn't perfect (collisions have been found), the real problem is the user's input. This is because there are huge **hash lookup**
 tables online, containing pre-calculated lists of common passwords and
the hashes for them. If you search online for a hash lookup table, or
just simply search for the hash mentioned, you'll find plenty of results
 online which tell you the plaintext was `password123`. This
is not a security flaw in MD5, but the lack of ensuring users set a more
 complex password. Providing a secure solution therefore includes a few
aspects - choosing a robust algorithm, having sensible usage of it and
making sure users provide strong passwords to avoid lookups.

On the next page we'll look at how salts can avoid the lookup table problem.

[← Previous: 3.04.01 - Introduction to hashing](https://play.cyberstart.com/field-manual/8fa8fec2-d7eb-11eb-9cd0-0242ac140009)
[Next: 3.04.03 - Salts →](https://play.cyberstart.com/field-manual/7cdc78c8-d7eb-11eb-b332-0242ac140009)
