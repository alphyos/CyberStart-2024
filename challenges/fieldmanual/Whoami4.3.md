## LINUX

# whoami

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/2bf91748-698e-49c2-9306-28fd0393ea94" width="800" />
</div>

## Finding yourself

The `whoami` command: the name is quite descriptive! As the manual states (`man whoami`) - this command displays the effective user id; i.e. the user we are currently logged in as on the system.

This may seem unnecessary at first. In many terminals the current
user is shown in the 'prompt' (the common portion of text shown before
the input you type), for example:

```console
mainuser@ubuntu: $
```

Here we can see what appears to be the user: `mainuser`.

However, sometimes in security scenarios, perhaps via finding a flaw
that you've managed to exploit, you'll end up with a shell you're
interacting with where it's not quite as obvious which user you're
operating as.

In these cases, it's very helpful to know what user permissions you have. This is where the `whoami` command comes in. When running this command you'll see the user information that might not have been available in the prompt:

```console
$ whoami
mainuser
```

> `whoami` is a short, handy and useful command to help you
> identify which user you're running as. Particularly important when
> you've gained access to a new system and are looking to explore further.

For a more informative view of your user you can also run the `id` command. This will show you your user and associated groups.

## Home directory

Once you know your user, you'll know where to find your home
directory! This is typically where user-specific files are stored; such
as documents, downloads etc. You'll usually find this at `/home/<user>`, for example `/home/mainuser`.

You can easily access this directory using the `~` character to reference the current user's home directory. For example:

```console
$ls ~
Desktop
Documents
Downloads
...

$ls ~/Downloads
image-01.jpg
installer
textfile.txt
...
```

## The root user

The 'root' user is the *superuser* account in Linux. It's
similar to an Administrator account on Windows, and will typically have
the highest access rights on the system.

Unlike a regular users' home directory (under `/home` as detailed above), you'll often find the root users' home directory as its own directory simply named `root`, at the root of the file system - `/root`.

[← Previous: 4.02 - Executing commands](https://play.cyberstart.com/field-manual/8fb65a2c-d7eb-11eb-86fb-0242ac140009)
[Next: 4.04 - Listing with ls →](https://play.cyberstart.com/field-manual/8fb874ba-d7eb-11eb-b539-0242ac140009)
