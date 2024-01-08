## FORENSICS

# Email

Email
forensics and analysis is used to study the source and content of email
messages as evidence. It is used to help identify the actual sender/date
 and time, subject and so on. There's a whole host of ways in which this
 can be performed, for example investigating metadata, listing protocols
 and ports used and keyword searching. We can also utilise techniques
described in memory forensics to use Volatility to extract .pst files
out of memory.

With cyber criminals increasingly using techniques such as phishing
emails, spam etc., the ability to investigate the source and content of
an email, and present it in a valuable way for evidence, is extremely
important in the world of forensics.

## PST Files

PST (Personal Storage Table) files are personal folder files in
Microsoft Outlook. They store information such as calendar events,
copies of messages, notes and other items. Once extracted from memory,
there are tools such as [pffexport](https://manpages.ubuntu.com/manpages/trusty/man1/pffexport.1.html)
 that can be used to browse the PST and discover various useful pieces
of information, including sender addresses, subjects and attachments.

## Base64

Data in emails is often encoded into Base64 in order to be safely
transferred to its desired location. The packets of Base64 data within
the email can be decoded and plain text can be seen using tools such as
CyberChef, a tool developed by GCHQ. To learn more about Base64, visit
that section of the Field Manual to understand this encoding format
better.

For more information on Base64, check out the [Base64 and Base32](Base64AndBase323.5.5.md) page in the Cryptography chapter.

<div align="center">

[← Previous: 7.06.04 - Deleted files](DeletedFiles7.6.4.md) | [Next: 7.08.01 - Registry and prefetch →](RegistryAndPrefetch7.8.1.md)
:-|-:
