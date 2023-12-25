## CRYPTOGRAPHY
# Introduction

<div align="center">
  <video src="" width="800" />
</div>

# Welcome to the wonderful world of cryptography!

In this section we will be making and breaking codes along with exploring tools and concepts to help reveal passwords, find flaws in encrypted information, and look into how data makes its way across the internet securely.

>Encrypting and decrypting data powers so much of the modern world around you. When you log in to an app on your phone, how do you think your username and password make it there safely? Even on your phone you've likely got the entire storage space encrypted (most tend to these days) in case it's lost so that no one can get their hands on your data.

Cryptography is a fascinating and vast subject area, but you'll be able to get quite far with some logical thinking, basic mathematical understanding of concepts and use of some tools. This is enough to have an impact in security testing, however if you really want to study this area it is one of the cyber security disciplines that tends to outright require an academic approach (university, for example) and extensive study of related mathematical concepts. See if you find it fun, it may even be what you want to do in the future!

Some terminology you may find helpful as you proceed:

1. Encryption. A process and method which takes plaintext and produces ciphertext that can be sent to another party, or stored. This often requires a key.
2. Decryption. A process and method which takes ciphertext, and produces plaintext. This often requires a key to be shared so that you can retrieve the plaintext data.
3. Key. A piece of information (typically a string of letters, numbers etc) which is used as part of an encryption and decryption process. Depending on the cipher, different requirements may exist for the key in size or structure. Sometimes different keys are used to encrypt/decrypt, which we will learn about later.
4. Cipher. An algorithm for performing encryption or decryption. Essentially a recipe that can be followed to produce the result. The cipher typically requires a key and the combination can transform plaintext to ciphertext, or back.
5. Hashing. This is where a plaintext input has a hashing algorithm applied to it, to produce a fixed length output of seemingly random, but always repeatable output if you follow the same steps. Most commonly used to validate data such as identity.

During our journey in the chapter we'll also discuss weaknesses in some areas of encryption, common misunderstandings people often fall into and how to make good choices in cryptography. Let's start by looking at password complexity in the next section.