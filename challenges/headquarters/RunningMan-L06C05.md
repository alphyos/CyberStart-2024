# 🐉 Running Man - L06 C05

The Yakoottees are preparing their break-in, so we're doing a full review of everything they have running. We found a service running on the server services.cyberprotection.agency, port 8203. Connect to the service and find what is on there to see if it's related.

**Tip:** Connect and look at the banner for the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Many ports have services running on them that provide banners, which tell you the service name and sometimes the version. You can connect to a remote port using Netcat, use $ nc -help in the terminal if you need info on usage.

</details>

<details><summary>

## Step by Step</summary>

- Open up a Linux terminal
- Run `nc services.cyberprotection.agency 8203`

![output of command](/assets/runningman1.png)

</details>
