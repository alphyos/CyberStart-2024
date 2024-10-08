# 📄 Float to the Top - L08 C08

Recruit, we're close to foiling The Chiquitoos' plans, but to do so our guy on the inside needs access to the senior members of the gang. The only way he can do that is to pass one of their tests to see if he's got what it takes.

The good news is that we know what the test is. He needs to bypass the security check on a file called "OverflowedBuffer". We've got hold of the file and the test is tonight. Can you do it for him?

**Tip:** Pass the security check to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The program is testing your knowledge of buffer overflows. Although it is only a simulated buffer overflow, the concept is the same. Fill the input buffer with too many characters and see what happens.

</details>

## Files

- [program-x86](/assets/floattothetop1)

<details><summary>

## Step by Step</summary>

- Download the file
- Open a terminal
- Set the execute permission using `chmod +x [filename]`
- Run the program `./[filename]`
- It tells you that the buffer is 20 characters long so any password longer than that will overwrite the memory address after it
- In this case overwriting more than just one memory address will not give you the flag though
- since a memory address is typically 4 bytes (characters) long any string of 24 characters will work
- for example: `abcdefghijklmnopqrstuvwx`

</details>
