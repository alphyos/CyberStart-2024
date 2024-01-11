## WALKTHROUGHS

# Tower of Wheels

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/93520964-b487-4e7a-96c1-a989df77fd4e"width="800" />
</div>

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we're given a **Tower of Hanoi** style puzzle to solve. We can move individual pieces of the puzzle by running the JavaScript function `move(<source>, <destination>)` where both `<source>` and `<destination>` can be "left", "mid" or "right". For example, if we want to move the top piece on the left, to the right, we would run `move("left", "right")`.

Once we've solved the puzzle we'll receive the flag we need to complete the challenge.

## Solution

If you've not encountered a **Tower of Hanoi** style
puzzle before, the goal here is to move the pieces of the puzzle from
the left 'pole' to the right, ending with the pieces stacked according
to height as they started. The catch is that you can *only* place a smaller piece on top of a larger one, not the other way around.

In order to solve the challenge, we have to run commands to move the
pieces, however first we need to open a console to run these commands.
This challenge has a built-in console we can use by clicking the
bouncing blue icon next to the URL bar. Or, if preferred, we can just
use the browser's Developer Tools console, easily accessible by
right-clicking the page and selecting "Inspect", followed by selecting
the "Console" tab.

Inside the console we can run our commands. For example, running `move("left", "right")` will move the current top piece on the left to the right. Then, running `move("left", "mid")` will move the new top piece on the left to the middle, and so on.

> If you'd like to try and solve the puzzle yourself at this point, give it a go! You can always start again by running the `reset()` command, and if you get stuck you can continue with the walkthrough below.

If you'd like to understand how to play the game itself, search
online for tactics. Below are the steps to take from a fresh start:

1. `move("left", "right")`
2. `move("left", "mid")`
3. `move("right", "mid")`
4. `move("left", "right")`
5. `move("mid", "left")`
6. `move("mid", "right")`
7. `move("left", "right")`

Now the pieces are stacked in ascending order on right side, a
success message will show at the top of the screen containing the flag
we need to complete the challenge.

Along with the above solution, there's actually a small easter egg on
 this challenge as well. If you inspect the HTML, or view the page
source, you can find a comment that mentions: *'You can complete this challenge quickly by running "cheat()" from the dev tools'*. So, instead of running all of the above commands, we could instead just run `cheat()` and it'll solve the puzzle for us!

This shows that by poking around and inspecting the underlying code,
sometimes we can find useful functions we can call directly that isn't
always intended by the developer.

## Real-world Uses

It can't be understated how important coding and the Console tab in
browsers can be to ethical hackers. Having the expertise to find, use
and write JavaScript, will be invaluable to you - so you can understand
the workings of a webpage, find data that's available and make use of
functions to trigger actions at will, are powerful tools in your
arsenal.

Websites with poor security, perhaps only "client-side" security
(that is, only security in the webpage seen in the browser, not server)
may be no match for a skilled hacker who makes use of its functions at
will, piece by piece. It's well worth spending time getting good at
JavaScript and the developer tools - with so much online today, it'll
open up a world of endless possibilities.

<div align="center">

[← Previous: 8.03.10 - Horrible Hats](HorribleHats8.3.10.md) | [Next: 8.03.12 - Binary Bike Lock →](BinaryBikeLock8.3.12.md)
:-|-:
