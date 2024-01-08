## FORENSICS

# Memory

Memory
forensics refers to the analysis of volatile memory captures taken from
systems of interest. Several tools can be used to capture memory for
investigation. It is useful in cases where breaches have occurred, and
the victim system has been left in a running state. This allows for a
more in-depth investigation of attacks and can provide details of
artefacts that are never written to disk.

Once a memory capture has been acquired, forensic investigators can
then use this to investigate and identify malicious behaviours and
activities that do not leave detectable tracks on a hard drive.

During memory analysis, the computer's RAM (memory) is examined to
retrieve forensic information. There are several tools that can be used
to aid in memory analysis; most notably is a tool called [Volatility](https://www.volatilityfoundation.org/).

## Memory capture

If the target device has not been powered off, then a memory
acquisition should be carried out as a priority task. A memory capture
will be a copy of everything that has been written to RAM since the last
 power cycle. It is possible to find evidence of previously written data
 in RAM, in a similar way to unallocated space on a drive. It's
necessary for the analyst to run the capture software on the machine
itself. Provided that this is fully documented and justified, it will
not have a negative impact to any legal proceedings.

The process of capturing volatile data is a relatively new concept.
The value gained by this process is now being recognised across the
security industry and in law enforcement. A capture of memory can
provide everything that is, and occasionally was, running on the victim
system. Examples of this would be the ability to see running processes,
child processes and orphaned processes, which can be extremely helpful
for identifying any malware on the system. The Windows Registry is also
loaded into memory, which gives the ability to gain access to data even
if the disk was not captured. Files that were opened from an encrypted
source can also be visible in memory in their unencrypted state.

All told, a memory capture is an incredibly useful piece of evidence
to have. It's unfortunate that for a long time analysts have been
trained to pull the plug on a computer as a first step before removing
the hard disk and copying it. Once the computer is powered off, the
volatile data is lost, so there is only one opportunity to capture
memory.

The tools you need to take a forensic memory capture depend on the
target system. For Windows, there is a selection of commercial and open
source tools that can do the job well. The most important thing to do
before using a tool in an investigation is to prove to yourself that it
works. This could be as simple as taking a capture of a test system and
validating that you can see things you know are there. For example, when
 a new variant of Windows is released it is possible that new
anti-malware protections stop, or hinder, the acquisition of memory. The
 most important aspects when considering a forensic tool are reliability
 and repeatability (the ability to perform the same operation on the
evidence more than once and get the same result).

[← Previous: 7.04 - Network](https://play.cyberstart.com/field-manual/72794be6-fde1-11ec-b939-0242ac120002)
[Next: 7.06.01 - Disk forensics →](https://play.cyberstart.com/field-manual/89762f44-fde1-11ec-b939-0242ac120002)
