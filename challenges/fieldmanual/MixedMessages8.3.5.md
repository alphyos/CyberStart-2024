## WALKTHROUGHS

# Mixed Messages

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/e30694eb-11f3-4931-bd19-4cb29e05e819"width="800" />
</div>

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, while monitoring communications between two senior gang members their messages suddendly started coming through **mixed up**.
 Though it could be a technical issue, it may in fact be deliberately
encoded messages instead. We're given an example of one of the messages
to try and decode.

Once we have the decoded message, we're told it should mention two colours which we need to combine to create the flag.

## Solution

Given we have the example message we need to decode, we could just
start inspecting it to try and determine how it has been encoded and
hope for the best. However, in the briefing we have also been given some
 additional information on the contents of the message, known as a *crib* - knowing some or all of the original **plaintext** version of an encoded (or encrypted) message can make decoding (or decrypting) the **ciphertext** a lot easier.

So, as we know the original message contains two colours, we can
focus our attention on the encoded message with that in mind.
Specifically, the last few words of the message look like they could be
rearranged to spell some colours: `LBEU` and `EYLLWO`, which is `BLUE` and `YELLOW` if we swap pairs of letters.

The briefing notes we just need to combine the two colours to create the flag, so we can submit these combined colours (`blueyellow`) as the flag to complete the challenge.

## Real-world Uses

Until recently when machine learning and artificial intelligence got a
 whole lot smarter, computers have generally found understanding our
natural language hard. Think about it - swap a few letters around and a
computer just doesn't understand what the word could be. Over the
decades, programmers have written ever more sophisticated techniques to
help software to "unjumble" letters, but it still can be hard for
computers to understand.

So while switched pairs of characters is something smarter software
can spot, it can still bypass basic software. Even with anti-virus
programs today, they often identify viruses via *pattern-matching*
 in strings, but even a single character change can mean the "signature"
 of the virus isn't identified and so the virus let through. This can
mean mixing up characters is a very valid technique, used with great
success in bypassing scanning and filters.

<div align="center">

[← Previous: 8.03.04 - Race To Where](RaceToWhere8.3.4.md) | [Next: 8.03.06 - Executable →](Executable8.3.6.md)
:-|-:
