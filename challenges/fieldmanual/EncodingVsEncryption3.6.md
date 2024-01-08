## CRYPTOGRAPHY

# Encoding vs encryption

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/750e2362-c3d0-4ec9-a2e0-52adb4401d2d" width="800" />
</div>

## To key or not to key

Encryption and encoding are often misunderstood, and sometimes people
 will use the terms interchangeably. They should not be viewed as the
same however; they both have very different purposes and using one or
the other inappropriately can lead to catastrophic consequences.

The goal of encryption is to get data from A to B, providing secrecy
as to the contents of the message. An encrypted message will often
require a key to return the cipher text back to the original message.
Without all of these components (the algorithm, the cipher text and the
key) it should be extremely difficult to retrieve the original message.
Let's look at an example of encrypting the contents of a file:

```console
$ openssl aes-256-cbc -salt -in input.txt -out output.txt
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

Here we're using the popular OpenSSL command to apply AES-256-CBC
encryption. We're stating a salted password needs to be applied, the
file "input.txt" used as a source and the file "output.txt" created as
our target encrypted file. Running this command, it will ask us to
provide a password, ask to confirm the same password again (for your
certainty) and the output file is then created.

AES-256-CBC is a great, modern form of encryption, providing an
extremely high level of encrypted output, particularly as the data
produced is very random (a great attribute for any good encryption
scheme). We can run `file output.txt` which will inform us that it's an OpenSSL encrypted file, which is encrypted with a salted password.

Encoding, however, simply takes some data and converts it into
another form. This is typically done to enable the transfer of data
because only a limited character set (eg just alphanumerics) can be
used. For example, we may have a collection of binary data but only a
means of transferring data as ASCII characters. Encoded data is not
intended to be secret and can be easily converted back to its original
form. It's merely to make it suitable for transfer and very likely
decoded as soon as it's received the other side.

Sometimes we can combine the two together: first encrypting data to
keep it secret, and then encoding it to allow us to transfer the data
somewhere.

> A final reminder: Encoding data when you meant to encrypt provides no
> security! Encrypting data when you meant to encode may mean the data
> cannot be transmitted successfully. Make sure you're using the right
> tool for the job... encoding is for transfer, encrypting is for
> security!

<div align="center">

[← Previous: 3.05.06 - UTF-8](Utf-83.5.6.md) | [Next: 3.07.01 - XOR encryption →](XorEncryption3.7.1.md)
:-|-:
