# 🦒 Social Safari - L04 C01

One of the customers who had their laptop hacked was kind enough to let us take a look. We believe the hacker social engineered them into downloading a file from a website which turned out to be malware. That gave the hacker a backdoor to the system, from which they then laterally moved across the network. Can you figure out how they did it?

**Tip:** The flag is the remote computer name.

**Note:** The files for this challenge are the same as Level 4 Challenge 3 and only need downloading once.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Look at the login type to determine if someone logged in from a remote source. Not all remote logins show as type 10 logins, think of different types of sessions and where they would be.

</details>

## Files

- [hacked_laptop.zip.001](https://drive.google.com/file/d/1vmb1lQL77sZQSA4_-2Ie0uy_BNL5M5K4/view?usp=sharing)
- [hacked_laptop.zip.002](https://drive.google.com/file/d/1v1YTYumY-ZXuQHmdXw_yZXpgQH24HqKu/view?usp=sharing)
- [hacked_laptop.zip.003](https://drive.google.com/file/d/1O8b1pQCej2w77hZGvMdP_Cf16GK3OcBV/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the files
- Run `cat hacked_laptop.z* > laptop.zip` to combine the parts of the image
- Extract and open it in autopsy
- Navigate to `/Windows/System32/winevt/Logs`
- You will see a long list of event logs, the one of interest is called `Microsoft-Windows-RemoteApp and Desktop Connections%4Admin.evtx`
- If you look through the text only one connection is to a different computer name
- `RDP-Tcp#2DESKTOP-KHVIA69192.168.80.1`

![autopsy view of the remote computer name](/assets/socialsafari1.png)

`flag: DESKTOP-KHVIA69`

</details>
