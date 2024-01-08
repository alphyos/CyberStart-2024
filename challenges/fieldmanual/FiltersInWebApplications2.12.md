## WEB

# Filters in web applications

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/0905ce36-225d-4840-a49f-472f111b96a8" width="800" />
</div>

## Keeping user input clean

In this chapter of the field manual we have learned about many ways
that incorrectly processed inputs can lead web applications to
unintended consequences. Command injection, SQL injection and even XSS
are often the result of attackers taking advantage of overly permissive
inputs & outputs.

Sometimes, when developers try to fix vulnerabilities, they do so by
implementing filters. For example, if you have a command injection bug
of `123; cat /etc/passwd` they might filter the character `;`.
 This is a short-sighted fix for the command injection bug because there
 are so many other ways to work around this. You can search for XSS
evasion or command evasion or whatever suits your needs to find huge
lists of attack vectors that may get around filtering. In this case we
may be able to simply change the semicolon for a pipe to get it to work -
 `123 | cat /etc/passwd`.

It is beyond the scope of this course to cover the development and
language specific ways to correctly restrict inputs, but very often it
comes down to restricting types and whitelisting data. If you know that
you expect the user to provide a number between 1 and 20, check they did
 precisely that! If you can ensure that your restrictions are
appropriate to keep the input as safe without frustrating genuine
users, you've hit a good balance.

From an attackers point of view, lots of creativity is maybe needed,
almost to the point of being artistic. If you're attacking your own
software, it can be a good idea to consider "crystal box" testing, which
 is where you have the code input or output points on screen as well as
the site in a browser and try to be creative to get around the code, by
abusing and bypassing the logic you see.

There are great tools out there also to help probe each input and
output point in your site, trying many thousands of variations, but
remember: an automated tool may not really replicate the creativity and
ingenuity of a human. Manual testing is also highly recommended - as you
 code, plus in regular security testing sessions.

[← Previous: 2.11 - Cross site scripting](https://play.cyberstart.com/field-manual/8f9f9f6c-d7eb-11eb-9870-0242ac140009)
[Next: 2.13 - OSINT and Robots →](https://play.cyberstart.com/field-manual/8fa15b22-d7eb-11eb-bd75-0242ac140009)
