# 🐢 Kappa’s Hidden Secrets - L10 C07

In what we thought was an unrelated piece of intel, one of our field agents monitoring the gang reported this morning that he noticed one of them looking at a site which sells pencils. Well, it seems they're using it for something else too - to hide files.

Luckily for us, we think the site is vulnerable to command injection. See if you can use the comment form to get access and find a file, we think it has a list of the gang members involved in the planned robbery and their particular role in the attack, so it's vital we get our hands on it right away.

**Tip:** Find the file, it contains the flag.

```txt
💡 Hint: Hmm, one of the other agents has taken a quick look and he thinks all command injection characters are
   filtered except for `$(command)`. He also suggested using `ls` to find the file.
```

## Step by Step

- At the bottom comment section, type the following and hit enter
  - `$(ls ..)` shows you where the flag is located
  - `$(cat ../flag.txt)` gives you the flag

`flag: 0dL6irM1XSgLRbtn3nVD`
