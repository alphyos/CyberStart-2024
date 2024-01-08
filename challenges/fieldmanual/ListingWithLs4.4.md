## LINUX

# Listing with ls

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/026dc491-692b-4f93-bd13-e980db03f594" width="800" />
</div>

## List your way to success

The `ls` command, as the manual notes (`man ls`), will list directory contents. For example, simply run `ls` to show the contents of the directory you're currently in:

```console
$ ls
dir1  file1  file2  ping
```

Depending on the contents of the directory you should see a series of
 files and/or folders. These may have different colours representing the
 different types of items shown. For example, a directory will have a
different colour than a file, and yet another colour for an *executable* file. This is interesting but there's more information we can see.

> Don't forget you can double-tab to autocomplete, as covered in the [Executing commands](https://play.cyberstart.com/field-manual/8fb65a2c-d7eb-11eb-86fb-0242ac140009) page.

There's many arguments we can provide to customise the `ls` command - if we pass the `-a` argument to the command, we can see some hidden files that weren't shown before:

```console
$ ls -a
.  ..  dir1  file1  file2  .hiddenfile  ping
```

Here we can see a new file: `.hiddenfile`. On Linux, any
file that is prefaced with a period is hidden by default. While this
might seem like a potentially shady thing that would be used by
attackers to hide malicious files - and sometimes it is - it's actually
just intended to hide a file from the average user so that you can
easily store settings, preferences, cache information and so on.

You can also see `.` which is a link to the current directory, as well as `..` which is a special link to the parent directory.

We can run the command with another argument - `-l` to show directory contents in long listing format. Rather than provide separate arguments `-a -l` however, we can join them into one, `-al`:

```console
$ ls -al
total 96
drwxrwxr-x  3 mainuser mainuser  4096 Sep  5 09:49 .
drwxr-x--- 21 mainuser mainuser  4096 Sep  5 09:49 ..
drwxrwxr-x  2 mainuser mainuser  4096 Sep  5 09:49 dir1
-rw-rw-r--  1 mainuser mainuser     0 Sep  5 09:49 file1
-rw-rw-r--  1 mainuser mainuser    22 Sep  5 09:49 file2
-rw-rw-r--  1 mainuser mainuser    25 Sep  5 09:49 .hiddenfile
-rwxr-xr-x. 1 mainuser mainuser 76744 Sep  5 09:49 ping
```

This shows us the permissions associated with these files (the first
column of d, r, w, x and -) as well as the file size (the 5th column,
for example 76744 bytes). For more information on the file permission
letters and what it all means, check out the [Linux permissions](https://play.cyberstart.com/field-manual/8fbbbdf0-d7eb-11eb-9d1f-0242ac140009) section of the Field Manual.

As we provided multiple arguments with `-al`, we can still see the hidden file as well as long listing format. It's covering both as requested.

Another useful argument can be provided to show the file sizes as human readable versions instead:

```console
$ ls -alh
total 96
drwxrwxr-x  3 mainuser mainuser  4.0K Sep  5 09:49 .
drwxr-x--- 21 mainuser mainuser  4.0K Sep  5 09:49 ..
drwxrwxr-x  2 mainuser mainuser  4.0K Sep  5 09:49 dir1
-rw-rw-r--  1 mainuser mainuser     0 Sep  5 09:49 file1
-rw-rw-r--  1 mainuser mainuser    22 Sep  5 09:49 file2
-rw-rw-r--  1 mainuser mainuser    25 Sep  5 09:49 .hiddenfile
-rwxr-xr-x. 1 mainuser mainuser   75K Sep  5 09:49 ping
```

Here we can see the file size represented with the more common and human readable `K`.

> You will be using this command a great deal, so get used to it!

[← Previous: 4.03 - whoami](https://play.cyberstart.com/field-manual/8fb7707e-d7eb-11eb-ad95-0242ac140009)
[Next: 4.05 - Changing directories with cd →](https://play.cyberstart.com/field-manual/8fb97a90-d7eb-11eb-9f69-0242ac140009)
