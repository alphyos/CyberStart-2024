# 🛠 Odd File - L10 C08

Hmm, this is an interesting one for you, Agent 707. We have a file that the Spetzners have been sending back and forth between them for a while. We have no idea what it is or how to get access. We've tried running it and answering the question it asks but to no avail.

Why don't you give it a try and see if you can get access.

**Tip:** Get access to the file to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The program was written in C. What is the largest number that can be stored in a regular integer in C?

</details>

## Files

- [program-x86](/assets/oddfile1)

<details><summary>

## Step by Step</summary>

- Download the file
- Run `chmod +x [filename]`
- Run `./[filename]`
- It tells you that the number is 1000 and to make it a negative while only using addition
- This can be achieved using an integer overflow
- Since the maximum value an `int` variable in can store is `2147483647`, adding that will overflow into the sign bit and make the number negative
- Enter `2147483647` as the number to add to 1000 and you will receive the flag

`flag: zftNrRCk3Yx8xBsAFpJ`

</details>
