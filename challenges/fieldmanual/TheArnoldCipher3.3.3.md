## CRYPTOGRAPHY

# The Arnold cipher

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/54387fcc-ccf8-4703-817a-fc4fa858537c" width="800" />
</div>

## A book cipher

The Arnold Cipher is a seriously cool example from history, both
because it is our first book cipher and because it has historical
significance. It's a fascinating and fairly secure means of encryption,
used by John André and Benedict Arnold on a negotiation of surrender to
the British in 1780.

Encrypting with a key does not always mean using a password you must share with the other party. Sometimes an external *rich source*
 resource, such as a book, is used as a means of encryption. Both sender
 and receiver must have identical copies of the book, as differences of
any kind mean the cipher won't work well.

The references might be page number and word, eg 217.34, 193.16...
would mean word 34 on page 217, then word 16 on page 193 and so on. The 2
 part references here are shorter, but you need a book that contains all
 the words from your message. Alternatively there may be 3 parts to it
such as 284.62.4, 67.29.8. These references are a little longer and
these 3 numbers may refer to page, paragraph and word (which would still
 have the same potential word existence problem as mentioned before), or
 page, word offset and letter offset (which would avoid that problem).

For example, here we have **paragraphs 3** and **4** from **page 7** of our book key:

> I was not able to light on any map or work giving the exact locality
> of the Castle Dracula, as there are no maps of this country as yet to
> compare with our own Ordnance Survey maps; but I found that Bistritz,
> the post town named by Count Dracula, is a fairly well-known place.
>
>
> In the population of Transylvania there are four distinct
> nationalities: Saxons in the South, and mixed with them the Wallachs,
> who are the descendants of the Dacians; Magyars in the West, and
> Szekelys in the East and North. I am going among the latter, who claim
> to be descended from Attila and the Huns.

Our cipher text is 7.3.17 7.4.5 7.3.10 7.3.10 7.4.7. We are already
looking at page 7, so the first plaintext letter would be paragraph 3,
letter 17 - h. Next, we have paragraph 4, letter 5 - e, and so on.

There are online tools which enable you to provide a 'digital book'
such as some copy from a Wikipedia article. However, in the electronic
age the chances of an update to that page are significant and
differences between sender and receiver copies of the book would cause
the cipher to not function well, especially over time. One of the
strengths of a book, when periodically used, was that it would have a
slow update cycle.

> This way of sending data encrypted might seem ridiculous now, but it
> does give us another insight in to fundamentally how the process works.
> Of course, historically this was a *revolutionary* approach!
> Think about a spy in enemy territory carrying a book. If captured the
> book could seem innocuous and not be used by the enemy to send false
> messages like a more obvious code book or message transmitter.

Considering the age of this cipher, given the right implementation it can still be surprisingly secure!

<div align="center">

[← Previous: 3.03.02 - Caesar or ROT ciphers](CaesarOrRotCiphers3.3.2.md) | [Next: 3.03.04 - The Atbash cipher →](TheAtbashCipher3.3.4.md)
:-|-:
