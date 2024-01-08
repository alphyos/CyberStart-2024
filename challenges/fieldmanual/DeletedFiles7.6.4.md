## FORENSICS

# Deleted files

One of the
key steps in a forensic investigation is to retrieve and index all the
files on the file system. This includes deleted files that have not been
 overwritten and remain on the disk. The process can take a long time to
 complete, but most forensic analysis software will do the search
automatically, building a searchable database with keywords that can be
used to find files of different types.

It's amazing what kinds of information can be found just from the
file system, such as years old MSN and Yahoo Messenger chat logs, full
browser history and so on.

There are ways to securely delete a file, by forcing the operating
system to write over the data, even after it is marked as deleted.
However, this doesn't always work on SSD drives. This is because SSD
drives have a feature known as 'wear levelling', which constantly moves
files around to prevent certain sections of the disk from wearing out
through overuse. This means that even if you try to overwrite a file, it
 may be automatically moved by the disk controller before it can be
overwritten. The only way to truly securely delete from an SSD drive is
to destroy the drive altogether.

<div align="center">

[← Previous: 7.06.03 - File system forensics](FileSystemForensics7.6.3.md) | [Next: 7.07 - Email →](Email7.7.md)
:-|-:
