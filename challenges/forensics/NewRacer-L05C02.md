# 🏎 New Racer - L05 C02

The plot thickens. It seems someone has indeed compromised the company's servers and even set up a new user account named "sshd server". Can you find out what the password is for the account so we can log in and unencrypt the data?

**Tip:** The password is the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The SAM registry hive holds the password hashes. Think about which tools can be used to gain hashes from the registry hives, and online tools that can subsequently be used to crack the hashes.

</details>

## Files

- [Hives.zip](/assets/newracer1.zip)
- [words.txt](/assets/newracer2.txt)

<details><summary>

## Step by Step</summary>

- Download and extract the files
- Install `samdump2` if you do not have it already (`sudo apt install samdump2`)
- Run `samdump2 SYSTEM SAM > hashes.txt` to extract the ntlm hashes

![hashes](/assets/newracer3.jpg)

- Use a password cracker of your choice to crack the hash using `words.txt`
- Hashcat example: `hashcat -a 0 -m 1000 hashes.txt words.txt --show`
- If you are running a VM and hashcat will not work for some reason, try running it on your host instead
- The cracked password is the flag

![cracked hash](/assets/newracer4.jpg)

`flag: D@rj33l1ng`

</details>
