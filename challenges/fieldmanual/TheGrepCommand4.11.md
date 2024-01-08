## LINUX

# The grep command

The grep
command is remarkable! It enables you to search files or data for
patterns. It is one of the most powerful and versatile commands out
there!

You will be getting lots of `grep` practice in CyberStart, so here are some helpful command snippets that you can customise:

**Search a file for a specific term with case sensitivity**

```console
$ grep "Search-term" file.txt
file.txt: Here you can find Search-term in the content.
```

**Search a file for a specific term ignoring case**

```console
$ grep -i "Search-term" file.txt
file.txt: Here you can find Search-term in the content.
file.txt: We also have sEarCh-tErm later in the same file.
```

**Search all files in your directory for a matching string**

```console
$ grep "Search-term" *
file.txt: Here you can find Search-term in the content.
another.txt You'll find Search-term was also in another file too.
```

**Search all files in your directory for a matching string, and any directories underneath too!**

```console
$ grep -R "Search-term" *
file.txt: Here you can find Search-term in the content.
another.txt You'll find Search-term was also in another file too.
some-dir/extra.txt The wording Search-term was in a file in a dir too.
```

**Search for a specific term in a file but show some lines before and after**

```console
$ grep -A 1 -B 2 "Search-term" file.txt
file.txt: A couple of lines above
file.txt: the content will show.
file.txt: Here you can find Search-term in the content.
file.txt: Also, one below.
```

This will show 1 line after and 2 lines before, and you can change it as you like!

**Search for any lines that do not match your provided string - invert it!**

```console
$ grep -v "Search-term" file.txt
file.txt: First line of content, always the tops
file.txt: and then the second line here.
file.txt: A couple of lines above
file.txt: the content will show.
file.txt: Also, one below.
file.txt: Notice the matching line isn't output!
file.txt: We also have sEarCh-tErm later in the same file.
file.txt: The above line was shown however (due to case).
file.txt: Last line of file to complete our example.
```

This will show 1 line after and 2 lines before, and you can change it as you like!

<div align="center">

[← Previous: 4.10 - SSH](Ssh4.10.md) | [Next: 4.12 - Netcat →](Netcat4.12.md)
:-|-:
