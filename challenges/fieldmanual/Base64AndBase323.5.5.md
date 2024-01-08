## CRYPTOGRAPHY

# Base64 and Base32

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/48e3cf12-f2c7-404f-b54b-c72a0a7134b2" width="800" />
</div>

## Transforming data

Base64 is a common encoding scheme for converting complex data to a
simple text based format. Like any encoding scheme, it can be both
encoded and then decoded back to the original data, but in its encoded
form can be easier to store or transfer, especially in more restrictive
scenarios where only text is feasible to use.

One example may be an embedded image in an email; you shouldn't store
 the binary data of the image file in the email file (typically .eml or
.msg format) as the email file format needs to contain just text
contents only. In this case you'd encode the image file as Base64, so
it's in simple text only format and that's then fine to store in an
email file.

Another example may be when you've gained access to a server and need
 to extract a file but transfer means such as SCP aren't available.
Copying & pasting file contents may be a quick solution, but if you
display binary data, copy that and paste it to a new file on your local
machine, it very likely won't result in a working file as not all
machine-readable data is displayable and so some data will be lost in
transfer.

Instead, the contents can be displayed in Base64 encoding, copied and
 pasted into a new file on your local machine and finally decoded back
to the original binary format. This is much less likely to fail as
during transfer (copying & pasting to your clipboard) as you are
dealing with just simple text (Base64 contents), avoiding the original
problem.

The characters in Base64 consist of `a` to `z`, `A` to `Z`, `0` to `9`, `+` and `/` characters and perhaps `=`
 "padding" characters that may show at the end. Between all the encoding
 characters there's 26 + 26 + 10 + 1 + 1, which makes up 64 characters,
hence the name "Base64". On the internet, Base64 is used extremely
widely such as in e-mails and web applications. Note that very often the
 amount of data in Base64 format will be larger than the original data,
as you're representing the same data with fewer characters, but the use
cases often far outweigh this slight drawback.

Base32 is a more restrictive version that uses fewer characters to
express data, so as a result means more characters needed to represent
the original data. Specifically, excluding the `=` padding character, it has 32 characters consisting of uppercase `A` to `Z`, plus numbers `2` to `7` (26 + 6 characters, hence "Base32"). Note that `1` is not used as it could be confused with the uppercase `I`
 character. Having fewer characters than Base64 means it's less
efficient in encoding, but more legible as it eliminates commonly
confused characters.

Base64 and Base32 are not encryption. They're not meant to obfuscate
or obscure data from a potential reader, they simply transform data into
 a different format for storage or transfer. There are many websites,
command line tools and code modules which facilitate conversion to and
from Base64. For example, on the Linux command line, you can use the
base64 command to encode data quickly as follows:

```console
$ echo "How are you today?" | base64
SG93IGFyZSB5b3UgdG9kYXk/Cg==
```

As you can see in the example above, a common way of spotting Base64 encoded data is trailing `=`
 characters at the end (there may be 0 - 2 of these!). This is because
part of encoding the original data is to split data into 24 bit chunks,
and if the chunk is shorter than 24 bits the data is 'padded' to fill in
 the gap, possibly resulting in the '=' characters you see - they're
"filler". Another indication is if it contains alphanumeric characters
(plus `+` or `/` characters) as mentioned previously.

<div align="center">

[← Previous: 3.05.04 - Morse code](MorseCode3.5.4.md) | [Next: 3.05.06 - UTF-8 →](Utf-83.5.6.md)
:-|-:
