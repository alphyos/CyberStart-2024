# 🏆 Trial by File - L13 C12

Agent 707, we've got what we think might be your toughest test yet. We've intercepted a file which was sent to the gang's boss, so we know it's important, but none of our agents can exploit it. Time for you to show us what you're made of.

**Tip:** Control @ n

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The program has code to prevent it from being debugged. Can you find a bypass? Reverse engineering the binary could also be a good start

</details>

## Files

- [launcher-x86](/assets/trialbyfile1)

<details><summary>

## Step by Step</summary>

- Note that the following is not a good solution. You are encouraged to try and find a better/more clear method to solve this challenge
- First disable ptrace which is used to detect and prevent debugging
- One way of bypassing it is overwriting the ptrace function by including it as a shared library in gdb
- Create this c file and save it as ptrace.c

```c
long ptrace(int request, int pid, void addr, voiddata) {
  return 0;
}
```

- Now compile it as a shared library using: `gcc -m32 -shared ptrace.c -o ptrace.so`
- Set the environment variable `LD_PRELOAD`: `export LD_PRELOAD=./ptrace.so` (this step might not be necessary)
- Set the execute permission `chmod +x launcher-x86` and start gdb `gdb ./launcher-x86`

![terminal view](/assets/trialbyfile2.png)

- Set the environment variable in gdb too `set environment LD_PRELOAD=./ptrace.so`
- Now enter `r` to run the program. This is important because it will update the memory addresses displayed in the disassembly
- You can enter any password you like

![terminal view](/assets/trialbyfile3.png)

- Type `disas main` and keep going down until you see the `<memcpy@plt>` system call
- Set a breakpoint at that address using `break *ADDRESS`
- Now run it again `r`

![terminal view](/assets/trialbyfile4.png)

- Once you hit the breakpoint, examine the stack `x/5x $esp`
- Now make a jump to the second address on the stack
- For example `jump *0xffffd626`

![terminal view](/assets/trialbyfile5.png)

- Now press `c` to continue. You can see from the output that a new process has been spawned.
- Open a second terminal and run `ps -aux` to get a list of all processes. The one you are looking for should be near the end.
- The flag is in that entry

`flag: 1337ReversingofBinary2`

</details>
