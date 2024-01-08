## LINUX

# The cat command

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/65d0858c-8eab-430b-8eda-f11d116c8b84" width="800" />
</div>

## Easy file output

The `cat` command. This command has a lot of functionality! It's often used as *glue* between other commands, however it's also a really quick way to print information from one or more files to the screen.

For example, let's say you're in a directory that contains a file - `starwars`. You can print the contents of that file with the `cat` command:

```console
$ cat starwars
May the force be with you
```

If you had another file - `terminator`, you could inspect the contents of both of them with a single command:

```console
$ cat starwars terminator
May the force be with you
I'll be back
```

Here we've con**cat**enated the two files; hence the name of the command!

The `cat` command isn't limited to text files. You can
inspect pretty much any file, but unless the content is legible text,
you'll likely just see a lot of unreadable jibberish!

```console
$ cat /bin/ping
@@@@��!�!0001�1����P3P3�
����@   �A�
����0888 XXXDDS�td888 P�td������ttQ�tdR�td�
������/lib64/ld-linux-x86-64.so.2GNU�GNU~ Ȼ��qY˓�L��ZX���ZGNUc�cef(��e�m9�2��������1�hd�����������=�"��$OWn
�\_��-����8 #`�S����\*����"��n��#���
...
```

As with most commands, you can get more information from the manual: `man cat`. This will show the various arguments available, such as the useful `-s` to suppress repeated empty lines. Most of the time, however, it's just a quick and easy way to print data.

Note that much like [Changing directories](https://play.cyberstart.com/field-manual/8fb97a90-d7eb-11eb-9f69-0242ac140009), you can use this **relative** to your current directory as above for the 'text' and 'text2' files, or for an **absolute** reference to a file such as the ping example.

Finally, the output from the `cat` command (along with many other commands) can passed along to another command, or saved into another file.

If you want to pass the output along to another command you can use the 'pipe' character: `|`:

```console
$ cat starwars terminator | base64
TWF5IHRoZSBmb3JjZSBiZSB3aXRoIHlvdQpJJ2xsIGJlIGJhY2sK
```

Or, if you want to take the output and put it into a file, you could use the `>` or `>>` operators. `>` will replace any existing content with the new data, while `>>` will append - so be extra careful to use the correct one for your need!

```console
$ cat starwars terminator > moviequotes
$ cat moviequotes
May the force be with you
I'll be back
```

[← Previous: 4.05 - Changing directories with cd](https://play.cyberstart.com/field-manual/8fb97a90-d7eb-11eb-9f69-0242ac140009)
[Next: 4.07 - Linux permissions →](https://play.cyberstart.com/field-manual/8fbbbdf0-d7eb-11eb-9d1f-0242ac140009)
