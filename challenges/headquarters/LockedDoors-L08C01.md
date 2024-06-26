﻿# 🚪 Locked Doors - L08 C01

Recruit, another piece of field work for you.

We want to test the internal door locks on the ship - and how better than to let one of our most promising agents (you!) try and hack into it!

Take a look at this lock. It has some binary numbers, can you figure out how to get in?

**Tip:** Break through the lock to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Hmm, one of the other agents mentioned that it might be XOR.
>
> XOR stands for Exclusive OR. This means that when two numbers are the same, you put a 0, and when two numbers are different you put a 1. So for example, XORing 1 with 0 will be 1, and 1 XORed with 1 will be a 0.
>
> Try using that to compare the top and bottom sets of numbers.

</details>

<details><summary>

## Step by Step</summary>

- Compare the two rows of numbers to each other
  - If the top and bottom numbers are the same, type a 0
  - If the top and bottom numbers are not the same, type a 1
- The flag should appear

![correct xor operation](/assets/lockeddoors1.png)

</details>
