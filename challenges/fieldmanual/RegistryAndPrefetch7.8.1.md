## FORENSICS

# Registry and prefetch

The Windows
Registry contains a whole host of useful information for forensic
analysis. It is the main collection of configuration settings and
databases within the Microsoft Windows operating system. In order to
access the Windows Registry, the command `regedit` can be typed into the run/search window, and from there you will be presented with the registry.

Each node within the hierarchical tree is called a *key*. Each key has a set of *subkeys*,
 which in turn can have subkeys of their own or values to those keys.
The terminology is confusing, however due to the requirement for
backwards compatibility, Microsoft have said that the naming will remain
 the same.

When the registry editor is opened, you are presented with a hierarchical list of keys. The root level keys are listed:

**HKCR (HKEY_CLASSES_ROOT) -** This key contains file extension association information which allows Windows to know which program to use to open which files.

**HKCU (HKEY_CURRENT_USER) -** This key contains Windows and software configuration related specifically to the currently logged in user.

**HKLM (HKEY_LOCAL_MACHINE) -** This key contains
Windows and software configuration which is specific to the computer
itself and not the logged in users. This 'hive' also contains
information about the current hardware of the computer and device
drivers.

**HKU (HKEY_USERS) -** This key contains user-specific
configuration information for all currently active users on the
computer. Not just the current logged in user, but also any other users
who have previously logged in to the computer.

Within these keys are subkeys, which can be used for analysis.

For example, within the HKLM structure there is a SOFTWARE subkey.
This key contains information such as what programs run on startup (MRU
lists) and what time they run. This could be useful when examining
computers that have malicious applications installed on them.

Another example can be seen in HKLM where the SAM and SYSTEM registry
 keys are referenced. These can be used together to obtain NTLM password
 hashes, which can be cracked in order to gain cleartext passwords to
user accounts.

There are many investigations that can utilise the registry!

When looking at the registry using the built-in Windows Registry
Editor, you will be presented with the registry in a way that Microsoft
has deemed logical. This does not mean that it directly represents what
you will find when carrying out a forensic image.

There are five hives stored on a Windows system. These are:

* SAM
* SECURITY
* SYSTEM
* SOFTWARE
* DEFAULT

We will not be covering what each hive does here, but do recommend
searching online for more information regarding these. For now, be aware
 that the location of a key, subkey or value may be different when
looking at the hives from a forensic perspective.

<div align="center">

[← Previous: 7.07 - Email](Email7.7.md) | [Next: 7.08.02 - Prefetch →](Prefetch7.8.2.md)
:-|-:
