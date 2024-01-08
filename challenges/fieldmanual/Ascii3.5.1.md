## CRYPTOGRAPHY

# ASCII

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/7b6f2e15-943a-4442-9e07-ed759daf4c12" width="800" />
</div>

## Simple character encoding

ASCII or the American Standard Code for Information Interchange is an
 encoding scheme designed to represent simple text characters on
computers. When a computer stores (or transmits) data, it fundamentally
does so in binary: a sequence of 1s and 0s (or high/low voltage on a
wire). ASCII provides a means of mapping those binary values to
characters we understand. It acts as a way to translate our preferred
method to read and write information (letters, numbers, symbols etc) to
the way a computer prefers (binary). This is primarily done via a
"lookup table".

For instance, the letter `A` has the decimal lookup number 65, which in binary is `1000001`.
 A computer would store that binary value rather than the lookup number
or letter, as it finds binary easiest to work with. When that binary is
loaded from storage and shown on screen for us humans, it will display `A`. The letter `B` has lookup number 66, which is `1000010`
 and so on for more letters in the alphabet. Most ASCII lookup tables
you find online will show a table of characters and the corresponding
values for that character as hex, decimal or binary values.

For example, for the letters 'ABC', you'll see the following rows:

| Character | Hexadecimal | Decimal | Binary |
| --- | --- | --- | --- |
| ... | ... | ... | ... |
| A | 0x41 | 65 | `100 0001` |
| B | 0x42 | 66 | `100 0010` |
| C | 0x43 | 67 | `100 0011` |
| ... | ... | ... | ... |

Hexadecimal may look a little strange - sometimes hex values are prefixed with `0x` or `\x` - however the 'real' values are the next 2 characters (41, 42 and 43
respectively). Considering what a computer would store for the
characters `ABC`, the resulting binary (shown in a typical group of 4 binary values at a time) would be `0100 0001 0100 0010 0100 0011`.

ASCII not only supports alphanumeric characters (that is letters and numbers) but some symbols (such as `!`, `@`, `#`) and control sequences (such as `ACK`, `DEL`, `ESC`).
 However, its complete character set is merely 256 characters and so
only covers the English (well, American) alphabet; that means French,
Japanese, Math, emojis and more not catered for. So how and where are
they stored? Well, we'll learn a little more about how this is handled
later, but essentially there's other, far bigger lookup tables, catered
for by the **Unicode** standard.

> You can always search online for 'ASCII table' to be able to look up
> values! This is useful because often in computer security we are
> analysing codes or hidden data where we may be looking for ASCII data.

<div align="center">

[← Previous: 3.04.03 - Salts](Salts3.4.3.md) | [Next: 3.05.02 - Hexadecimal →](Hexadecimal3.5.2.md)
:-|-:
