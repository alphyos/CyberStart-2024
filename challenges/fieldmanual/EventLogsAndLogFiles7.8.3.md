## FORENSICS

# Event logs and log files

Log file
analysis is another major part of being a forensic analyst. Windows log
files can be confusing, as they tend to be filled with vague codes and
identifiers. Reading them is often a multi-stage process of looking up
various codes and looking at the registry and file system to determine
what the identifiers mean.

When a significant or auditable event happens in Windows, the
operating system generates a log file. These are viewed using the
Windows Event Log Viewer. The Event Viewer has a Windows event log
hierarchy, which contains many categories. The main event categories
that are populated on all Windows systems by default are:

* Application
* Security
* System

These logs contain detailed information, such as important hardware
and software actions and different types of logins. All of these can be
used in forensic investigations to further examine suspicious
activities. Each event log contains date/time information, usernames and
 computer IDs, and source and type information.

Also included within the log is an Event ID, which specifies the
event type 4626. These IDs can be searched for using a tool such as [eventid](https://www.eventid.net/) and further information can be gleaned from them.

For example, an Event ID of 4624 is a successful login event and is
generated when a logon session is created. The most common types of log
on fields are 2 (interactive) and 3 (network). All of this information
can be extremely useful in identifying any unexpected or malicious
logons from unknown users.

```txt
Event ID:4624
Source
Microsoft-Windows-Security-Auditing
Level
Success Audit
Description
An account was successfully logged on.

Subject:
Security ID: NULL SID
Account Name: -
Account Domain: -
Logon ID: 0x0

Logon Type: 3

New Logon:
Security ID: SYSTEM
Account Name: JDOE$
Account Domain: CONTOSO
Logon ID: 0x2b5a1cc
Logon GUID: {8d290146-94c0-cb12-53e0-fc3f3e7fa143}

Process Information:
Process ID: 0x0
Process Name: -

Network Information:
Workstation Name:
Source Network Address: ::1
Source Port: 54076

Detailed Authentication Information:
Logon Process: Kerberos
Authentication Package: Kerberos
Transited Services: -
Package Name (NTLM only): -
Key Length: 0
```

By far the most important thing to consider when looking at log files
 is the time zone. Some log files are written according to a specific
time zone, while others are written according to the current system
time. You can look in the registry to find out the system time at the
time the disk capture was made. However, this doesn't take into account
the fact that the time zone may have been different at the time the
event was logged.

Many analysts have been caught out by shifts in time zone, so we
recommend that you convert all time stamps to UTC format across the
entirety of your report.

<div align="center">

[← Previous: 7.08.02 - Prefetch](Prefetch7.8.2.md) | [Next: 7.09.01 - Tools →](Tools7.9.1.md)
:-|-:
