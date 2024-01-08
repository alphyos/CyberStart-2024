## WALKTHROUGHS

# Happy Customers

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, a curious looking list of customers was spotted being
shared between a gang's bike shops. Each customer had a unique pattern
of numbers after their name, which we think might be **encoded words**. To support this, we also noticed **the numbers never went above 26**.

We need to decode the message to find a secret word, which is the flag we need to complete the challenge.

## Solution

Looking at the customer list noted in the briefing, we can see we
have a number of customers followed by a sequence of numbers. The fact
that these numbers never go above 26 is interesting, as there are 26
letters in the alphabet.

it's possible we're looking at a simple substitution cipher, where for example the letter A is *substituted* for 1, B for 2, and so on through to Z and 26. You can read more on the subject in the [Substitution ciphers](SubstitutionCiphers3.3.1.md) page of the Field Manual.

Let's try swapping back the numbers to the corresponding letters
based on the assumption above (1 = A, 2 = B, 3 = C etc). Alternatively,
we could also search for an online tool to convert these numbers for us.

> 20, 8, 5 = the
>
>
> 19, 5, 3, 18, 5 20 = secret
>
>
> 23, 15, 18, 4 = word
>
>
> 9, 19 = is
>
>
> 23, 8, 5, 5, 12 = wheel

Nice! We've successfully decoded the message and we now know the secret word: **wheel**. The briefing tells us this is the flag we need, so we can submit "wheel" in the toolbox on the left to complete the challenge.

## Real-world Uses

While no longer considered a good means of securing messages, this
type of substitution cipher is so named because Julius Caesar used it in
 his private correspondence! Infact, some of the best early methods of
encryption involved simple schemes based on this, which simply shifts
plaintext characters through the alphabet.

It's typically not used much today, but this and variations based on
it, were used for decades. Of course with the advent of computers and
the internet, it's a well documented cipher and can be automatically
decrypted by tools readily available. This means it's not really used
for much these days - aside from an important part of cryptographic
history that all budding ethical hackers should know of.

<div align="center">

[← Previous: 8.03.02 - Broken Banks](BrokenBanks8.3.2.md) | [Next: 8.03.04 - Race To Where →](RaceToWhere8.3.4.md)
:-|-:
