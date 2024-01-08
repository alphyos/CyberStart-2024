## FORENSICS

# Disk capture

It's very
important to capture the disk received in a forensically sound manner.
The first action is to discover if the hard disk is encrypted with full
disk encryption. Full disk encryption is where the data is encrypted on
the drive when the computer is at rest, but when the computer is on the
data is decrypted.

If the computer is on, you can use a tool such as Magnet's Encrypted
Disk Detector to determine if the disk has full disk encryption enabled
on it. **This is important if the disk is encrypted: do not turn the computer off.**
 An encrypted disk must be imaged while the computer is on. This is
known as taking a live capture. You can do that with something like
AccessData's [FTK Imager](https://accessdata.com/product-download/ftk-imager-version-4-5).

If the computer is on but the disk is not encrypted, then you should
pull the plug on the computer (not a regular shutdown, just turn it off
from the mains) and then remove the hard drive. The hard drive should be
 connected to a write blocker, which is a piece of hardware that makes
it possible to read from a drive but not write to it. This ensures the
integrity of the evidence. The write blocker, with the drive connected,
is then connected to the analyst's computer and the drive is captured.
Again, you can use FTK Imager for this.

FTK Imager and other forensic capture tools will hash the disk image
that was produced. Note down this hash both in the notebook (print it to
 avoid making a mistake and glue or tape it in the notebook), on the
evidence bag and also in a text file that stays with the disk image.
This is in case the evidence is ever in doubt. The disk could be
captured again and hashed to determine if any changes were made during
the investigation. Of course, if a live capture had to be taken as a
result of full disk encryption then the results will not be repeatable
either way.

[← Previous: 7.06.01 - Disk forensics](https://play.cyberstart.com/field-manual/89762f44-fde1-11ec-b939-0242ac120002)
[Next: 7.06.03 - File system forensics →](https://play.cyberstart.com/field-manual/93317250-fde1-11ec-b939-0242ac120002)
