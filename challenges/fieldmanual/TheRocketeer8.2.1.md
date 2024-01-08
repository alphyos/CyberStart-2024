## WALKTHROUGHS

# The Rocketeer

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we're asked to run a command to help a space agency launch a satellite into space!

## Solution

Initially, we can see there's not really any meaningful interface
given to us to interact with here - no login form to fill in, or
client-side restriction to bypass. This makes sense: the briefing tells
us we need to run a command, rather than interact with the webpage.

One thing that does stand out, however, is a bouncing blue icon
alongside the URL bar in the challenge interface. If we click this, we
can see a new section at the bottom of the challenge pop open - the
Console!

A browser's console allows us to interact with the JavaScript within
the website, or even add our own. Here, the console notes that we need
to paste (or type) the launch command into the command line and submit
it.

Below this message, we can see some text that says "Enter command and
 hit enter". Here, we can type the command we're asked to submit - `launchRocket()` - and hit enter. By doing so, we're actually running the `launchRocket`
 function! This results in the rocket taking off, and the flag showing.
We can copy the flag and submit it to complete the challenge.

The console provided within the challenge is actually a simplified version of a browser's real **developer console**.
 Much like our simple version it allows you to run JavaScript functions,
 as well as inspecting variables, monitoring for errors, running your
own custom script and much more!

You can access the browser's real developer console by selecting the
option from a dropdown option in your browser or shortcuts such as the `F12` key (though there may be other shortcuts for your particular browser).

Try to complete this challenge again, but use the browser's console instead!

## Real-world Uses

While HTML makes up the structure of the page and CSS makes that
structure look visually pleasing, JavaScript really brings it to life
with interactivity, actions and events. However, there's far more ways
to trigger JavaScript than just by clicking the links and buttons within
 the webpage! Here we're making use of the browsers Console tab in its
developer tools, to run an available JavaScript command. Almost all
webpages have JavaScript code used by them and there's usually plenty
available to use - variables, functions, classes and more!

Think about this - if it's available to the webpage to use, it'll likely also be available for *you*
 to use and even better, everything available is discoverable using the
Console tab. If adequate security isn't put in place to protect
JavaScript items, a hacker can run your premade functions at will and
even get to sensitive data, logic and endpoints that they wouldn't
otherwise have. This can lead to security bypasses, data theft and far
worse!

<div align="center">

[← Previous: 8.01.04 - Lazy Locked Login](LazyLockedLogin8.1.4.md) | [Next: 8.02.02 - First Contact →](FirstContact8.2.2.md)
:-|-:
