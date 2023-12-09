# 🥶 Volatile Memory L03 C05

When our team in New York came across a couple of PCs they thought might have been compromised by the hackers they took some **memory dumps** to **analyse**. Take a look at this one with a tool called **Volatility**, see if you can identify the running processes and see if you can spot any that look suspicious.

**Tip:** The suspicious process is the flag.

```
💡 Hint: After identifying the correct profile, use Volatility to identify the process lists to see the flag.
```
## Step by Step

- Download the memdump.zip file
- Extract the contents and navigate there in a terminal
- Use volatility3 to get a list of processes `volatility3 -f memdump.mem windows.pslist.PsList`
  ![running volatility3](/assets/volatilememory1.jpg)
- One of them has a weird name which is the flag (without file extension)
