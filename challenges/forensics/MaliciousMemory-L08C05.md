# 🚜 Malicious Memory - L08 C05

Breakthrough! We've identified the hacker we think is in control of the group and managed to get hold of a memory dump from his machine. Our analysts in Athens have taken an initial look and believe there are some malicious tools and files hidden in memory, but they're quite small and stored in the MFT. Can you help us retrieve the file?

**Tip:** Find the file, the flag is inside.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Volatility has functions for this that will help. "Malicious Tools" is a keyword. What could the "Password" be?

</details>

## Files

- [athens hackers memdump.zip](https://drive.google.com/file/d/1O2_DKg0-RtDVm3v7n6S-uzq1kawGsIyL/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the file and run `volatility -f filename imageinfo` to figure out the operating system profile
- Run `volatility -f filename --profile=Win7SP1x64 filescan`
- Run `volatility -f filename --profile=Win7SP1x64 mftparser | grep -C 30 "Malicious Tools"`
- With the physical address secured, run `volatility -f filename --profile=Win7SP1x64 dumpfiles -Q 0x19bbc400 -D /home/agent/Downloads/malicious`
- Unzip the file with `7z e filename`
  - The password is `3xtract0r`
- Reading the resulting flag text is in hex, decode this to get the flag

`flag: v0lat1l1ty_MFT_GAM30v3R`

</details>
