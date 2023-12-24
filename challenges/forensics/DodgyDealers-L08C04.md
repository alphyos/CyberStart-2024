# 🎶 Dodgy Dealers - L08 C04

To help expand the investigation we've been permitted to do some analysis on the machines of other dealers that weren't under suspicion of being involved, and we've already found something interesting. Take a look at this network capture, an initial analysis has revealed that it might have some hidden messages in it, can you help us figure out what they are?

**Tip:** The flag is in the message.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Raw!

</details>

## Files

- [wraw.pcapng](/assets/dodgydealers1.pcapng)

<details><summary>

## Step by Step</summary>

- Download the pcapng and look for **TCP** packets in Wireshark
- Once found, right click the packet and follow the TCP stream
- Change the format of the text to `Raw` from the default "Ascii"
- Save the file as a `.wav` with the "Save as" button
- Listening to the file will make it obvious what the flag is
  - "The flag is the `MD5sum` of the word `wireshark` all lowercase."
- Put this into a [MD5 Hash Generator](https://www.md5hashgenerator.com/)

`flag: ec7553e42cad6f1007645ba062f7e8ee`

</details>
