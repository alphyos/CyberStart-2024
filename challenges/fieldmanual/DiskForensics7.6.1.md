## FORENSICS

# Disk forensics

Disk
Forensics is the science of extracting information from hard disk
images. After acquisition, you will be presented with an image file,
which is typically in a compressed format such as [EnCase's](https://security.opentext.com/encase-forensic)
 E01 files. This file is produced when imaging a hard drive and is the
most common image format produced during acquisition. Another common
disk image format would be a raw image captured referred to as a 'dd'
image (due to the tool used to collect it). While EnCase may have
created the E01 format, it is commonly used due to its ability to
compress data and store metadata without affecting the original
evidence.

It is useful to note that, technically, this should be referred to as
 the E0 format, as the 1 is interchangeable should the evidence be split
 into many files (E02, E03 etc). However, the industry has settled on
the de facto E01 name.

There are various parts of the file system that can prove useful for
forensic investigations once the image file has been mounted; from
recent document locations, the recycle bin and prefetch to things as
simple as hiding data in different partitions on the disk.

There are many different kinds of file systems, each one structured
differently. They can span across different storage devices that use
different kinds of media. The most common today being the hard disk
drive (HDD).

Examples of disk file systems include FAT(12/16/32), NTFS, HFS,
ext2/3/4, and UNIX. File systems such as FAT (File Allocation Table) and
 UNIX store directory information as a simple flat file. This is
different to NTFS, as NTFS provides indexing and efficient storage of
large data for fast lookups.

[← Previous: 7.05 - Memory](https://play.cyberstart.com/field-manual/7ec662f8-fde1-11ec-b939-0242ac120002)
[Next: 7.06.02 - Disk capture →](https://play.cyberstart.com/field-manual/8e94a08c-fde1-11ec-b939-0242ac120002)
