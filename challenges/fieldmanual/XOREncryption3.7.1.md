## CRYPTOGRAPHY

# XOR encryption

The XOR
cipher uses... you guessed it, the XOR (exclusive or). Much like other
ciphers, you’ll have three components - the plaintext, the ciphertext
and the key. One of the great properties of XOR is that if you have the 3
 components, and you XOR any two, you can produce the other one. This
somewhat naturally produces an encryption and decryption mechanism. This
 also provides reasonable security because if you have 1 of the 3 parts
it is very hard to guess the other 2 correctly!

Let us look at an example by first reminding ourselves how XOR works:

```txt
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0
```

This cipher works by doing the following:

* Encryption: Plaintext *XOR* Key = Ciphertext
* Decryption: Ciphertext *XOR* Key = Plaintext

There are also other versions for key recovery, but these are for more advanced study later.

In this instance, the plaintext is `HEY`. That means when converted to binary `HEY` is `01001000 01000101 01011001`. Our key must be the same length as the data we wish to encrypt, so our key will be (for great irony) `KEY` which is `01001011 01000101 01011001` in binary.

Now we simply need to align these two into columns and XOR them one by one. Let us label the plaintext `p`, the key `k` and the ciphertext `c`.

```txt
p = 010010000100010101011001
k = 010010110100010101011001
c = 000000110000000000000000
```

The first value in both p and k is 0, therefore we do 0 XOR 0. This
produces a 0 and forms the first in the ciphertext. The second in the
sequence is 1 and 1, therefore 1 XOR 1 produces 0. We continue the
process until we are done. This is why the key must be identical to the
plaintext!

At the end of the encryption process, if we only have c it is very
hard to figure out the original message was HEY (it could also be all
kinds of other words, so without context this is strong security).
However, if I possess c and k (because the sender shared the key with
me) I can simply XOR c and k one by one, and I will get p back!

Isn't that amazing! This is a very simple encryption scheme and
depending on the key and use case it can provide some reasonable
security.

Often times with programming languages you can XOR non-binary data
such as hex. Behind the scenes this will convert from hex into binary,
XOR the values, and convert the binary result back into hex for you. It
helps make things a lot simpler, but the fundamentals are the same!

> You can search for tools to do XOR encryption, and it is built in to [CyberChef](https://gchq.github.io/CyberChef/).
> This may be a simple cipher, but it is more accessible and a wonderful
> way to understand what happens when we encrypt or decrypt by hand.

<div align="center">

[← Previous: 3.06 - Encoding vs encryption](https://play.cyberstart.com/field-manual/8fb100e0-d7eb-11eb-8c2b-0242ac140009) | [Next: 3.07.02 - Symmetric encryption →](https://play.cyberstart.com/field-manual/8fb39f12-d7eb-11eb-aa59-0242ac140009)
:-|-:
