# ⛰ Uphill Section - L05 C05

We've hit a bit of a stumbling block in our investigation and need your urgent help - our client is planning to do their pitch to the marathon committee in the next few days so we need to get the report finished. Unfortunately, we've received an important pcap containing potentially malicious files from our field agents and it seems to be corrupt. We've been unable to open it. Can you help?

**Tip:** Find a way to open the pcap to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Think about the error message and how you can go about fixing the headers. Perhaps there's an open source tool?

</details>

## Files

- [Taipei malicious capture.pcapng](/assets/uphilsection1.pcapng)

<details><summary>

## Step by Step</summary>

- Download the latest version of [pcapfix](https://f00l.de/pcapfix/)
- Extract the archive and get into the directory
- Run `make` and `sudo make install`
- Use pcapfix on the pcap file: `./pcapfix filename`

![terminal output](/assets/uphilsection2.jpg)

- A file should appear in the pcapfix directory
- Open the `fixed_filename` file in wireshark
- Filter for http traffic
- One of the two packets contains the flag

![wireshark interface](/assets/uphilsection3.jpg)

`flag: Scor3dAwin0nPCAPfor3ns`

</details>
