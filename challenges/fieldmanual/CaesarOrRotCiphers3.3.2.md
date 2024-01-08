## CRYPTOGRAPHY

# Caesar or ROT ciphers

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/83f33272-1e68-4748-a2d0-e18cbd306a8d" width="800" />
</div>

## ROTating the alphabet

The Caesar Cipher, or 'ROT' is a very simple and a wonderful way to
demonstrate how information can be hidden from, and transmitted under,
prying eyes. At the same time it is a great demonstration of how
attackers can recover this data through analysis and how over time
security needs change. The Caesar Cipher is named after Julius Caesar
who used it in his private correspondence. You may also hear to it being
 referred to as ROT-13, which is essentially rotating the alphabet by 13
 places. This is not the only version of this cipher procedurally, but
the most common one. Here is a brief example using this offset:

```txt
offset = 13
T + 13 = G
E + 13 = R
S + 13 = F
T + 13 = G
I + 13 = V
N + 13 = A
G + 13 = T
```

You can find lots of code snippets online which will perform these
operations, and lots of online tools too. Here is a script which will
brute force all 26 variations, listing them for you to spot the
potential word. You can find more about how this is coded and the key
concepts in the Programming chapter. Here's the script:

```python
def crack(input):
    # Try an offset of every possibility from 0 to 25
    for i in range(0, 26):
        output = ""
        # For every character in the provided input
        for j in range(len(input)):
            char = input[j]
            # Move the character along by the offset
            newChar = chr((ord(char) + i - 65) % 26 + 65)
            output += newChar
        print ("Combination " + str(i) + " = " + output)

# Output all 26 variations, as letters rotate through the alphabet
# At offset 13 we see "TESTING"
crack("GRFGVAT")
```

A key feature of a Caesar cipher is that as letters hit `Z` and need to move onto the next they'll loop back to start, continuing from `A`
 again. A couple of common ways to decrypt are negatively apply the
offset if known (eg if an offset of +5 was applied, reverse it by
applying -5 to get back to original plaintext), or simply try all 26
offsets, one for each letter in the alphabet and visually spot any words
 within that list, as a list of 26 variations is quite reasonable to
review.

While ROT13 and the more granular Caesar cipher were great methods
for securing messages in Roman times, they're clearly not suitable today
 as people and technology have moved on. 26 variations just simply isn't
 enough when brute forcing is a fairly small task and so today's
cryptography needs billions of variations available to ensure in a
"secure" world, encrypted data stays secure.

There are concerns over quantum computers breaking today's
cryptography easily as they can operate at a whole new level to current
computers. Work has already begun on quantum safe cryptography to ready
us all for the future, rather than be caught out with new technology
used on old standards and putting security at risk worldwide.

<div align="center">

[← Previous: 3.03.01 - Substitution ciphers](SubstitutionCiphers3.3.1.md) | [Next: 3.03.03 - The Arnold cipher →](TheArnoldCipher3.3.3.md)
:-|-: