## CRYPTOGRAPHY

# Symmetric encryption

This is a
big topic! Encryption supports most modern applications and websites, as
 well as most of the technology around you. At this point in your study,
 we don't want to get too far in to encryption at the modern day working
 level, but let's cover some key concepts and show how you can encrypt
and decrypt some data with strong encryption.

Symmetric encryption is where a key is used for both encryption and
decryption. This same key can be used to encrypt and then decrypt. It is
 ideal in a scenario where I want to encrypt data, retain the key as a
secret, and then decrypt later. Of course, I could also share it with
another party via some out of bands mechanism to make sure the key is
kept safe.

There are broadly two types of symmetric encryption:

* **Block.** These work in 'blocks'. They take a defined
size of data, e.g. 8 bytes. They then encrypt one block at a time. They
continue working in blocks until the data falls short, and then they
simply 'pad' the data to align to 8 bytes.
* **Stream.** This works on a 'stream'. That means that
the data is encrypted as it flows. Instead of grabbing a block of data
and encrypting it, it encrypts it continuously and outputs it. This is
very useful if you have a radio signal for example!

There are many types of symmetric algorithm, such as AES and DES (block), or RC4 (stream).

There are numerous implementations available to you, but the `openssl`
 command line tool is a very handy quick tool to encrypt/decrypt. It can
 also be used to encode too! Let us review an example of encryption with
 AES256. Our plaintext file will be called `coolfile.jpg`.

```console
$ openssl enc -aes256 -base64 -in coolfile.jpg -out coolfile.enc
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

This command will ask you to provide a password, derive a key and
then encrypt the data. The coolfile.enc will contain the encrypted data
and will be wrapped in base64. Want to decrypt?

```console
$ openssl enc -d -aes256 -base64 -in coolfile.enc -out coolfile2.jpg
enter aes-256-cbc decryption password:
```

Note we added the -d and of course you will also need the same passphrase!

[← Previous: 3.07.01 - XOR encryption](https://play.cyberstart.com/field-manual/8fb2cccc-d7eb-11eb-9a39-0242ac140009)
[Next: 3.07.03 - Asymmetric encryption →](https://play.cyberstart.com/field-manual/8fb487ec-d7eb-11eb-a506-0242ac140009)
