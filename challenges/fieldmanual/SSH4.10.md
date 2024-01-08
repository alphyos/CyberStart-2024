## LINUX

# SSH

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/9c1bca12-0c59-4387-b4af-9e4b2479ef2e" width="800" />
</div>

## Secure shell

The `ssh` command allows you to connect from one machine to another, providing **secure** access to the connected machine's **shell**.

This is very useful for remote administration of machines. Let's say
you have a server in a data center in another country, and you need to
be able to take control of it. This is exactly what SSH enables you to
do!

> The first `s` in `ssh` stands for **secure**! `ssh` has many excellent security settings and data is encrypted by default.

There are two main components to an ssh connection: the **client** and the **daemon**.

The **client** is the `ssh` tool that lives on the machine you're connecting from, which helps you connect to another machine.

The **daemon** is responsible for hosting a listening
agent on the ssh port (the common default being 22), waiting for
incoming connections and then handling them as they arrive.

Let's break down an example `ssh` command and what it'll do:

```console
$ ssh -p 22 -v mainuser@172.16.6.4
... lots of debug information ...
mainuser@172.16.6.4's password:
... welcome messages ...
Last login: Wed Sep 29 09:36:19 2021 from 172.16.6.1
mainuser@ubuntu:~$
```

Here we see the `ssh` command is run with a couple of arguments and data provided. With the `-p`
 argument we can specify the port to connect to. Here it's port 22 - the
 default - but it may not always be, so you can adjust if needed.

After that you'll see the `-v` argument, which asks for *verbose* output. This is useful for viewing additional information if you're seeing unexpected errors.

Finally, we provide the user and address we want to connect to - `mainuser` 'at' the address `172.16.6.4`.

The above example has the debug information from the `-v` argument trimmed. We then see a request for `mainuser`'s
 password and after this has been entered, we receive the system's
welcome messages and the prompt for the requested user on the
now-connected machine.

At this point, we can do anything that the `mainuser` could do via a terminal on the machine directly - browsing the file system, running commands, inspecting files and so on.

Another argument worth noting is `-i`. This allows us to provide a **private key** file related to the user we're attempting to ssh into, for example:

```
$ ssh -i key.pem mainuser@172.16.6.4
```

That of course means you need the previously created 'key.pem' file.
It's worthwhile looking into these SSH key files if you want to SSH into
 servers regularly, as they provide a higher level of security than
typed passwords.

[← Previous: 4.09 - Stopping program execution](https://play.cyberstart.com/field-manual/8fbecfe0-d7eb-11eb-8e19-0242ac140009)
[Next: 4.11 - The grep command →](https://play.cyberstart.com/field-manual/8fc12286-d7eb-11eb-b542-0242ac140009)
