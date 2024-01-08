## FORENSICS

# File integrity and hashes

File
integrity is particularly important in forensics. It allows us to
identify if any unauthorised changes have been made to the file and
allows us to prove that a file has not been changed.

This process is integral in forensic investigations, as it allows
investigators to be certain that the files have not been exposed to any
damage, manipulation or tampering throughout their investigations, thus
allowing it to be admissible in court.

Or perhaps, if you publish a piece of software online, you may want
to provide some way of proving that the file has not been tampered with
by a third party when it was redistributed. We do all this using a file
'hash'.

Hashing is a form of one-way encryption. When a file is operated on
by a hashing algorithm, it will produce a value that is unique to the
contents of that file. If you use a good hashing algorithm, when you
change by even one bit, the hash produced by the hashing algorithm will
change drastically, in what is known as the 'avalanche effect'.

MD5, SHA1, SHA-256 are a few examples of common hashing algorithms
you may come across. For more information on hashing, check out the [Hashing](IntroductionToHashing3.4.1.md) page in the Cryptography section.

## Hash Collisions and forensics

There has been research published for a number of years now referring
 to MD5 (and other algorithms) being "broken", as it is possible to
generate collisions. This is the process whereby two different pieces of
 data can be calculated to have the same hash value.

This research does not change the forensic process and does not mean
that we are required to use more complex algorithms, but illustrates
that trust can be lost in situations like this.

When a disk image is taken, it is normal to record both an SHA-1 and
MD5 hash values. Even if it were possible to create a collision on a
hash that you did not create/generate, the second hash would be
different, showing that tampering had occurred.

<div align="center">

[← Previous: 7.02.01 - Headers and strings](HeadersAndStrings7.2.1.md) | [Next: 7.03 - Steganography →](Steganography7.3.md)
:-|-:
