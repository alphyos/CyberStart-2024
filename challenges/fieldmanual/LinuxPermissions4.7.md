## LINUX

# Linux permissions

Linux has an
 extensive permission system and modules that can extend it in pretty
incredible ways. It can control who can access specific devices,
processes, or files.

We will focus on the most important and basic file permissions here.
These are the ones that control who can read, write, execute, and a few
special cases.

Linux by default organises permissions around three groups of users:

* The owner. The named owning user, separate from other users.
* The group. For example, you might have a group of users with these rights, e.g. 'Database users'
* All users. The default that applies to all others on the system

Each group may then have a combination of permissions, these are
read, write and execute. For example, if you want to run a program you
need to have the execute permission.

For example, if we list files using `ls -al` we may see the following two files:

```console
-rw-r--r--   1 AgentJ  users    887  4 Oct 13:20 AgentJ.pem
-rw-r--r--   1 AgentJ  users    272  4 Oct 13:24 AgentJ_public.pem
```

Let us draw attention to a few specific elements here. Note the sequence `-rw-r--r--`. The first `-`
 is used for special permissions, so ignore it for now. The next 3
characters are permissions related to the owner (the owner is the first
column after the `1` - AgentJ). Here we see `rw-` -
 that means that the owner can read and write, but not execute. Then the
 group - users (the column after the owner) - can read only, as it
displays `r--`. The final 3 characters are also `r--` which means all users can also only read the files.

If we want to assign permissions we use a numeric representation of
the above sequences. This is a bit more complex and there are numerous
great write ups for you to find online. In an nutshell though r=4, w=2,
x=1. So if you want a user to be able to read, write and execute (`rwx`) they are set to 7 (4 + 2 + 1). If you want them to read and execute (`r-x`), they are set to 5 (4 + 1). Read and write? 6! This means you could write the above permissions `-rw-r--r--` as 644 - 6 for the owner, 4 for the group and 4 for all users.

What if we want to change these and see how they display? We can use the `chmod` command to change permissions. Let us say we want to change the permissions to `-rw-r-----`. This would be 640 numerically.

```console
$ chmod 640 AgentJ.pem
$ ls -al
-rw-r-----   1 AgentJ  users    887  4 Oct 13:20 AgentJ.pem
-rw-r--r--   1 AgentJ  users    272  4 Oct 13:24 AgentJ_public.pem
```

Note how the 3 characters for 'all users' now show no permissions?

We can also use this command to control the execute permissions. Let
us copy a binary and remove permissions to execute, then add them back.

```console
$ cp /bin/ping ping2
$ ls -al
-rwxr-xr-x   1 AgentJ  users    202944 4 Oct 14:10 ping2
```

Note how ping2 has 'x' permissions? We can take them away!

```console
$ chmod -x ping2
$ ls -al
-r--r--r--   1 AgentJ  users    202944 4 Oct 14:10 ping2
```

See how there are no execute permissions left? You can't run it now!

```console
$ ./ping2
-bash: ./ping2: Permission denied
```

If you want, you can add them back to test the reverse.

```console
$ chmod +x ping2
$ ./ping2
```

> Linux permissions are very powerful, and this is really just
> scratching the surface. They are very well documented, so consider it a
> research assignment to go and learn more. You might find the `suid` and `sguid` rights particularly interesting!

<div align="center">

[← Previous: 4.06 - The cat command](TheCatCommand4.6.md) | [Next: 4.08 - Running programs →](RunningPrograms4.8.md)
:-|-:
