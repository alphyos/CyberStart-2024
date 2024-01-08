## FORENSICS

# Prefetch

Prefetch is
also another common area of investigation for forensics. It is a feature
 introduced in Windows XP that stores specific data about the
applications you run, in order to help them start faster. Windows
requests data that isn't stored in the disk cache and stores that data
on the hard disk for easy retrieval.

Superfetch is a feature of the Prefetch algorithm. It attempts to
determine which applications you will launch and loads up the necessary
files and data into memory.

Prefetch artefacts are located in `%Windows%\Prefetch`,
which shows a list of applications that have been started. This is
incredibly useful for forensic investigators, as it contains the name of
 the application along with an eight character hash of the location from
 which the application was run. Prefetch data also contains timestamps
and metadata, such as run count and files and directories used during
the application's start up. This enables investigators to spot any
anomalous or malicious looking programs that have been run, which could
be linked to their investigation and used as supporting evidence.

It may be possible to see Prefetch disabled on a machine. This is
typically the case if an SSD is present. In Windows 8 this was a yes/no
option. If an SSD was present then Prefetch was off. In later version of
 Windows, this was changed so that the system could calculate the
performance of the SSD before deciding if Prefetch was needed.

[← Previous: 7.08.01 - Registry and prefetch](https://play.cyberstart.com/field-manual/a82a131a-fde1-11ec-b939-0242ac120002)
[Next: 7.08.03 - Event logs and log files →](https://play.cyberstart.com/field-manual/acc4d57c-fde1-11ec-b939-0242ac120002)
