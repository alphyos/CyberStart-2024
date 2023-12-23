# 💔 Volatile Memory - L03 C05

When our team in New York came across a couple of PC's they thought might have been compromised by the hackers they took some **memory dumps** to **analyse**. Take a look at this one with a tool called **Volatility** and see if you can identify the running processes and see if you can spot any that look suspicious.

**Tip:** The **suspicious process** is the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: After identifying the correct profile use Volatility to identify the process lists to see the flag.

</details>

## Files

- [memdump.zip](https://drive.google.com/file/d/1jD1bEhX4Sqk6f_NChLjilmDDvnOy6u2Z/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the memdump.zip file
- Extract the contents and navigate there in a terminal
- Use volatility3 to get a list of processes `volatility3 -f memdump.mem windows.pslist.PsList`
  ![running volatility3](/assets/volatilememory1.jpg)
- One of them has a weird name which is the flag (without file extension)

`flag: 19hglski!hg`

</details>
