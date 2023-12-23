# 💼 Dubious Jobs - L03 C04

As part of our work helping the New York branch, we took on the task of monitoring some of the sites the hackers have been looking at - one of which was a job board for graphic designers. We managed to get a **network capture** of one of them viewing a job posting which we suspect has a secret message in it. See if you can confirm that by looking at this pcap (packet capture) file.

**Tip:** The **flag** is in the file.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Have you tried using a tool called 'Wireshark'? It has a follow stream option which can be helpful in identifying traffic. There's also an option to find specific packets. Perhaps try searching for the string "flag" and see would you find.

</details>

## Files

- [job board suspicious packets.pcapng](/assets/dubiousjobs2.pcapng)

<details><summary>

## Step by Step</summary>

- Download the pcapng and open it with Wireshark
- Press Ctrl + F and type `flag` into the search filter and make sure it is on `Packet list`
- Frame 29325 has the flag in the packet name

![Untitled](/assets/dubiousjobs1.png)

`flag: 19guhLoi`

</details>
