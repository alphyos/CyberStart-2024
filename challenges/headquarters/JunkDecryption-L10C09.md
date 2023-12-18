# 📆 Junk Decryption - L10 C09

Agent 707, we've just received a bunch of files from one of our field agents taken from one of the senior gang members hard drives, and our team is having trouble putting it all together. Maybe you can help?

Here's what we have: a decryption program which takes a string as an argument, but when we run it we just get junk back; some encrypted text, and; a weird image file of a calendar. A bizarre combination, take a look and see if you can figure it out.

**Tip:** Run the correct string through the decryption program to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: The decryption program only takes in the string as an argument. What could the picture mean,
   and can you think of a way to use it without passing it as an argument to the program?
```

</details>

<details><summary>

## Step by Step</summary>

- On your Linux terminal, download the files provided and run the following commands
  - `sudo chmod +x executablefilename`
  - `sudo sudo timedatectl set-time 2015-08-20`
    - This is because the provided calendar picture is of the date `August 20th, 2015`
  - `./executablefilename NXIS24@ul{}mzVKV`
    - Replace the last item with whatever your included string is in the challenge
- The flag should appear

`flag: HadouKEN[^_^]`

</details>
