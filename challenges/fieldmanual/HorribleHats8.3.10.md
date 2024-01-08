## WALKTHROUGHS

# Horrible Hats

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, the gang's bike store website has a tool people can use
 to create a custom cycle hat. Members of the gang have been sending
each other links to hat colour combinations they had created, suggesting
 they might be using the tool to hide secret messages. We're given an
example of one of these pages, which we're told contains a **secret code word** that we're looking to find.

Specifically, we need to convert the colour **RBG numbers** into letters, using the **ASCII table** provided, to get the flag.

## Solution

Typically, RGB numbers are a way of representing a particular colour, with values from 0-255 for the **r**ed, **g**reen and **b**lue
 values. However, given that they're really just number values and
numbers could translate to letters, they could also be used to hide
data, for example [ASCII](https://play.cyberstart.com/field-manual/8faa18d4-d7eb-11eb-aa93-0242ac140009) character reference codes.

In the challenge we're given an ASCII table, showing us a range of
characters and their corresponding decimal, binary, octal and hex. Of
importance to us are the letters starting at decimal number 65 - the
letter A.

As the briefing notes, we can convert each of the individual R, G and
 B colour numbers (decimal), for the various colours, into the
associated ASCII character. Doing so reveals the hidden message:

```txt
THE
SEC
RET
HAT
COD
EIS
BOT
TLE
```

We can combine the pieces to form a sentence that makes sense: The
secret hat code is bottle. The briefing states we're looking for a
secret code word, and given the hidden message we can assume this is
"bottle". We can submit this as the flag to complete the challenge.

## Real-world Uses

It can be quite common to encode or encrypt a message that can be
turned back into the original plain text message. However, poor choices
by cyber criminals or knowledge from cyber security experts can mean
it's reversed back into plain text easily. A well experienced cyber
forensics expert would instantly be suspicious of numbers in the range
65-90, as those represent characters A-Z in the ASCII character set.

It might be enough to raise a suspicion, resulting in running the
numbers through an ASCII decoder. However, while cyber criminals have
great tools, so do the cyber-security experts: likely using a tool which
 attempts to decode information under lots of different schemes
automatically. Getting suspicious about parts of evidence which prove
the most useful improves with experience and coupled with great tooling
that ultimately unmasks evidence can bring far less experienced
criminals to justice!

[← Previous: 8.03.09 - Bike Fan](https://play.cyberstart.com/field-manual/bfb59632-0e89-11ec-82a8-0242ac130003)
[Next: 8.03.11 - Tower of Wheels →](https://play.cyberstart.com/field-manual/efeee330-0e89-11ec-82a8-0242ac130003)
