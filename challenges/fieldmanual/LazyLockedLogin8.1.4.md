## WALKTHROUGHS

# Lazy Locked Login

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, the agency recently purchased a new internet-connected
homehub which has been malfunctioning with unpredictable temperature
changes and light toggles. We've found the settings page and login
credentials to hopefully resolve these issues, however the login form
restricts access unless viewed from a technician's laptop.

We need to work out how to bypass this restriction and successfully log in.

## Solution

As the briefing also notes, the username and password are already
provided for this challenge. The problem is, we can't click the "Enter"
button to complete the login. There's a few ways we could solve this
problem but the simplest route is using the **Developer Tools** built-in to most browsers.

Popular browsers for desktop and laptop computers have a toolbox
available to help website developers in various ways, known as the
Developer Tools. In particular, it enables us to easily poke and prod at
 the client-side code used to run the web page - that is, the code that
has been sent over to your browser (the client). It also allows us to
make modifications to the code, locally, to perhaps route around some
client-side restrictions.

Each browser's tools can be opened in different ways, however we have
 provided a stripped back DevTools Inspector to assist you in completing
 this challenge. To open it, click the **Open Devtools** button in the top-right of the browser. This will open the inspector to the right side of the window.

You should now be able to see the HTML code that comprises this
particular form we're looking at on screen. We can see an HTML comment -
 content that is visible amongst the code itself, but hidden from
display on the webpage: "Developer notes: This will be disabled if page
not accessed from technician's laptop". Underneath this we can see
another element, and notably, a `disabled` attribute on it: `<input ... value="Enter" disabled="">`.

If we click the disabled attribute and hit the **Delete**
 key on your keyboard, we can remove it from the element entirely. When
removed, hit the "Enter" key on your keyboard to save the changes to the
 element. Now, we're able to click the "Enter" button on the Homehub
login, and receive the flag for the challenge.

Note that these changes are only made to your local version of the
webpage. On top of that, they're only made to that particular 'instance'
 of your local version of the webpage - that is, if you refresh the
page, your changes are lost.

This challenge shows us that if we implement security checks in our
local browser, we can manipulate that and so could an attacker; and so
simple client-side checks like this could be bypassed. If this is the
first time you've played with the browser Developer Tools, it's well
worth getting familiar with them! They're extremely useful when it comes
 to poking and prodding at web applications as you'll be doing more of
in challenges to come. You can open the developer tools in most browsers
 by pressing `F12` on your keyboard, or by right-clicking on the page and selecting "Inspect Element".

## Real-world Uses

There's a really important message here, and it's perhaps not too
obvious what that is; quite simply - "don't trust users"! In this
challenge we have security only on the client-side (that is, your
browser, the "client" side) and that's not good! Everything that's shown
 to the user can be altered by them in their browser as much as they
like and if that's your only means of security, it can spell big
trouble.

It's important to have both client-side security (to stop users
meddling with the interface), plus also server-side security too, in
order to stop them actually actioning something you don't to happen also
 on your server. Quite simply think - client-side security for *robust interfaces* and server-side security to provide the *real security*. This challenge shows as a demo what happens if you only have client-side security ...it's simply not enough!

[← Previous: 8.01.03 - Social Engineering](https://play.cyberstart.com/field-manual/11bd01ce-0e88-11ec-82a8-0242ac130003)
[Next: 8.02.01 - The Rocketeer →](https://play.cyberstart.com/field-manual/67608bf0-0e88-11ec-82a8-0242ac130003)
