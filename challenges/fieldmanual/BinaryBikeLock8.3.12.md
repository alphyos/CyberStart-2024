## WALKTHROUGHS

# Binary Bike Lock

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/c7aeb995-2c29-4109-8423-5e53ad343b53"width="800" />
</div>

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, the gang has created a custom bike lock which is
potentially going to be used as part of a bigger bike heist. We want to
try and figure out how it works ahead of time. Once we unlock the bike
lock we'll receive the flag that we need to complete the challenge.

## Solution

If we take a look at the lock we can see a few things of note:

* We have a couple of binary values with a `+` indicating we probably need to add them together.
* We have an input field where we presumably need to enter the answer.
* Finally, we have buttons for 0-9, plus a green `>` we
can click to submit the answer. Given binary contains just 0 and 1, this
 suggests we probably need to provide the answer in decimal rather than
binary.

Based on those assumptions, we first want to tackle the addition of
the two binary numbers. We could do this manually if we wanted, or we
could search online for a binary addition tool.

The binary values change on each page request, so these values likely won't match your own, but for example:

`00011100 + 00011111` converted to decimal values results in 28 + 31. Adding these together, we get **59**.

If we enter this final number into the input field, either by typing
or clicking the numbers on the lock, we can then submit it by pressing
the green button. Assuming we provide the correct answer, we'll see a
success message at the top of the screen, which contains the flag we
need to complete the challenge.

## Real-world Uses

Binary data is really what computers use to work, by reading these `0` and `1`
 digits at incredible speeds (many billions per second). They find them
vastly more efficient to work with for math and characters, but herein
lies a problem - computers like binary data, but humans like language.

If we were to perform even simple math operations like addition on
binary numbers, we'd be quite slow, perhaps only an equation or two a
minute. While it's a fun exercise to try, it's generally smarter to let
the computers do the hard work. Use tools where appropriate to carry out
 math, encode/decode etc - it'll be far quicker and also free of errors
you might make. Work smart, not hard!

<div align="center">

| [← Previous: 8.03.11 - Tower of Wheels](TowerOfWheels8.3.11.md) |
|-|
