### WEB
# Dev Tools Introduction

<div align="center">
  <video src="https://github.com/alphyos/Cyberstart-2023/assets/116646389/f47ee800-670e-4c68-9d93-cb374e0c3d62" width="800" />
</div>

# Explore Behind The Curtain

When you interact with a web app, all kinds of transactions are occurring in the background. There is a lot of code and complexity behind the wonderful, simple and powerful exchanges you have with websites online. Your web browser may be interpreting code, sending off small updates as you interact with the site, or receiving data from the server to continuously update what you see. Being able to understand what is happening behind 'what you see in front of you' will help you understand web applications, and how they might be attacked.

There are lots of popular browsers out there, but each of them has Developer Tools which allow you to gain insights and perform actions. These tools can be accessed a number of ways such as via the browser dropdown menu, right-clicking on the page and choosing `Inspect`, or using shortcuts such as `CTRL+U` or `F12`.

A browsers suite of dev tools includes the Console where you can view errors, messages and run commands, the `Inspector` where you can review and modify page elements and the Debugger which allows you to analyse code and replay attacks. Beyond these you'll likely find the Network tab interesting, as it allows you to review files sent & received that make up the page and Storage which contains data items including cookies (such as session cookies, often related to user login state).

All of a browsers dev tools can help us in our security research, but the Inspector is great to understand initially, as you can view the current HTML structure of the page, perhaps find new links to visit, spot parameters to meddle with, plus perhaps comments left by the developers which might give insight into workings and even vulnerabilities.

> We can use the browser Developer Tools to explore the code behind a web page, find information hidden from sight, change data to test if something interesting happens, or find other resources to access. All very useful whether we are testing an application to find a way in, or understanding how a cyber criminal distributed some malicious code!

### <div dir="rtl">[→ Next: 2.3.2 Console](Console2.3.2.md)
