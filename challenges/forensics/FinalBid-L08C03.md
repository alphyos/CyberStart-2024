# 🏺 Final Bid - L08 C03

We have a quick task for you. One of our agents was almost done completing a forensics report for the client but got called away, could you help her finish it? There are only two questions left.

**Tip:** Finish the report to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Think about how email attachments are sent in an ASCII format, and how that would be decoded by a mail client.

</details>

## Files

- [Information Update.txt](/assets/finalbid1.txt)

<details><summary>

## Step by Step</summary>

- Download the txt file and copy the huge box of encoded Base64 text which holds all the attachment details
- You don’t need to visualize this data, just decode into Base64 and read the readable text
- It says something similar to the following:
  - "Hello from `Athens`, Our work here is almost complete. The `antique dealers` we have been working with have been instrumental in helping us to hack into the digital auction system. Without them we would be stuck at the script kiddie level! I suspect we will have all we need very soon, you know what you need to do, so just keep doing it. This time next year we will be millionaires."
- Fill out the report with this information:
  - City: `Athens`
  - Working Closely With: `Antique dealers`

![completed report](/assets/finalbid2.png)

- Submit the report and the flag should appear

`flag: Q42df3lOT1CWGFpx9A2P`

</details>
