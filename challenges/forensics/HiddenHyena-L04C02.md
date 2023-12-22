# 🐆 Hidden Hyena - L04 C02

Our team in Kenya decided to take a page out of the hackers playbook and try sending an agent of their own along on one of the tours to follow a suspect they suspected might be one of the hackers. Our agent noticed them using a particular website which we believe had a secret message on it for him. Take a look at the network capture file and see if you can find anything interesting.

**Tip:** The flag is in the pcap.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Find packet?
```

</details>

## Files

- [Tour Capture.pcapng](/assets/hiddenhyena2.pcapng)

<details><summary>

## Step by Step</summary>

- Download the file and open it in Wireshark
- Press Ctrl + F and search for "html", search until the frame description has a suspicious looking html name

![wireshark search result](/assets/hiddenhyena1.png)

- Copy and pasting this string and putting it through a [Base64 decoder](https://www.base64decode.org/) will reveal the flag.

`flag: hgjks2JFu!hf`

</details>
