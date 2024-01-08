## WALKTHROUGHS

# Race To Where

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we're shown a website advertising an upcoming bike race
 organised by a gang. From an initial inspection, it looks like there
are just two images on the page: a logo and the poster. We're looking to
 find anything suspicious, perhaps some hidden text.

If we can find the hidden content, it will lead us to the flag we need to complete the challenge.

## Solution

As mentioned in the briefing, all we can initially see on the page is a logo and the poster for the bike race.

A quick and easy way to see if there's any additional content on the
page, not immediately visible to us, is simply to click and drag to
select all the content on the page (or press CTRL + A to select all). In
 doing so, we can see there's some text under the logo image, cleverly
disguised with the same colour as the page background; red text on a red
 background.

The hidden text tells us to go to `/secret.html`. This looks like another web page, so lets try going to this page in the challenge browser: `https://www.canalbikerace.com/secret.html`. When the page loads we're given the flag, which we can submit to complete the challenge.

## Real-world Uses

It may seem a little silly to hide information by having the same
colour text as the background, but this is a common and heavily used
technique even today. A good portion of spam emails evade spam filters
this way, and it's even been used to trick search engine bots into
giving sites higher rankings in search results, in what's known as
"Google bombing", which pushes spam and malicious sites to be above, and
 so more visible than more legitimate sites.

But the key point to note here is that - what *you* see isn't all a *computer*
 will see; there's usually a lot of extra information for computers to
work with, and it's that hidden data that can lead to all kinds of
unseen bypasses and trickery!

<div align="center">

[← Previous: 8.03.03 - Happy Customers](HappyCustomers8.3.3.md) | [Next: 8.03.05 - Mixed Messages →](MixedMessages8.3.5.md)
:-|-:
