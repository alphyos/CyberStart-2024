## CRYPTOGRAPHY

# Asymmetric encryption

Asymmetric
encryption (also known as public-key encryption) differs from symmetric
in that the encryption key and the decryption key are different. The
encryption key, often known as the public key, is used to transform the
plaintext to ciphertext. The decryption key, often known as the private
key, is then used to retrieve the plaintext.

> The private and public key are related through a mathematical
> relationship, but it is infeasible (at least for now!) to get the
> private key from the public key. The major benefit of this is that the
> public key can therefore be distributed widely and transparently. Anyone
> can use that key to encrypt messages that only you, in possession of
> the private key, can read!

For example, you have a website and you host public\_key.file on the
site. A person you have never met and with whom you have not exchanged a
 password can use this file to encrypt a message that only you can open.
 Indeed, if they encrypt their message and destroy the original, they
can't get it back!

One of the big benefits of this system is that you do not need to
pre-share a password to share encrypted data, you can exchange safe to
share public keys!

One of the challenges with asymmetric encryption is that compared to
symmetric it is quite slow. This can lead to using them in a combination
 that is quite novel:

A user, *Agent J*, wants to send a large chunk of data to another user, *Agent Z*.
 They have the public key of Agent Z, however, encrypting the data would
 be slow as it is quite large! Agent J has a program generate a long
complex key and then encrypts the original data with this new key,
symmetrically. This is fast!

Then Agent J encrypts the new key that was used, with the public key
of Agent Z. As the key is much smaller than the data, this is also fast!
 He then sends the encrypted data and the encrypted key to Agent Z.
Agent Z is able to decrypt the symmetric key that was encrypted using
asymmetric encryption, and quickly because the key is quite small. Agent
 Z can then decrypt the large data set using this key, at speed! This is
 a novel use of both technologies.

> Public key cryptography is used in a wide array of use cases. From
> encrypting data to digital signatures and authentication. Examples
> include RSA, ElGamal, Diffie-Hellman key exchange protocol, and more.

OK, let us use `openssl`, just as we did with symmetric
encryption, to generate two key files and then encrypt/decrypt. Normally
 this would happen on two computers, but we will do it on the same one
and simulate sharing of keys.

**Step 1**
We will generate a private key for AgentJ and also Agent Z.

```console
$ openssl genrsa -out AgentJ.pem 1024
$ openssl genrsa -out AgentZ.pem 1024
```

*Note, you can also protect keys with a passphrase that must be provided on every use!*

**Step 2**
Now we will make public keys for each agent.

```console
$ openssl rsa -in AgentJ.pem -pubout > AgentJ_public.pem
$ openssl rsa -in AgentZ.pem -pubout > AgentZ_public.pem
```

**Step 3**
Normally the agents would exchange public keys. They could e-mail them,
message them or send them however they like. They can be shared in the
open. As we have them on the same computer, we can skip this step.

**Step 4**
We will encrypt a message from Agent J to Agent Z, but first we need a message!

```console
$ echo 'Hey Agent Z, this should not be seen by Agent Q!!!' > plain.txt
$ openssl rsautl -encrypt -inkey AgentZ_public.pem -pubin -in plain.txt -out top_secret.enc
$ rm plain.txt
```

top\_secret.enc is now encrypted so that only Agent Z with their private key can open it.

**Step 5**
Agent Z will now decrypt the file, as they possess the private key!

```console
$ openssl rsautl -decrypt -inkey AgentZ.pem -in top_secret.enc > plain.txt
$ cat plain.txt
Hey Agent Z, this should not be seen by Agent Q!!!
```

Neat, you have your file back! We just used asymmetric crypto to
share data with another agent using their public key, and we never
exchanged a passphrase. This is really novel!

This topic is huge, and we could dedicate a whole Field Manual to it!
 If you want to learn more you can find many guides that walk through
how RSA works, as a great example of asymmetric cryptography. You may
also want to read about Diffie-Hellman exchanges, it is all quite
magical!

[← Previous: 3.07.02 - Symmetric encryption](https://play.cyberstart.com/field-manual/8fb39f12-d7eb-11eb-aa59-0242ac140009)
[Next: 4.01 - Introduction to Linux →](https://play.cyberstart.com/field-manual/8fb56ae0-d7eb-11eb-b9ec-0242ac140009)
