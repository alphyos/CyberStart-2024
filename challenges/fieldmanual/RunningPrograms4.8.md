## LINUX

# Running programs

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/5598306c-ed28-401f-bae6-ade6baec6a97" width="800" />
</div>

## Standard and custom binaries

Running programs in Linux is pretty important! Maybe you've
downloaded some custom utility you want to run, maybe you've got a
binary you want to work with in a local directory. Generally, you don't
just want to be restricted to the tools provided by your chosen Linux
distribution.

By default there's an important variable in Linux; the `PATH`:

```console
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/snap/bin
```

This contains the various locations where Linux will look for
binaries, or commands, you want to run. For example, if you ask Linux
which `ping` command it uses if you were to run it, it'll be in one of the directories listed in the `PATH`:

```console
$ which ping
/usr/bin/ping
```

Sometimes you might want to run a binary outside the directories listed in `PATH`. If you have a binary file in your current directory, you can run that with the `./` prefix:

```console
$ ./custombinary
bash: ./custombinary: Permission denied
```

Often if this is the first time you're trying to execute a custom
binary file, you'll receive a permissions error similar to the above. As
 we've covered in the [Linux permissions](LinuxPermissions4.7.md) section, you'll need to give this file executable permissions:

```console
$ chmod +x custombinary
$ ./custombinary
I was executed successfully!
```

Much like other commands we've looked at, you can also run a binary with an absolute reference instead of relative:

```console
$ /home/mainuser/custombinary
I was executed successfully!
```

## Processes

A process in Linux is an instance of a program that is currently
running, and any command you execute will create a process. Linux keeps
track of these running processes; you can view them with the `ps` (process status) command:

```console
$ ps --help simple

Usage:
 ps [options]

Basic options:
 -A, -e               all processes
 -a                   all with tty, except session leaders
  a                   all with tty, including other users
 -d                   all except session leaders
 -N, --deselect       negate selection
  r                   only running processes
  T                   all processes on this terminal
  x                   processes without controlling ttys
```

A common command to view running processes is `ps -aux`. The `a` argument shows processes for all users, not just your current user. The `u` argument display's the processes' *owner* (the user who ran the command), and the `x` argument shows processes not 'attached' to a terminal - background processes that haven't been executed from a terminal.

The result of this command is a very helpful output showing running processes with lots of userful information:

```console
$ ps -aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.1  0.5 169388 10376 ?        Ss   09:56   0:05 /sbin/init splash
root           2  0.0  0.0      0     0 ?        S    09:56   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   09:56   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   09:56   0:00 [rcu_par_gp]
root           5  0.0  0.0      0     0 ?        I<   09:56   0:00 [netns]
...
```

In the example here we can see the user the process belongs to, the **process ID (PID)**, performance information, as well as the command that is running if available.

> The process ID is particularly useful if you need to [stop a program that is currently running](StoppingProgramExecution4.9.md).

<div align="center">

[← Previous: 4.07 - Linux permissions](LinuxPermissions4.7.md) | [Next: 4.09 - Stopping program execution →](StoppingProgramExecution4.9.md)
:-|-:
