# ⚔ Binary Battle - L11 C04

Agent 707, it looks like we might need your programming skills again. We've intercepted a binary that we want you to take a look at. It takes a password as an argument and produces a result if you get it correct. We think writing a script which uses strings might be the best way to crack it, but none of the other agents have been able to so far.

The file was taken from the hard drive of the gang member we think has been doing reconnaissance on the bank, so it could contain some extremely important information.

**Tip:** Input the right password to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Try to run strings against the binary. You should see a lot of possible passwords. You could try them each one by one, but wouldn't it be easier to write a simple script that will try them all for you?

</details>

## Files

- [strings3-x86](/assets/binarybattle1)

<details><summary>

## Step by Step</summary>

- Download the file
- Use `chmod +x [filename]`
- Run `strings ./[filename] | xargs -I {} ./[filename] "{}"`
- This will run the program with each string the string command yields as an argument
- The flag should show up

`flag: 3rtzdrp0nr3y7qzqiblm7mdw`

</details>
