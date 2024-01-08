## LINUX

# Netcat

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/ad452d31-87f7-433e-860b-517b45a3437f" width="800" />
</div>

## The Swiss army knife of networking

Netcat, while not the most advanced tool available, has a lot of
functionality and is great at what it does. It's often described as the
swiss army knife of networking!

It enables us to connect to various resources using TCP or UDP and
send data. We can use it to do all kinds of things such as building TCP
proxies, servers, testing networking servers and more. There are more
advanced tools such as 'socat' which provide even more functionality,
but part of the appeal of netcat is its simplicity.

To give an example of what we might want to do with it, let's use netcat to connect to a resource on the internet:

```console
$ nc www.google.com 80
GET /
HTTP/1.0 200 OK
Date: Mon, 25 Jul 2022 10:36:36 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
...
```

Here we run the `nc` command, connecting to `www.google.com` on port `80`. Initially, we won't see any output; netcat is waiting for us to tell it what to do. We tell it to `GET` (a type of [web request](WebRequestsAndHttp2.5.md)) the URI `/`. Netcat then gives us the HTTP response from the server.

Note that after we're given the response the connection still remains
 open. You can send additional commands, or if you'd like to exit you
can hit [Ctrl + C](StoppingProgramExecution4.9.md).

That's pretty neat! We can connect to a server and request or send
data. This can also be automated. If you had a file 'request.txt', with
the contents of 'GET /', you could get the same result as the above
command with `nc www.google.com 80 < request.txt` - the `<` feeds the following file into the command. Similarly, you could also run `echo "GET /" | nc www.google.com 80` to instead 'pipe' the command in. These can be very helpful for scripting or other automation involving netcat.

Netcat can also be used as a **server**. If you were to run `nc -l -p 8081`, this tells netcat to listen (`-l`) on port (`-p`)
 1.    Another system could then connect to this port and send data to
netcat; useful if you've gained access to another server and want to
send data back to your own machine!

There is, however, some dangerous functionality to netcat. Older versions used to allow the `-e`
 argument: giving us the option to specify a binary to run when a
connection is initiated. This may still be used by attackers as it can
create a simple backdoor to a system!

For example, by running the command `nc -l -p 8081 -e /bin/sh`,
 an incoming connection to port 8081 would receive shell access to the
machine. If an attacker were able to find a way to run this command,
such as [Command injection](CommandInjection2.10.md) in a vulnerable web app, they could create a backdoor to the server and wreak havoc!

This quick introduction just scratches the surface of of netcat. Be
sure to investigate further, as it'll no doubt become an important tool
in your cyber security journey.

Finally, here are some helpful commands for reference:

**Connect to a server with TCP on port 8081**

```console
$ nc servername 8081
```

**Connect to a server with TCP on port 8081 and send a file**

```console
$ nc servername 8081 < file.txt
```

**Connect to a server with TCP on port 8081 and write any output to a file**

```console
$ nc servername 8081 > file.txt
```

**Listen on port 8081 for connections**

```console
$ nc -l -p 8081
```

**Listen on port 8081 for connections and send a file on connection**

```console
$ nc -l -p 8081 < file.txt
```

**Start a backdoor on port 8081 with a compatible version of nc**

```console
$ nc -l -p 8081 -e /bin/sh
nc: invalid option -- 'e'
...
```

<div align="center">

[← Previous: 4.11 - The grep command](TheGrepCommand4.11.md) | [Next: 4.13 - Reading history →](ReadingHistory4.13.md)
:-|-:
