# 🗑 Masai Mystery - L04 C05

We've just finished an interview with one of the customers who believed their equipment was hacked whilst on the safari. Intelligence tells us this group encrypt and encode all of their data, along with the encryption key string, before exfiltrating and deleting the files. We have got a copy of the HDD to examine. Can you find the encryption key?

**Tip:** Intelligence tells us that historically the encryption key always starts with the string 'flag:'

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Think about where files go when they are deleted. Also think about how you can look for a specific string in a large amount of text using Linux tools.

</details>

## Files

- [047943a-disk-image.zip](/assets/masaimyster1.zip)

<details><summary>

## Step by Step</summary>

- Download the file
- Open it in autopsy and select the keyword search ingest module
- After waiting some time for the ingest to finish, make a keyword search for `flag:` as a substring match
- There are only two matches, the second one of them is the correct flag

![autopsy view of things](/assets/masaimyster2.jpg)

`flag: Gr3p15th3friendyf1nd3r`

</details>
