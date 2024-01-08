## WALKTHROUGHS

# Mixed Up Messages

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we're told a group of hackers is communicating via a
social media site, using cryptic messages. One in particular, we
believe, contains an important secret and we need to find out what it
is. This secret is also the flag we need to solve the challenge.

## Solution

Interestingly, this is actually a tactic that cyber criminals use in
real life! They'll use real websites and hide information in encrypted
form in plain site. In this instance, of course, we're hoping they're
using a relatively simple transformation.

So, let's take a look at the text. We can see it's using English
characters and punctuation - there's no unusual characters outside of
the alphabet or what you'd find on a standard keyboard. This suggests
the code should hopefully be simpler to crack!

On further inspection we can see a few key words that stand out as
simple backwards text. For example, the final word in the message:
"ehT", is "The" backwards. It also ends with a capital T, suggesting
that might be the start of the original message.

If we reverse the message (either manually or using an online tool) we can see the original:

*The time to launch our attack is now! Gather all resources and
prepare. Commence plans when I post code word "time4hackattack". Good
luck!*

The briefing tells us the flag we're looking for is an important
secret from the message. Presumably, this would be the code word - **time4hackattack**.

Submitting this as the flag will then complete the challenge.

## Real-world Uses

Until recently when machine learning and artificial intelligence got a
 whole lot smarter, computers have generally found understanding our
natural language hard. Think about it - swap a few letters around,
especially near the start of a word and a computer just doesn't
understand what the word could be. Over the decades, programmers have
written ever more sophisticated techniques to help software to
"unjumble" letters, but it still can be hard for computers to
understand.

While reversed characters is a well covered way for even *moderately* smart software to understand, it can still bypass basic software. Even with anti-virus programs today, they spot viruses via *pattern-matching*
 in strings, but a single character change can mean the "signature" of
the virus isn't found and so the virus let through. Mixing up characters
 is still a crucial technique heavily used with great success even today
 and to some extent, reversed character order is too.

<div align="center">

[← Previous: 8.01.01 - Hello World](HelloWorld8.1.1.md) | [Next: 8.01.03 - Social Engineering →](SocialEngineering8.1.3.md)
:-|-:
