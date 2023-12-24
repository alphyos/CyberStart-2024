# 🏝 Island Image - L06 C04

Here's a question for you, Agent 707 - one our team was never able to answer. We have a disk image file taken from the hacker which we know ran a number of oddly named executable files on the target machine, but we don't know what the names mean. Can you unravel the name of one of the programs?

**Tip:** One of the filenames (excluding its extension) contains the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Did you know that Windows has a feature that stores specific data about the applications you run to help them start faster?

</details>

## Files

- [unknown_executable.zip](https://drive.google.com/file/d/1XO-ee6vVocU5sGmDgTAsags0_KGD0SGD/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download and extract the zip file and examine with `Autopsy`
- You are looking for a program that is a prefetch file with the extension of `.pf`
- Looking under **Data Artifacts** and **Run Programs**, you will find many prefetch files but many of these have normal seeming names

![prefetch files in autopsy](/assets/islandimage1.png)

- At the end of this list are a couple odd looking names, copy and paste the name of the very last entry without including the extension and put it through a Caesar Cipher
- You can recognize these file names are odd because they are composed of random letters
- Once decoded, it should produce the flag

`flag: PREFETCHWIN`

</details>
