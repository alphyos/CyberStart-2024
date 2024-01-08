## FORENSICS

# Steghide

One of the most common stegonography tools and the easiest to use is [Steghide](http://steghide.sourceforge.net/).
 Steghide can both hide and extract data in various kinds of file types.
 It is a command line-based tool, so it is important to learn the basic
commands in order to get the most out of it.

Useful commands in Steghide:

| Argument | Description |
| --- | --- |
| info, --info | Display information about a cover or stego file |
| -ef, --embedfile *\<filename>* | Specify the file that will be embedded (the file that contains the secret message) |
| -cf, --coverfile *\<filename>* | Specify the cover file that will be used to embed data within |
| -sf, --stegofile *\<filename>* | Specify the stego file (the created file that contains embedded data) |
| -xf, --extractfile *\<filename>* | Create a file with the name  and write the data that is embedded in the stego file to it |

Example Steghide command:

Show image info:

```console
$ steghide info file.jpg
"file.jpg":
  format: jpeg
  capacity: 2.9 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase:
  embedded file "secret.txt":
    size: 7.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

Extract embeded data:

```console
$ steghide extract -sf file.jpg
Enter passphrase:
wrote extracted data to "secret.txt".
```

There are vast amounts of steganography tools available today. The below are just a few:

**Crypture** - Crypture is a command line tool that
performs steganography. You can use this tool to hide your sensitive
data inside a BMP image file.

**Binwalk** - Binwalk is a tool for searching a given
binary image for embedded files and executable code. Specifically, it is
 designed for identifying files and code embedded inside of firmware
images. It is a very powerful tool and has all sorts of functions!

**Steghide** - Steghide is an open source steganography
software that lets you hide your secret file inside an image or audio
file, without any noticeable change to the visuals or sound. It is a CLI
 based software.

**rSteg** - rSteg is a Java based tool that lets you
hide textual data inside an image. It is able to embed or extract the
data from the file and uses a PIN to add an extra layer of complexity.
The tool is as simple as selecting the image file, entering the PIN and
then entering the text that you want to hide in the image.

**OpenStego** - With OpenStego you can attach any kind
of secret message file in an image file. You can hide images in BMP,
GIF, JPEG, JPG, PNG and WBMP. You can hide data in these files and take
output as a PNG file.

All provide similar functions in examining images for embedded data
and extraction. These tools can also be used to embed your own secret
files into images.

<div align="center">

[← Previous: 7.09.01 - Tools](Tools7.9.1.md) | [Next: 7.09.03 - Wireshark →](Wireshark7.9.3.md)
:-|-:
