## FORENSICS

# Wireshark

[Wireshark](https://www.wireshark.org/)
 is a network packet analyser, and it can be used to troubleshoot and
analyse network traffic. This information can then be used to evaluate
security events and aid in forensic investigations, along with generic
infrastructure troubleshooting.

Wireshark enables you to *sniff* packets going across the
network (which are visible to your computer) and save the packets into a
 file known as a 'packet capture' or, as it is more commonly referred
to, a 'pcap'. Wireshark has a graphical user interface that can let you
examine a packet capture in a visual manner, but there's a command line
alternative also called 'tshark' which can be really useful. Either one
makes analysis of packet captures much easier than it would otherwise
be.

Here are some useful Wireshark filters:

| Filter | Description |
| --- | --- |
| ip.addr | Lists packets with IP address of specified value |
| ip.dst | Lists packets with destination IP address of specified value |
| ip.src | Lists packets with source address IP of specified value |
| tcp.port | Lists packets with TCP ports of specified value |
| udp.port | Lists packets with UDP ports of specified value |
| http.request | Filters all HTTP GET and POST requests |
| http.response | Shows the responses to the HTTP requests, including the response codes |
| dns | Sets a filter to display all packets that contain DNS data |
| tcp contains *\<input>* | Displays all TCP packets that contain a string matching whatever *\<input>* is defined as |

<div align="center">

[← Previous: 7.09.02 - Steghide](https://play.cyberstart.com/field-manual/993adf40-0108-11ed-b939-0242ac120002) | [Next: 7.09.04 - Tcpdump →](https://play.cyberstart.com/field-manual/368c9658-0109-11ed-b939-0242ac120002)
:-|-:
