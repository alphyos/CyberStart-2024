## WEB
# Cookies and sessions

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/1cc849d3-0ef3-40c5-ae05-07f94006a1c7" width="800" />
</div>

# Want a Cookie?

Cookies and sessions can seem daunting, but with the basics understood the workings really make sense.

# Cookies
Cookies are used for a variety of purposes such as storing tracking information, data used to enable an application or associating with sessions.

Cookies typically store a combination of **name**, **value**, **expiry**, **domain** and **path**. These 5 parts are fairly common and when omitting any of these, the browser will use a default value. As a simple example, we might set a cookie **name** of `username`, a value of `jameslyne`, an expiry value of 30 days from now, the `example.com` domain and a path of `/`.

This information is retained in the browser between page loads and even computer restarts, and is applicable until the expiry date (or manually cleared). A website will only be able to read that cookie data if it's the same **domain** specified in the cooke, as well as the same **path**.

Sometimes however, we want to store some sensitive information. There are industry recognised approaches such as `JWT` (JSON Web Token) where you can encrypt, to some degree, the sensitive data. It's not bulletproof by any means, but useful to mask sensitive data from the vast majority.

# Session Cookies

There's also the well-used approach of a **session cookie**. This cookie contains only a unique reference, which is available for every page request made to the server. The server has a record of that ID and sensitive data is recorded against it, keeping the data on the server-side away from prying eyes.

For PHP based sites, you'll commonly find a cookie with a name of `PHPSESSID` and a long unique looking value such as `518378383afc122059ee9d8a8ec7b9e1`. On page load all associated cookies are sent to the server. PHP will spot the cookie with name `PHPSESSID` and check if there's a session for that unique value. On discovering there is, it can retrieve the associated session data and use it in combination with processing the page request. A typical example is after you're logged in, all subsequent requests have this cookie name & value sent, to identify you for subsequent pages and keep you 'logged in'.

Of course, if an attacker could get the session ID for a user they could set that in their browser cookie, reload the page and take on the same state as the user; logged in and able to access their account, for example. To prevent this from happening a long, unique session ID is needed. There's plenty of server side logic that could also be implemented including changing the session ID on page requests and enforcing high security standards.

The session information by default tends to be in a file on the server, but could also be in server memory or a database. All are viable storage means and have their pros and cons. The main feature of these approaches is that the sensitive data is on the server and not kept in the browser at all. As we know from the [client and server side](TheClientAndServerSide2.2) field manual module, the server side has higher trust because users can't directly tamper with it.

### <div dir="rtl">[→ Next: 2.8 SQL Injection](SQLInjection2.9.md)
