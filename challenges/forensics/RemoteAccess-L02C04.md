# 🎑 Remote Access - L02 C04

After we initially spoke to the owner of the small business as part of our team's initial recon he has been back in touch to let us know that some other **strange things** have been happening on one of the office PC's outside of normal business hours. We think sometime around the **1st of September** the photographer logged onto the business network remotely. Take a look at the log files we have for **login events** and see what you can find.

**Tip:** The name of the account the photographer used to log in is the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Look for account names logged in around that time that don't appear to be normal. Could the file you're analyzing need to be converted from evtx to xml? Grep can be helpful for searching through logs.

</details>

## Files

- [Malicious Login.evtx](/assets/remoteaccess2.evtx)

<details><summary>

## Step by Step</summary>

- Download the file
- You can solve this by just running `cat filename`
- You will see a repeated series of odd characters underneath `UserSid`

![terminal view](/assets/remoteaccess1.png)

- The flag is the highlighted text

`flag: 18ghllshtkQE!`

</details>
