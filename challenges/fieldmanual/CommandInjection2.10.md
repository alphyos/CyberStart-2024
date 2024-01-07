## WEB
# Command injection

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/50586d9f-1cf8-42e3-9378-a5fb76a4a00d" width="800" />
</div>

# Command Trickery

In this video we walk through an amazing bug class known as command injection. The name is very descriptive! It centres around the ability to trick a server, or app on the server, into executing additional commands through data you supply. Perhaps it's a web app, and it may be intended for users to just supply some data, but what if an attacker could 'sneak' a command in there for it to run too? There are actually all kinds of variations of command injection using different types of inputs, let's look at one now.

Let's say we have an app that receives an IP address input from a user and pings that to check it's available and display the response times. So you may input `4.2.2.1` and the server would reply with information about data communications to that IP address. The code to handle this on the server may include:

```bash
shell(ping -c 4 $USER_INPUT);`
```

In the above example, the 4.2.2.1 IP provided would be used as the value of $USER_INPUT, so the command actually ran would be shell(ping -c 4 4.2.2.1). However, this is a very vulnerable application! What if instead of providing 4.2.2.1 we experimented for potential vulnerabilities and actually provided 4.2.2.1; cat /etc/passwd. This would not only cause the server to execute the ping command as intended, but continue onto the next command too, as there is another chained after the semicolon. As commands are run in succession it would run that 2nd command also, outputting a list of all users on the server. The code ultimately ran was this:

```bash

shell(ping -c 4 4.2.2.1; cat /etc/passwd)
```

The server has effectively just ran `ping -c 4 4.2.2.1; cat /etc/passwd` which outputs this - the expected command first, then our extra command:
```bash
PING 4.2.2.1 (4.2.2.1) 56(84) bytes of data.
64 bytes from 4.2.2.1: icmp_seq=1 ttl=55 time=11.4 ms
64 bytes from 4.2.2.1: icmp_seq=2 ttl=55 time=11.4 ms
64 bytes from 4.2.2.1: icmp_seq=3 ttl=55 time=11.9 ms
64 bytes from 4.2.2.1: icmp_seq=4 ttl=55 time=11.7 ms

`−−− 4.2.2.1 ping statistics −−−
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 11.387/11.593/11.859/0.190 ms
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
...
```

The next step for a hacker may be to begin brute forcing a password for these known users which can give SSH access to the server directly. Until then, at minimum they'd have a working command injection. Note also the user could run any command when chaining multiple commands together! Or they could supply the input `ping -c 4 4.2.2.1; shutdown`. This would shut down the server (assuming the user has the right permissions)!

It's crucial to have the mindset of *don't trust user input*. Firstly, the server is using a command with too much power here - `shell` is too unsafe to sensibly consider, a more restricted solution should be used. Also, considering what the user should be providing (an IP address only), a filter could be implemented to reduce the range of expected characters to only include characters found in an IP address, plus code to validate it is a valid IP would be highly advised before being trusted. If more characters are needed (such as covering IPv6), these could be added to the range after careful review. This is a little like applying 'least privilege' - start with an absolutely safe filter and widen what's accepted as needed and deemed safe to do so. Don't start with maximum and try to reduce down when it's maybe too late.

### <div dir="rtl">[→ Next: 2.11 Cross Site Scripting](CrossSiteScripting2.11.md)
