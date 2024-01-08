## FORENSICS

# Headers and strings

What are
files? A file is just a collection of data. Each file is interpreted
differently depending on the program used to read the file. To a
computer, the file is just a series of 0s and 1s.

Viewing a file as the 0s and 1s would make it much too long, however,
 so we encode them into hex and can then view it with a hex editor, such
 as [Ghex](https://wiki.gnome.org/Apps/Ghex) (a GUI tool) or [hexedit](https://linux.die.net/man/1/hexedit)
 (a CLI tool). We can learn a lot from looking at the raw hex of a file.
 One of the things we can find information on is the file header.

For more information of hexadecimal encoding, check out the [Hexadecimal](https://play.cyberstart.com/field-manual/8fab6bbc-d7eb-11eb-b696-0242ac140009) page in the Cryptography section.

## File headers

Since a file is just a series of 0s and 1s, you need to open the
right file with the right program to get something meaningful. On some
operating systems, the file extension is mapped to a program, so for
example opening a file that ends in '.pdf' would, when clicked, open in a
 PDF viewer. Just because a file ends in a particular extension it
doesn't mean that the file is in the correct format to be read by that
program, however. What matters most is the contents of the file itself.

Within most files there is a file header. The file header is a
sequence of bytes near the start of the file which are essentially a
signature and can reveal the actual type of file you are looking at. If
you were to rename a text file to '.zip', the unzip tool would know it
is not a valid zip file from the file header. The file header is also
sometimes known as the 'magic numbers' or 'magic bytes' of a file. Take
zip files as an example:

`50 4B 03 04` is the file header for a normal zip file with something in it. `50 4B 05 06` is the file header of a zip file which is empty. `50 4B 07 08` is the file header of a zip file has been split into multiple parts.

Many file types have file header associated with them, they are easily searchable online. Additionally, Linux has a tool called `file`
 which is available on most Linux systems by default. The file command
can use a database to look up file headers for you automatically. Here's
 the usage:

```console
$ file filename.txt
filename.txt: ASCII text
```

This will tell you what the file header says the file is, in this case a plain text file that uses the ASCII character set.

## Strings

The file header is not the only useful bit of information you can
find in a file with a hex editor. If you open a binary file in a hex
editor, most will show you the sequences of bytes that when converted to
 ASCII look like words or sentences. This is because the editor will
automatically try to convert the hex data into ASCII text side by side.

Most of the time, the hex was never intended to be ASCII so it will
just produce junk but, if you come across any text in the code, it will
be handily converted for you. There's actually a faster way to go
looking for strings in text files: it's called `strings` and it's a CLI tool, so available within your terminal. The usage is simple:

```console
$ strings hashes-and-text.txt
T$(H
x(H9{(uWH
This is some readable content
;*3$"
l$8M9,$u
And so is this
P+8S+t
H9T$0uIH
```

This will output all the strings it finds in a text file. It will
also produce lots of junk because it doesn't know for sure what is
supposed to be text and what is just data. By default, it will ignore
very short strings, so watch out for that!

<div align="center">

[← Previous: 7.01 - Introduction to forensics](IntroductionToForensics7.1.md) | [Next: 7.02.02 - File integrity and hashes →](FileIntegrityAndHashes7.2.2.md)
:-|-:
