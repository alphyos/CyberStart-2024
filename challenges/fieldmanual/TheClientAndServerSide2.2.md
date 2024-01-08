## WEB

# The client and server side

<div align="center">
  <video src="https://github.com/alphyos/Cyberstart-2023/assets/116646389/32ca853d-9a13-4ab0-8e9f-62acf1cc43e6" width="800" />
</div>

## Defining two sides

In the simplest terms, for more complex websites to function there
are two 'sides': the server side and client side. Let's look these both
in a little more depth.

**Server side**, is where the web server is located. It
may be Apache or Nginx based (to name popular web servers) and may serve
 static files, or it may have code (such as PHP) which handle dynamic,
data rich requests. To help in that, server side code may also connect
to a database, such as MySQL. An attacker wants access to the server
side data, but typically can only talk to the web server like a normal
user. They can't just *access the code* which makes it an area of higher trust.

**Client side**, is your browser or web tool, which
connects to the server side. Your client app will request content from
the server, the server responds with something and the browser then
renders it, resulting in the web page you see. The browser knows how to
translate HTML, CSS, JavaScript and other web technologies into the page
 you see in front of you. An attacker can manipulate the client side and
 bypass checks or change code, which makes it an area of lower trust.
Being able to do that on your own system does not necessarily impact
other users, however.

When you visit a web server via your browser the 'index' file
(index.html or index.php for example) is typically the default page a
server will load - unless you request a specific file, which the server
may or may not have, or refuse to output.

The content often returned from a request to the server will be HTML. The HTML 'tags' such as `<html>`, `<body>`, `<div>` and more are not displayed as text, but denote areas of the page structure. Likewise, `<form>` will indicate the start of a form, and may have attributes such as `action` and `method` (eg `<form action="/handle-request.php" method="POST">`) which will send data from the form over 'POST' method to the `/handle-request.php` endpoint when the form is submitted. Sections within the form may include `<input>` fields which may be of regular text, password or other varieties, an example being `<input name="user_password" type="password">`.

You can inspect the content of the page, for example by right-clicking and choosing `Inspect`.
 You can then select and edit those elements, which are updated in the
page you see in your browser. Note these are not being changed on the
server, merely making adjustments to what you see right now. A page
refresh will get the original page content again from the server and any
 local adjustments will be gone.

It's worth noting that while the client side is great for providing rich
 user experiences, it's difficult to provide meaningful security
protections because the user can make adjustments to any client-side
code. With this in mind, strong security should always be implemented on
 the server side.

This concept is crucial when it comes to more advanced web attacks.
You will often be interacting with the server side through a client,
such as a browser or an attack tool. The goal of many of these attacks
is to find ways to impact other user data, or to gain access to the
server. This should not be possible with the design of the web
application you access, but it can be if flaws are found!

> Remember, modifying some text on the client side in your browser
> developer tools only changes this for you and hasn't bypassed the server
> side security!

<div align="center">

[← Previous: 2.01 - Introduction to web applications](IntroductionToWebApplications2.1.md) | [Next: 2.03.01 - Dev tools introduction →](DevToolsIntroduction2.3.1.md)
:-|-:
