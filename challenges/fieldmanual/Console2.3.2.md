## WEB

# Console

## Fun with JavaScript

The Developer Tools **Console** is a super useful tool
when wanting to interact with JavaScript in a web page. You can see
errors or other messages that are otherwise hidden from view, as well as
 run functions and view the contents of variables. You can also write
and run your own JavaScript - great for automating attacks and deeper
probing of vulnerabilities!

> Working with the Console generally requires at least a basic
> understanding of JavaScript; in particular variables and functions. If
> you haven't already, this is worth looking into!

Let's dive in and see some examples!

Say we have a login page with some code that checks credentials
client-side: with the username and password stored in JavaScript. But
wait! The developer understood this was a potential security risk, and
so the variables are not set in readable code, but instead with some
obfuscated JavaScript to hide the actual values:

```js
var username = '';
var password = '';

(function(\_0x5805ab,\_0x2ca47d){const _0x44ecc9=_0x4485,_0xb77332=\_0x5805ab();while(!![]){try{const _0x397f62=-parseInt(\_0x44ecc9(0xc4))/0x1+parseInt(\_0x44ecc9(0xc5))/0x2*(parseInt(\_0x44ecc9(0xc7))/0x3)+parseInt(\_0x44ecc9(0xc2))/0x4+parseInt(\_0x44ecc9(0xc0))/0x5+parseInt(\_0x44ecc9(0xc3))/0x6+parseInt(\_0x44ecc9(0xbf))/0x7*(-parseInt(\_0x44ecc9(0xc1))/0x8)+-parseInt(\_0x44ecc9(0xc6))/0x9;if(_0x397f62===_0x2ca47d)break;else _0xb77332['push'](_0xb77332['shift']());}catch(_0xcec07a){_0xb77332['push'](_0xb77332['shift']());}}}(_0xdddf,0xe3e12));function \_0xdddf(){const _0x26993e=['629973TmCCsH','2217327BvKgCP','58639dGMTxh','1064490BVJJlE','664lfYPXU','3532608uRXmQw','5648070eQHrpp','1077822YrBWIx','2qUBwcR'];_0xdddf=function(){return _0x26993e;};return \_0xdddf();}function creds(){let _0x146a9c='us',_0xefbe62='er',_0xf5479='pa',_0x2433ee='ss',_0xf23932='wo',_0x606498='rd';username=_0x146a9c+_0xefbe62,password=_0xf5479+_0x2433ee+_0xf23932+_0x606498;}function \_0x4485(\_0x8cd0c1,\_0x91ede){const _0xdddf75=\_0xdddf();return _0x4485=function(\_0x44850f,\_0x790c90){_0x44850f=_0x44850f-0xbf;let _0x9dde75=_0xdddf75[_0x44850f];return _0x9dde75;},\_0x4485(_0x8cd0c1,_0x91ede);}creds();
```

You could probably reverse engineer the obfuscated code (the example
above is quite simple if you know what you're looking for!), however a
much easier solution is to just ask the Console to tell us the value of
the variables `username` and `password` after the page has loaded and, presumably, the obfuscated code has run.

In the Console, you can simply 'run' the commands `username` and `password`, and we're shown the variable contents:

```js
> username
< "user"
> password
< "password"
```

*Note: The `"` surrounding the output are not part of the variable content - they tell us that the variable is a `string` data type.*

Neat, right?!

Now, let's say this login page code also includes the following function for attempting to log in:

```js
const login = function(provided\_username, provided\_password, admin) {
    // If admin is true, give user admin access
    [...]
}
```

We can see there's a parameter - `admin` - which we could use to gain admin access. However, if we attempted to log in the *intended way*, even with the credentials we discovered above, it's likely the existing code will not log us in as an admin user.

However, using the Console we can instead just call this function directly!

```js
> login("user", "password", true)
< undefined
```

In our hypothetical website, we may have just been able to bypass the
 login and gain access with admin privileges, simply by interacting with
 the original JavaScript via the Console. Very cool!

*Note: When calling the function above we're passing in our string versions of the username and password, hence the use of the `"` surrounding each.*

## How to access the Console

While all commonly used browsers have a Console, they're not always
accessed in the same way. If you're unsure of how to access the Console
in your chosen browser, check the appropriate subsection below!

Depending on your operating system, browser and version there are a
few different methods to open the Developer Tools (where the Console can
 be found). If one doesn't work for you, try another!

### Google Chrome

* Right click somewhere on the page and select the "Inspect" option - this will open the developer tools.
* Click `⋮` (typically in the top-right corner) and then "More tools", then "Developer tools".
* (Windows) Press F12.
* (Mac) Select "View" from the browser's main drop-down menus, then go to "Developer" and finally click "Developer Tools".

With the developer tools open, click the "Console" tab to show the console.

### Mozilla Firefox

* Right click somewhere on the page and select the "Inspect" option - this will open the developer tools.
* Click ≡ (typically in the top-right corner) and then "More tools", then "Web Developer Tools".
* (Windows) Press F12.
* (Windows) Press F10 to show the main drop-down menus at the top of
the browser. Open "Tools", then "Browser Tools" and finally "Web
Developer Tools".
* (Mac) Select "Tools" from the browser's main drop-down menus, then go
 to "Web Developer" and finally click "Web Developer Tools".

With the developer tools open, click the "Console" tab to show the console.

### Microsoft Edge

* Right click somewhere on the page and select the "Inspect" option - this will open the developer tools.
* Click … (typically in the top-right corner) and then "More tools", then "Developer tools".
* Press F12. You may be shown a prompt confirming you want to "Open DevTools" - click this button to do so.

With the developer tools open, click the "Console" tab to show the console.

### Safari

* Right click somewhere on the page and select the "Inspect Element" option - this will open the developer tools.
* Select "Develop" from the browser's main drop-down menus, then click "Show JavaScript Console".
* Press Cmd (⌘), Alt (⌥) and C.

If you can't access any of the above, you'll need to enable the
developer tools. First go to Safari's settings, select "Advanced" and
then check the box for "Show Develop menu in menu bar".

If you don't see the console within the developer tools, click the "Console" tab.

<div align="center">

[← Previous: 2.03.01 - Dev tools introduction](DevToolsIntroduction2.3.1.md) | [Next: 2.04 - Manipulating URLs →](ManipulatingUrls2.4.md)
:-|-:
