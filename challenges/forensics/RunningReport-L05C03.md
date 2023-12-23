# 🏃‍♂️ Running Report - L05 C03

Ok agent, it's time to start putting together a draft of the report we'll send on to the client and there's some specific information we need that you can help with. We have found the first time and date the hacker attempted to connect to our client's networks, but we cannot determine what their first actions were. Take a look at the network traffic and then see if you can use it to fill out the forensics report form.

**Tip:** Answer the questions to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: What would an attacker need to do before attacking a machine?

</details>

## Files

- [port scan.pcapng](/assets/runningreport2.pcapng)

<details><summary>

## Step by Step</summary>

- Download the pcapng and open it with Wireshark
- This port scan looks at a single ip address which indicates `Vertical`
- The TTL of 128 indicates `Windows`
- The blue highlighted ACK sequences have 6 entries with the numbers:
  - `135, 139, 445, 5357, 6666, and 7443`

![completed report](/assets/runningreport1.png)

- The flag should appear

`flag: lDd0KKJgfjF9QDv289io`

</details>
