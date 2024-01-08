## LINUX

# Changing directories with cd

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/460cb930-d795-418a-9288-293ec7f95b60" width="800" />
</div>

## Time to explore

The `cd` command stands for **change directory**, and that's exactly what it's used for. You'll be using the `cd` command **a lot**, and while it has some extra functionality, there's some basics you'll need to know.

The `cd` command will change to a directory (commonly
referred to as 'dir') based on the additional information you provide.
There are two ways to reference this additional directory information: **absolute** and **relative**.

An **absolute** path starts at the 'beginning' of the file system - the 'root' - which can be pointed to with `/`. For example, you could run `cd /bin` to change to the root of the file system, and then the bin directory.

A **relative** path is based on where you currently are.
 For example: if a directory 'tmpdir' exists within the directory you're
 currently in, you can refer to it 'relative' to your current location
simply with `cd tmpdir`. Notice there's no `/` at the beginning!

If you type `cd` by itself, wherever you are, it will change to your user's home directory (e.g. `/home/mainuser`). Also, if you're elsewhere and want to quickly reference your home directory, you can use the `~`
 character. For example, if you wanted to change to the above 'tmpdir'
directory (assuming it is within your home dir), you could use `cd ~/tmpdir`.

You can navigate through directories one by one, for example running `cd /`, followed by `cd home`, `cd mainuser` and then `cd tmpdir`. You can also chain directories together and accomplish the same thing with `cd /home/mainuser/tmpdir`. It's worth noting that the `/`
 by itself points to the root of the file system, but the '/' character
is also used between dirs to separate them. Think of the '/' at the
beginning as a separator between *nothing* and the first directory. Since there is *nothing* before the first '/', it instead points to the very start of the file system!

One other special use to know: if you want to change to the parent directory, you can do so with `cd ..`. This can also be used multiple times, as well as in between other directories.

For example, let's say you're in your user's home directory - `/home/mainuser` - which contains the above 'tmpdir' directory. You could run `cd ../../home/mainuser/tmpdir/../` and you would end up back in the same directory you're already in! You changed up to the parent dir (`/home`), to the parent dir again (`/`), then back into the `home` dir, into your user dir, into the tmpdir directory and then finally back up to your user dir again.

This is a very widely used command, and you will use it frequently, so get some practice! Don't forget to use `ls` to checkout what's available to know what directories you can jump into.

[← Previous: 4.04 - Listing with ls](https://play.cyberstart.com/field-manual/8fb874ba-d7eb-11eb-b539-0242ac140009)
[Next: 4.06 - The cat command →](https://play.cyberstart.com/field-manual/8fbaa28a-d7eb-11eb-a2b6-0242ac140009)
