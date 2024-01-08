## FORENSICS

# Tcpdump

[Tcpdump](https://www.tcpdump.org/) is similar to Wireshark, as it can be used to *sniff*
 packets going across the network (which are visible to your computer)
and save the packets into a file usually known as a 'packet capture'.
Tcpdump is a command line tool with no graphical user interface. It
allows the user to display TCP/IP and other packets being transmitted or
 received over a network that the computer is attached to. Along with
printing contents of network packets, it also reads packets from a
network interface card or from a preciously created packet file. Tcpdump
 writes packets to a standard output or file. There are many common uses
 for tcpdump: below are some useful commands.

| Command | Description |
| --- | --- |
| tcpdump -i eth0 | This allows you to investigate what is being transmitted to the interface you specify |
| tcpdump host 10.10.10.10 | This command captures packets where the host is 10.10.10.10 |
| tcpdump src 1.1.1.1 | This command captures from source IP 1.1.1.1 |
| tcpdump dst 1.1.1.1 | This command captures traffic with a destination IP 1.1.1.1 |
| tcpdump net 1.2.3.0/24 | This command lets you capture packets going to or from a particular network/subnet |
| tcpdump -c 1 -X icmp | Allows you to capture packet contents with Hex output |
| tcpdump port 389 | Shows you specific port traffic, use tcpdump src port and dst port to be more granular |
| tcpdump icmp | Or similar will find traffic relating to specific protocols such as TCP, UDP and so on |

Both tools are integral within the field of Network Forensics, in not
 only capturing but also analysing traffic that could potentially
provide evidential value in forensic investigations.

Note that there's a *lot* of traffic if you just run `tcpdump`
 and the logs will pass by too quickly to read. You may want to be more
selective by adding command line arguments to filter and so reduce
traffic, or output to a file for later analysis. Another good tip may be
 to pipe the output to `grep`, so you can not only filter but also highlight data, eg: `sudo tcpdump | grep "search_term_here"`

<div align="center">

[← Previous: 7.09.03 - Wireshark](Wireshark7.9.3.md) | [Next: 7.09.05 - Volatility →](Volatility7.9.5.md)
:-|-:
