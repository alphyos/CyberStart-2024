## WALKTHROUGHS

# Bike Fan

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we're looking at a blog post written by a gang member,
containing pictures of bicycles he likes. One of the images, however,
isn't loading and hasn't been fixed. We need to take a **look at the source code**
 of the page and see if we can spot anything that doesn't look right.
Specifically, we need to find a way to get the image to show, and we'll
be given the flag we need to complete the challenge.

## Solution

As the briefing notes, we want to take a look at the source code of
the webpage to help us solve this challenge. The source code is the raw
data behind the scenes, containing the content for the page and telling
the browser how to display it. In particular, we want to have a look at
the **HTML** of the page.

There's a couple of ways we can do this: we could view the page
source directly - most browsers allow you to do this by right-clicking
the page and clicking something similar to "View page source".
Alternatively, we could use the browser's Developer Tools - a handy
toolbox for deeper inspection of the nuts and bolts of the webpage. This
 can easily be accessed by right-clicking on the page and selecting
"Inspect" or "Inspect Element".

While browsing through the HTML for the page, we can spot a lot of elements with the `class` of "bike". Inside each is an image; presumably these are the pictures of the bikes in the blog post.

One of them has a `src` (the web address, or the **source**) for the image that ends abruptly with `1438.`, so looks slightly different to the others as it's missing the `jpg` file extension. If we're just viewing the page source, we can click this `src`
 URL to try and go directly to it, or if we're inspecting the element we
 can double-click it to modify the URL within the webpage itself.

Either way, we can add the missing file extension - `jpg` -
 and successfully load the previously broken image. In the corner is the
 flag we need, which we can submit to solve the challenge.

## Real-world Uses

While in this case we were just requesting an image that was not
loading for us, there's an important aspect to learn here; often files
are named sequentially, or there's a pattern you can identify. Are there
 files from the past, or future you can predict the references for, and
so you can perhaps guess the names of them according to the "pattern"
used?

Guessing these undisclosed URLs for unreleased content can be hugely
lucrative. Imagine an unreleased computer game, movie or music album
which is being prepared for a big launch, but obvious naming and lack of
 security means hackers can find it early. It's the sort of thing that
can be sold on black markets, a lot of money lost by companies and a lot
 of money gained by the bad guys!

<div align="center">

[← Previous: 8.03.08 - Hidden Report](HiddenReport8.3.8.md) | [Next: 8.03.10 - Horrible Hats →](HorribleHats8.3.10.md)
:-|-:
