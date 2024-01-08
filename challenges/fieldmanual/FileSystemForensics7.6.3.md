## FORENSICS

# File system forensics

File System
Forensics is an extremely broad subject within the world of forensics.
It encompasses things such as digital evidence, which is stored within a
 computer's file system, and areas of investigation within that file
system that can be particularly valuable to forensic investigators. In
order to be able to extract relevant information from the file system,
it is first important to understand how file systems work on a basic
level.

A file system, in terms of computers, can be described as the way
files are named, stored and retrieved. It almost works like a database
or an index, whereby every single piece of data on the storage device
has its own specific location, which is then recorded. This data is
organised into folders called directories, and these directories contain
 further folders and files.

File systems also make use of metadata. This is incredibly important
to forensics, as it documents the date the file was created and
modified, which could be of evidential value if needed in court.

Some commonly used file systems are:

## NTFS File System

NTFS (NT File System, sometimes referred to as New Technology File
System) is the proprietary system developed by Microsoft, and is the
file system that the modern Windows operating system uses for storing
and retrieving files on the hard disk. Forensic investigators can take
advantage of NTFS in order to identify files that once existed in a
given directory. Master File Table (MFT) entries in NTFS provide a
wealth of information and are not completely removed when file deletion
occurs; these files in some cases can be retrieved and investigated.
NTFS directory index entries utilise a $FILE\_NAME attribute to store
information within the index, providing information about the file such
as full file name, creation and modification time, access time, MFT
change time, file size and its parent directory.

NTFS was developed as it provided folder and file security, and
larger files and partition sizes than those of the FAT file system. This
 file system is useful for forensic investigators, as the Master File
Table resides within NTFS. Here data is stored with information on every
 file and directory on the system. This can be an incredibly useful area
 for investigation when carving and extracting files from memory
captures.

## FAT File System

File Allocation Table or FAT is a file system used by operating
systems for locating files on a disk. Files can become scattered around
and divided into different sections. FAT system keeps track of all parts
 of that file and has existed since the invention of personal computers.
 Unlike NTFS however, FAT offers no folder and local security.

FAT32 is a more advanced version and is used on drives up to 2TB.
FAT32 is said to be more storage efficient in comparison with its
predecessor, and ultimately provides better use of disk space.

## EXT File System

Extended File Systems (EXT) (EXT2) (EXT3) are implemented on Linux.
EXT file systems are old and were used to pioneer Linux systems. The
most widely used Linux file system is EXT2.

It is vitally important to understand the basics of the file system.
Throughout the whole process, from acquisition (creating disk images and
 memory dumps), to validation (hashing) and extraction (retrieving data
from acquired medium for forensic investigation), there are parts of
file systems that provide a treasure trove of useful information.

<div align="center">

[← Previous: 7.06.02 - Disk capture](DiskCapture7.6.2.md) | [Next: 7.06.04 - Deleted files →](DeletedFiles7.6.4.md)
:-|-:
