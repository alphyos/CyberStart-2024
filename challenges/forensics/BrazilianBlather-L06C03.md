# 🥥 Brazilian Blather - L06 C03

Another bit of evidence you can take a look into, Agent 707 - a packet capture containing an email conversation and attachments from some interactions the hacker had with a gang member in Brazil. Do some analysis and see what you come up with.

**Tip:** Answer the question to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Email attachments require base64 conversion. Make sure you don't miss any questions within the pcap.

</details>

## Files

- [Email_Capture_3.pcapng](/assets/brazilianblather1.pcapng)

<details><summary>

## Step by Step</summary>

- Download the file and open it in a packet analyzer like Wireshark
- Search by typing `tcp.stream eq 2` into the search bar
- Right click any of the packets and follow the TCP stream to see the email conversation
- The first obvious question is further down in the stream and is as follows:
  - "This is what we found, question is: What `year` did AMD release the K6 Processor?"
- A quick google search reveals the answer as `1997`
- The attachment that came with the email is a gzip file, export this object through the export function
- Unzipping it reveals that it is a program which prompts you for a password as an argument
- Using "`1997`" as the password will get you the flag

`flag: C4Tch_M3_1F_Y0u_c4N`

</details>
