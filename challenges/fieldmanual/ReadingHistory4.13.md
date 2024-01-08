## LINUX

# Reading history

## Looking at previous commands

The simplest way to look at previously executed commands is to press
the up and down keys while in the terminal. This will cycle through the
commands that were previously ran in that particular terminal, if any
are available.

However, there are also a couple of helpful tools to better examine the command history. We're going to take a look at the `history`
 command, as well as the bash history. These are really useful from a
couple of perspectives. As an attacker, you might look at history to see
 what the previous user was doing and perhaps find sensitive info or
files of interest. From an analytical point of view it's useful for
troubleshooting issues on systems, as well as for forensically
reconstructing what attackers might have done after breaking in.

Whatever your viewpoint, the `history` command allows you
to look at the previous commands run by the current user. It will read
from what's known as the bash history file, as well as memory, and
output to the screen. Let's take a look:

```console
$ history
    1  ping www.google.com
    2  echo "test" | base64
    3  echo "dGVzdAo=" | base64 -d
    4  cat /etc/passwd
    5  history
```

You can see the previously run commands here, including the `history` command we just ran as the most recent entry.

Another way to view command history is looking at a user's `.bash_history` file:

```console
$ cat ~/.bash_history
ping www.google.com
echo "test" | base64
echo "dGVzdAo=" | base64 -d
```

As you can see, this is stored in the user's home directory (quickly accessed above using the `~`). You'll also notice this file doesn't have *all*
 of the latest commands: some are still stored in memory, only being
written to this file periodically and when finishing a bash 'session'
(such as closing the terminal).

Note that command history doesn't continue forever. You can configure
 at the system level whether it should record nothing, 10 commands,
perhaps 100, a 1000 or more. It's also not perfect; it's possible to
prevent commands from being recorded, as well as remove them from the
history after the fact.

Even so, this can still be useful. It can be a goldmine of
information; what do you type that you wouldn't want an attacker to
find?

> Fun fact! If you don't want a command to appear in the history you can prefix it with a space.

[← Previous: 4.12 - Netcat](https://play.cyberstart.com/field-manual/8fc23310-d7eb-11eb-8b90-0242ac140009)
[Next: 4.14 - Scripting →](https://play.cyberstart.com/field-manual/8fc474b8-d7eb-11eb-8cc8-0242ac140009)
