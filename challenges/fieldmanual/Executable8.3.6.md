## WALKTHROUGHS

# Executable

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/2975583d-a04b-4db6-a689-264079cae048"width="800" />
</div>

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we're presented with a selection of files recovered from a memory stick. We're asked if any of them are **executable files**. The name of the executable file, including the file extension, is the flag we need to complete the challenge.

## Solution

Executable files are a type of file that can be *run*; rather than just reading the data, such as text file, the contents can be executed to run code on the system.

There are lots of different types of executable files - a common one you'll likely have seen on a Windows system is `.exe`.
 To try and find the relevant file in this list, we can search for a
list of executable file types and see if we can spot any matches.

After some searching and reviewing, we can spot that there's a simple executable in the list using the `.com` format: `old-bike-parts.com`.
 As the briefing notes, the full program name, including the file type
(.com), is the flag we can submit to solve the challenge.

## Real-world Uses

There are a lot of different types of executable files used for
different contexts and most come with their own file extension to help
identify them. Common types such as `.exe` (which is a Windows executable) are fairly well known, but there's others such as `.com` (a Windows command file which contains commands to be issued to the operating system).

If there's poor filtration in place to help dangerous programs
getting onto a machine, it may only check for executable files and as
part of this look for `.exe` file extensions only. Or perhaps
 it scans the content of the file and as it's not a binary program and
instead contains commands, isn't seen as a problem. This cat and mouse
game of evading detection can mean hackers try other file types, each
which may or may not work. A cyber criminal only needs to get lucky
once, whereas a defender has to be lucky every time!

<div align="center">

[← Previous: 8.03.05 - Mixed Messages](MixedMessages8.3.5.md) | [Next: 8.03.07 - Secret Caesar →](SecretCaesar8.3.7.md)
:-|-:
