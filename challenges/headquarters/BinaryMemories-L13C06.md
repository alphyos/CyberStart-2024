# 🧩 Binary Memories - L13 C06

Ok, this is annoying. Our undercover agent has just sent us a file he managed to take from the gang's primary server, so we think it's important, but when we run it nothing happens. We think it might be loading something into memory, any ideas?

**Tip:** gdb unscramble

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Perhaps use other reverse engineering methods to examine the program.

</details>

## Files

- [program-x86](/assets/binarymemories2)

<details><summary>

## Step by Step</summary>

- `ltace program`
- `strcat` is being run with the same line over and over adding three characters each time.
- Take those three characters and combine them into one string

![image of ltrace](/assets/binarymemories1.png)

`flag: r4nd4tfunall4is444dOm`

</details>
