# 🖊 Report Part Two - L01 C04

One of our agents in the field has just put a **packet capture** from the suspected employee's computer on our internal drive for you to take a look at. Can you use it to help finish off the second part of the forensics report we're preparing for the client?

**Tip:** Analyze the packet capture to get the right information to put in the report.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Try looking up HTTP request methods and follow the 'stream'.
```

</details>

## Files

- [employee.pcapng](/assets/reportparttwo1.pcapng)

<details><summary>

## Step by Step</summary>

- Download the pcapng from the left and open it with Wireshark
- Right click frame 14 and follow the HTTP stream
- All of the information is in the conversation including the first name of the user

![image of finished report](/assets/reportparttwo2.png)

- Fill out the report and submit to get the flag

`flag: unH0os2S9MnYneK2LfGG`

</details>
