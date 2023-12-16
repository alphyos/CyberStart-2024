### WEB
# Introduction to Web Applications

<div align="center">
  <video src="https://github.com/alphyos/Cyberstart-2023/assets/116646389/e2b27c78-cd40-49b4-97fd-ea91db497216" width="800" />
</div>

# Powering The Modern World

Whether you're just visiting a simple website or using a browser to interact with an app that controls complex processes, web technologies have become our interface for so much of what we do today. They've evolved a lot over the years to now provide banking, utilities, shopping, food & drink services, social media and so much more; all of which have complex web apps behind the scenes yet seem to make it look effortless with their user-friendly interfaces. The management of these services is also typically online, providing people at those companies the ability to manage these sites.

When you 'browse' to a website using `http://` or `https://` (the encrypted secure equivalent), a request is sent to the web server that contains the web application. It will typically respond with HTML content, which your web browser uses as a start point of content to show on screen and associated files to load. These often include CSS (files to style the content), images to place in the page and JavaScript (files to make the page more interactive). Let's look at these.

**HTML**, short for Hyper Text Markup Language is often the first set of content to be returned to your browser, and is used to describe the layout of a page, and the contents therein. It describes what image files are needed, plus CSS and JavaScript files also, in order to style the page and add extra interactivity, plus form elements you might interact with (like the email and password fields you would use to log in).

**CSS**, or Cascading Style Sheets, are the files that describe the way the contents are displayed. They provide a way to 'style' elements such as specifying positions, sizes, colours or other properties that impact how elements appear on the page.

**JavaScript**, this is a powerful programming language which can make the page feel really interactive, handle events, play media files, render animations and much more.

# Viewing These in Your Browser

The languages mentioned above provide the basis of the user interface you see in front of you, interpreted **locally** (on your computer) within the browser. Think of them as an instruction set on how to describe a web page, plus how it looks and how it behaves. We can view the content of these files, and others, by right-clicking on the page and choosing `Inspect` or `View Source`. This will show the HTML contents (worthwhile studying to understand the structure of the page) and allow navigation to the extra files such as CSS, JavaScript and more. Do not be put off by the unknowns, many of the terms in these languages are quite logical.

The CSS and JavaScript will often be loaded in the `<head>` section and content you see in the webpage within the `<body>` section. The `Inspect` method is particularly useful, because as you highlight elements it will highlight the corresponding rendered element in the page.

Within the page itself, anytime you take a new action to request new content, such as go to a new page, the cycle of 'request sent to server' and 'response received by browser' (which includes the loading of all new HTML, CSS, JavaScript and other files) begins again.

While CSS is worth learning about, from a vulnerability point of view HTML and JavaScript will be most interesting to us, as they allow us to find new pages to visit and code which describes how the page works. Between these we might find sensitive data or oversights which allow us to manipulate, break and 'hack' the website.

In the following pages we will learn some of these client side languages, but you could spend a lifetime understanding them all really well, so don't forget to search online to learn more as the need or interest arises.

> Modern web applications are a combination of client side and server side technologies, and both of them can be attacked and leveraged by cyber criminals. A security check implemented at either side could be bypassed, so checks and balances are often applied at both!

### <div dir="rtl">[→ Next: 2.2 The Client And Server Side](TheClientAndServerSide2.2.md)
