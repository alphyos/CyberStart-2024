# 📨 Ancient Attachment - L08 C02

As part of investigating the ongoing communications between the dealers and hackers, we've been able to recover a mailbox file, extracted from a memory image by one of our analysts. Based on other messages we've seen we think there might be an attachment here with something interesting in it. See what you can find.

**Tip:** Open the attachment to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Have you checked deleted items?

</details>

## Files

- [mailbox.pst](/assets/ancientattachment1.pst)

<details><summary>

## Step by Step</summary>

- Download the file provided
- Run `pffexport filename`
- A newly exported directory should be created, `cd` into this
- Run `cd "/Top of Outlook data file/Notes/Note00001"`
- Run `cat Message.txt` This contains the password for the zip attachment you need to unzip, copy the password
  - `cmVhbGRlYWw=`
- Run `unzip ../../Deleted\ Items/Message00001/Attachments/1_final.zip`
  - When prompted for the password, paste the contents of `Message.txt`
- The attachment should be `final.txt` and extracted to whatever directory you ran the command from, simply use `cat final.txt` to get the flag.

`flag: Ema1l_f0r3ns1cs`

</details>
