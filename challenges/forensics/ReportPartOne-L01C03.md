# ✍️ Report Part One - L01 C03

One of the things our agents did whilst in the field was to get a **packet capture** from the suspected employee's computer for us to **analyse**. Can you take a look and fill in page one of the forensics report we're preparing for the client.

**Tip:** Analyze the packet capture to get the right information to put in the report.

```
💡 Hint:Check out a tool called Wireshark, it can help you follow the 'HTTP stream'.
```

## Step by Step

- Download the packet from the left side and open it with Wireshark.
- Frame 6 will show that the request was `successful` and the code is `200`.
- Right click any of the frames and click follow HTTP stream, the flag should be visible in the conversation.
    - `200[REDACTED]agent`

![picture of the form](/assets/reportpartone1.jpg)

- Fill out the report and submit to get the flag.
