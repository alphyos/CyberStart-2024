### WALKTHROUGHS
# Hello World

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/6e77929f-f281-447c-a9eb-d19050d17c78" width="800" />
</div>

# Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we're told that a hacker has hidden a secret way to contact him on his profile page. Specifically, we're looking for his email address, and this is the flag we need to solve the challenge.

The briefing notes that the information visible on the page is useless to us. This could be important - is there any information that isn't immediately visible?

# Solution

First and foremost, remember that with webpages there's information behind what we see in the browser; code that we can inspect. In this instance, however, it may be something hidden amongst the elements on the page that we're looking for - as the briefing notes, the information **visible on the page** is useless to us.

If we try selecting the content on the page (or pressing CTRL + A to select all) we can see there's some text under the "Send me an email" button, cleverly disguised with the same colour as the page background; white text on a white background.

As the briefing notes: the email address is the flag. We can copy the hidden email address and paste it into the flag submission box at the top-left of the page, and press "Enter" to submit.

# Real-World Uses

It may seem a little silly to hide information by having the same colour text as the background, but this is a common and heavily used technique even today. A good portion of spam emails evade spam filters this way, and it's even been used to trick search engine bots into giving sites higher rankings in search results, in what's known as "Google bombing", which pushes spam and malicious sites to be more visible than more legitimate sites.

The key point to note here is that what you see isn't all a computer will see - there's usually a lot of extra information for computers to work with, and it's that hidden data that can lead to all kinds of unseen bypasses and trickery!

### <div dir="rtl">[→ Next: 8.1.2 Mixed Up Messages](MixedUpMessages8.1.2.md)
