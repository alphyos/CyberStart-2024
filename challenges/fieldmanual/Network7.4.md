## FORENSICS

# Network

Network
Forensics can be described as the forensic investigation of network
traffic and data captured in transit between devices. This technique
aims to provide investigators with insight into the source and
characteristics of an attack.

It is the capture, recording and analysis of network events by
various means, in order to discover the information related to the
attack in question. This network traffic data can be collected from a
host of devices, such as IDS/IPS, switches, network TAPs or firewalls.
This discovery and retrieval of potentially critical evidential material
 relies on a sound knowledge of common application and network
protocols. For example:

* Data link and physical layer (ethernet)
* Transport and network layer (TCP/IP)
* File transfer protocols such as Server Message Block (SMB) and Network File System (NFS)
* Web protocols such as HTTP and HTTPS
* Email protocols such as Simple Mail Transfer Protocol (SMTP)

Knowledge of these protocols is important to analysts and
investigators, as they are required to have a good understanding of what
 'normal' looks like. Anomalies within network traffic then become
easier to spot. In order to analyse this evidential data, forensic
investigators typically focus on a multitude of areas, for example:
NetFlow full packet capture and log files.

NetFlow is the de facto term used to describe capturing meta-data
from network traffic. NetFlow itself is a Cisco technology; other
variants by different vendors are available. NetFlow was designed to
help engineers fault find connectivity issues. Security professionals
realised that it could also be used to baseline network activity and
carry out trend analysis. The benefit of NetFlow to full packet capture
is that on a normal network the storage requirements would be lower, and
 it can be enabled on already existing network infrastructure.

Full packet capture is advantageous, however not routinely deployed
in most organisations due to storage requirements. It allows analysts to
 gain the full picture of the network traffic, enabling them to analyse
this data more accurately and draw conclusions. Data from full packet
captures can be examined using tools such as [Wireshark](https://www.wireshark.org/) and [tcpdump](https://www.tcpdump.org/).

Log files gained from routers, proxy servers, web servers, IDS/IPS
devices etc. are another way of further investigating useful information
 related to the specific incident and the activity on the network. This
log data can be manually parsed, however most organisations now present
them in Security Incident and Event Management Systems or SIEMS. This
gives analysts even more options when dealing with log files, as custom
rules can be created to focus on specific network activity, improving
the overall value of the investigation.

[← Previous: 7.03 - Steganography](https://play.cyberstart.com/field-manual/675ba65a-fde1-11ec-b939-0242ac120002)
[Next: 7.05 - Memory →](https://play.cyberstart.com/field-manual/7ec662f8-fde1-11ec-b939-0242ac120002)
