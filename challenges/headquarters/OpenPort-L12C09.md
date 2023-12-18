# 👐 Open Port - L12 C09

Agent 707, it looks like we're having an effect on the morale of the Bulldogs with all the chaos we've been causing! Our inside agent has just picked up some chatter from a small group of the Bulldogs that are planning to splinter off and form their own gang! There's a possibility they might be planning to hijack the trojan horse idea and steal the gold bullion for themselves, so we need to find out what they're up to.

We believe they've set up a port running on an IP address that we've pointed services.cyberprotection.agency at, between ports 19000 and 20000. See if you can connect to it and help us find out what they're up to.

**Tip:** Connect to the port to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: You'll want to use nmap for this. Make sure you specify the port range. If it's not coming up,
   remember there are two types of ports. A normal nmap scan will only check for one type of port by default.
```

</details>

<details><summary>

## Step by Step</summary>

- Open a terminal and run `nmap -p 19000-20000 -Pn services.cyberprotection.agency`
- It should list an open port, for me it was `19991`
- Run `nc services.cyberprotection.agency 19991`
- Hit enter when its seems like the scan is showing up blank
- The flag should appear

`flag: rIT9xIxJ1/78dp8KjN7o`

</details>
