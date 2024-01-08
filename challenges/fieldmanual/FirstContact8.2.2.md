## WALKTHROUGHS

# First Contact

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, the satellite software used to listen to specific
objects in space is broken and in the short term we'd like to find a way
 around this. It may be possible to find somewhere to specify object
coordinates instead, so we can still listen for signals at that object
whilst the mouse click interaction isn't fully working.

## Solution

Let's start by hovering the mouse pointer over some objects in the scene. Doing this reveals `x` and `y`
 coordinates for the specific object, and by clicking the object we find
 the red box at the top shows the same information. However, it also
informs us that the auto-focus feature isn't working, so we can assume *this* is the part of the software that is unable to target objects.

Looking just above the red box, in the web address for the page, we can see `x` and `y` querystring *keys*, both with `000` *values*.
 Given that the coordinates for the objects are also 3 digits, we can
deduce that the 3 digit values need to be placed where these placeholder
 values are in the web address.

Doing this for the selected object and hitting the Enter key will try
 that unique web address, we see a short animation for the object, which
 results in informing us the signal from that object is weak and, due to
 the target box turning red also, we can understand it wasn't the
correct object.

The same process of selecting an object and updating the two
querystring values can be repeated for other objects. After a few
attempts, we find one of the objects has a strong signal, the target box
 turns green, and we're given the flag!

Software breakages happen and in this case we're able to get around
that by manipulating the web address ourselves. However, beyond
breakages, this challenge illustrates how web addresses for dynamic page
 content can be observed, understood and possibly variations attempted.
With a little scripting, many variations can be attempted automatically
and so it's crucial from a website owners point of view to adequately
protect against unauthorised use. Hackers certainly won't stick to just
clicking links you provide!

## Real-world Uses

Websites have come a long way over the years. From simple static
pages, to full-blown dynamic web apps that we enjoy using today. A
dynamic site can often use a website template, and decides the
appropriate content to load on page according to the web address; such
as information in the path or querystring parameters, as this challenge
does. The trouble is, if the data items are easy to guess and there's no
 security to protect that content, and even server adequately, it can
lead hackers to access things they shouldn't.

While amending the `x` and `y` querystring
values in this challenge didn't feature much security (this was an
internal tool for Agents in the HQ to use), what if this was a public
facing app and perhaps the querystring values were for user accounts? It
 may seem like something that shouldn't happen, but all too frequently
does. What happens if you change a reference in the querystring to
another, perhaps up or down a digit, or `0`, `-1`, `NULL`, `[]`
 or other values? If the developer of the site doesn't handle cases like
 and others these well, it can lead to lots of unexpected consequences!

<div align="center">

[← Previous: 8.02.01 - The Rocketeer](TheRocketeer8.2.1.md) | [Next: 8.02.03 - Galactic Greetings →](GalacticGreetings8.2.3.md)
:-|-:
