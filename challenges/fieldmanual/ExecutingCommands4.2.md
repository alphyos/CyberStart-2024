## LINUX

# Executing commands

Executing
commands on the Linux command line is pretty easy once you know a few
simple tricks and facts. Let us review some of the most important ones,
and then you can practice in the CyberStart Virtual Machine or one of
your own.

## You can execute commands and programs from a shell

If you open the Terminal on your system you get a shell. This is a
command line where you can execute commands by typing them. For example,
 type the following and hit enter.

```console
$ echo "There are $RANDOM bottles of water on the wall"
There are 32057 bottles of water on the wall
```

This should run the echo command, and then print text. If you hit the
 up arrow on your keyboard you should be able to hit enter again, and
run it once more!

## Commands are found in the $PATH

When you type a command like `ping` your Linux system
looks in the locations specified in the path. This is a special variable
 that lists places where commands are expected to be found; locations
like `/bin` or `/usr/bin`. If you want to see what locations are included, you can do so by executing `echo $PATH`. It would look somewhat like the below depending on your system.

```console
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin
```

## You can double tab to find commands that you can't fully remember

Go to your command line and type the letter `p`. Now press the 'tab' button on your keyboard twice. You should see a long list of command names you could run. Now type `pi`
 and double tab again. The list should have reduced to the subset that
match. This also works for directories and files, for example you can
type `cd` and double tab to show possible directories you can change into.

## `apropos` can find matching commands by keywords

Unsure which command to use for a specific use case? `apropos` can help with that by searching the directory of help documentation for commands.

```console
$ apropos list directory
IO::Async::Listener (3pm) - listen on network sockets for incoming connections
acl (5)              - Access Control Lists
acpi_listen (8)      - ACPI event listener
add-apt-repository (1) - Adds a repository into the /etc/apt/sources.list or ...
add-shell (8)        - add shells to the list of valid login shells
...

$ apropos ping
Compose (5)          - X client mappings for multi-key input sequences
a2ping (1)           - - convert between PS, EPS and PDF and other page descr...
avahi-publish (1)    - Register an mDNS/DNS-SD service or host name or addres...
avahi-publish-address (1) - Register an mDNS/DNS-SD service or host name or a...
avahi-publish-service (1) - Register an mDNS/DNS-SD service or host name or a...
...
```

See how they return potential matches for you to try? What a cool way to learn new commands!

## Additional help

If you need some extra info on a particular command you can always try the `-help` argument, or the manual page (`man <command>`). For example:

```console
$ man nc
NC(1)                     BSD General Commands Manual                    NC(1)

NAME
     nc — arbitrary TCP and UDP connections and listens
...

$ nc -help
OpenBSD netcat (Debian patchlevel 1.206-1ubuntu1)
usage: nc [-46CDdFhklNnrStUuvZz] [-I length] [-i interval] [-M ttl]
      [-m minttl] [-O length] [-P proxy_username] [-p source_port]
      [-q seconds] [-s source] [-T keyword] [-V rtable] [-W recvlimit] [-w timeout]
      [-X proxy_protocol] [-x proxy_address[:port]]       [destination] [port]
...
```

## If in doubt, search the Internet!

There are a massive number of Linux commands out there. Some default
and well known and some more obscure for specific problems. You can use
package managers to install new software you might need, or even build
your own binaries. If you are struggling to find the command you need
then search the web! The community of Linux and command line power users
 is huge, and they more than likely have 10 different ways for you to
solve your problem!

<div align="center">

[← Previous: 4.01 - Introduction to Linux](IntroductionToLinux4.1.md) | [Next: 4.03 - whoami →](Whoami4.3.md)
:-|-:
