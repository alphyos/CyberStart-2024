## FORENSICS

# Volatility

[Volatility](https://www.volatilityfoundation.org/)
 is one of the most widely used memory forensics tools. It is commonly
used in both incident response and forensics. It is used to analyse
memory dumps from 32-bit and 64-bit systems on Linux, Windows, Mac and
Android systems. It can analyse virtual memory dumps, virtual box dumps,
 raw dumps, crash dumps and others types too.

It provides more advanced memory forensic capabilities, such as
investigating running processes and carving data out of memory, parsing
MFT's enabling examiners to extract files from within it. For attackers,
 it can also be used with more offensive Python modules, such as `mimikatz`,
 in order to glean cleartext passwords from memory, and even for
extracting files stored in memory (such as .pst files) from a memory
dump.

Useful Volatility commands:

| Command / argument | Description |
| --- | --- |
| imageinfo | `vol.py -f mem.image imageinfo` (or `volatility -f mem.image imageinfo`). This shows the recommended OS Volatility has identified |
| --profile= | This is where you set the profile discovered in imageinfo and append
 different commands to the end of the command, example syntax: `volatility -f image -profile=Win10x64 pslist`. An incorrect profile selection will produce empty results when used with other modules such as `pslist` |
| pslist | Shows a high-level view of running processes |
| psscan | Scans memory for EPROCESS blocks |
| pstree | Displays parent-process relationships |
| filescan | Scans memory for FILE_OBJECT handles |
| dumpfiles | Extracts FILE_OBJECTS from memory |

Volatility is intended to aid in investigations and to introduce
people to the techniques required to extract digital artefacts from
volatile memory dumps. It does not, however, currently have acquisition
capabilities and other tools are required in order to first acquire
these memory dumps for investigation.

<div align="center">

[← Previous: 7.09.04 - Tcpdump](Tcpdump7.9.4.md) | [Next: 7.09.06 - Autopsy →](Autopsy7.9.6.md)
:-|-:
