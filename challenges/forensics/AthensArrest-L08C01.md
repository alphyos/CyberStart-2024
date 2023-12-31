# 👮‍♂️ Athens Arrest - L08 C01

We're trying to piece together the communications that have been happening between the dealers and the hackers. Luckily for us, a hacker our Athens team recently apprehended was one of those involved. We have a recovered memory dump of his machine. See if you can dig through it to find some key information to go in our initial report.

**Tip:** Fill in the report correctly to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: You'll need previously used Volatility filters along with other plugins for a filescan and export of pst.
>
> Explore the different options to export and view the pst, then answer the questions based on items found within the mailbox (pfftools).

</details>

## Files

- [athens-hacker-comms.zip](https://drive.google.com/file/d/1qXlc3P7ORusQ0erP2-CelogJucxA2PF1/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the file and extract it
- Run `volatility -f filename imageinfo` to get the image type/profile
- Run `volatility -f filename --profile=Win7SP1x64 filescan | grep '.pst’`
- This will produce the name of the pst file and the location which we need to extract it
- `volatility -f filename --profile=Win7SP1x64 dumpfiles -Q 0x0000000032d186d0 --name mail -D /home/agent/Downloads/mail/`
  - You can specify this with any name of the file or directory you want to export this to
- Run `pffexport filename.pst` This will create a new folder to explore
- You want to specifically look at the `Top of Outlook Data Files` and the directories of `Sent Items`, `Calendar`, and `Contacts`
  - Decode any encoded strings from Base64
- The following completed report should look like the following

![completed report](/assets/athensarrest1.png)

`flag: AoDvaBV7Fp89Sa4BQjxK`

</details>
