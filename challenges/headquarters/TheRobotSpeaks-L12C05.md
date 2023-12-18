# 🗣 The Robot Speaks - L12 C05

Agent 707, we have more details about the Bulldogs trojan horse robot. The gang are planning to send the robot to a senior manager as a pretend birthday gift! On the face of it the robot doesn't do anything fancy, it moves around and has an LCD display for messages. But of course, being the Bulldogs they obviously have something more sinister in mind.

We think the LCD display might be used as a way to display secret messages and access codes to someone in the bank. We've managed to get hold of the program, written in Assembly code, that outputs the messages to the display. But it seems to have bad instruction and fails to run. See if you can patch it.

**Tip:** Edit the code and run it, the robots confirmation message will show the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: You'll want to check that all the assembly instructions are valid instructions.
```

</details>

<details><summary>

## Step by Step</summary>

- Change `af` in the `DoMore` line to `al`.

```nasm
section .data
Snippet: db "@E9>06G@Q:CN3C57I<)<)*"
SnipLen: equ $-Snippet
section .text
global _start
_start:
        nop
        mov ecx,Snippet
        mov edx,SnipLen
        mov eax,6
DoMore: add byte [ecx],al
        inc ecx
        inc eax
        dec edx
        jnz DoMore
        mov eax,4
        mov ebx,1
        sub ecx,SnipLen
        mov edx,SnipLen
        int 80H
        mov eax,1
        mov ebx,0
        int 80H
        nop
```

`flag: zrh8v8kmBVNL8zE8EUUV`

</details>
