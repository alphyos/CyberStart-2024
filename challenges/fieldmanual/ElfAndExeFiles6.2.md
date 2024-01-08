## BINARY

# ELF and EXE files

ELF and EXE files are a type of binary container that contains what you need to run a program.

You might be familiar with EXE files already; they're an executable
file format for use in Microsoft Windows operating systems. An ELF is
most commonly used on Linux, and stands for Executable and Linkable
Format. It is a standard file format for executable files, object files
and shared libraries.

The PE format (Portable Executable), or PECOFF as it is more
completely known (Portable Executable Common Object File Format), allows
 executables, object code and DLLs to be mapped and executed. This
standard file format provides broadly the same capabilities as an ELF.

Over time these standards are upgraded to support new features and
architectures. For example, opening an EXE with a hex editor you will
find sections that report the minimum CPU you need and whether the
binary is 32-bit or 64-bit. This did not exist in the earlier days of
computing!

If you want to check what kind of file you are dealing with you can use the `file` command, e.g.

```console
$ file file.exe
file.exe: PE32 executable (GUI) Intel 80386, for MS Windows

$ file /bin/ping
/bin/ping: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7e20c8bbbcf57159cb93bc4cb3bb5a58978fde5a, for GNU/Linux 3.2.0, stripped
```

This will confirm the file type and various properties of an ELF or
EXE. There are also helper utilities that can tell you even more about
such a file, for example `readelf`. This is not always installed by default but can output all the headers for a file, e.g.

```console
$ readelf -h /bin/ping
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
 Version: 1 (current)
 OS/ABI: UNIX - System V
 ABI Version: 0
 Type: DYN (Shared object file)
 Machine: Advanced Micro Devices X86-64
 Version: 0x1
 Entry point address: 0x4800
 Start of program headers: 64 (bytes into file)
 Start of section headers: 70920 (bytes into file)
 Flags: 0x0
 Size of this header: 64 (bytes)
 Size of program headers: 56 (bytes)
 Number of program headers: 13
 Size of section headers: 64 (bytes)
 Number of section headers: 29
 Section header string table index: 28
```

This will output the entry point (where execution starts) and various sizes and flags.

> Broadly speaking a binary executes with the permissions of the
> running user. That means if you can modify a binary run by a more
> powerful user, you can potentially change the code to do things you're
> not supposed to be able to do. This is privilege escalation!

<div align="center">

[← Previous: 6.01 - Introduction to binaries](IntroductionToBinaries6.1.md) | [Next: 6.03 - Compiling a binary →](CompilingABinary6.3.md)
:-|-:
