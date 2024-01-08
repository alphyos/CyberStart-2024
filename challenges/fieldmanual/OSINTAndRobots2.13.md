## WEB

# OSINT and Robots

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/f383bf7c-9969-4dad-8bf3-c945ab3494be" width="800" />
</div>

## Seek and ye might find

Open Source Intelligence, or OSINT for short, is the use of open
source (or publicly available) resources to collect intelligence. Using
social media sites, such as LinkedIn, to get information about employees
 at a company would be one example. Another may be using the careers
pages at a site to see what technologies they list and learn about their
 infrastructure. Perhaps you found some relevant information in the [Wayback Machine](https://archive.org/web/), in an old archived version of a company website.

We are all sharing more information about ourselves that we don't necessarily think twice about and that can be a problem.

The `robots.txt` file on a website (eg `https://example.com/robots.txt`)
 is used to tell search engines which parts of a site (including those
not even linked to from the website itself) they should visit and which
they should avoid. Organisations use this to direct search engines away
from public listings which might reveal hidden pages, such as an admin
login page.

Here is an example `robots.txt`

```txt
User-agent: *
Allow: /registration
Disallow: /admin-management.php
Disallow: /admin
Disallow: /email
```

This is useful information to a search engine, however, it could also be **really**
 useful information to an attacker. Some of these pages might be
intended to be hidden from the public and might reveal useful
information. Perhaps a backup directory with poorly protected files, or
some further intelligence to prime another attack.

If these pages need to be online they should be adequately protected;
 especially as they've been noted in an easily accessible list, commonly
 used by hackers. Backup directories, forgotten experiments and lesser
known services can all be found here, so a potential goldmine for
attackers. While it may not provide a vulnerability or sensitive
information immediately, it may lead to something more serious.

Hopefully you can see why it's important that as security defenders
we can get the same intelligence as the cyber criminals to see what our
exposure is! Thinking like a hacker may just stop a hacker.

[← Previous: 2.12 - Filters in web applications](https://play.cyberstart.com/field-manual/8fa01690-d7eb-11eb-81eb-0242ac140009)
[Next: 3.01 - Introduction →](https://play.cyberstart.com/field-manual/c078b80a-0e8a-11ec-82a8-0242ac130003)
