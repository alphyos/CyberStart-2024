## CRYPTOGRAPHY

# UTF-8

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/c11bd44c-27f9-43da-9759-410fe82b897e" width="800" />
</div>

## UTF-8 and unicode

Unicode is a standard for the consistent encoding, representation,
and handling of text expressed in most of the world's writing systems.
It defines and includes characters from modern and ancient languages,
symbols, emojis and formatting.

Unicode can be implemented by different character encodings, such as
the very popular UTF-8. This is just a subset of what Unicode offers,
but is commonly used as a mechanism of encoding data to display or
transmit. It can be thought of like [ASCII](Ascii3.5.1.md)
 but has significantly greater flexibility and supports a huge array of
simple and complex characters. To put this into context, while ASCII
provides a maximum of 256 character codes, UTF-8 can encode all
1,112,064 character code points! When you send a message to your friends
 including a high five emoji, it'll very likely be UTF-8 that's used, as
 simpler standards like ASCII just don't cater for it.

UTF-8 is very widely used on the internet, and you will find it being
 used as an encoding scheme when interacting with web applications or
databases. This could be because usernames need to be stored and names
that contain characters from say the French, Japanese or Russian
language need to be catered for. Or perhaps formulas are stored and the
complex Math symbols needed.

> You can find lots of UTF-8 converters and Unicode lookup tools on the
> web that can search for a specific value or character. This is useful
> as you are not expected to memorise them all, ha!

Let's look at a simple example, the E-acute letter from the Latin alphabet - `é`. This has a value of `0xE9` and in HTML is often referenced by the value `&eacute;`. In UTF-8 this character is `\xC3\xA9`,
 which is in hexademical format; however you can find the HTML entity
reference, URL encoded reference and more. Just pick the reference that
suits your use case.

Simply put - UTF-8 is part of Unicode standards, and is a lot like ASCII but caters for a far bigger range of characters!

<div align="center">

[← Previous: 3.05.05 - Base64 and Base32](Base64AndBase323.5.5.md) | [Next: 3.06 - Encoding vs encryption →](EncodingVsEncryption3.6.md)
:-|-:
