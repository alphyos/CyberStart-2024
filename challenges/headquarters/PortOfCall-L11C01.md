# 🥌 Port of Call - L11 C01

Quick job for you Agent 707. We think the gang have a port running between 14000 and 15000 that might expose some interesting information about them, we've temporarily pointed our domain `services.cyberprotection.agency` to their server. Use that address to find the service and connect to it.

**Tip:** Connect to the port to get the flag.

```txt
💡 Hint: You'll want to use nmap for this. Make sure you specify the port range!
```

## Step by Step

- Open a Linux terminal
- Run `nmap -p 14000-15000 -Pn services.cyberprotection.agency`
- Run `nc services.cyberprotection.agency 14444`
- The flag should appear

![running netcat](/assets/portofcall1.png)

`flag: Dc4GChlyxd3jkTmapRcQ0S`
