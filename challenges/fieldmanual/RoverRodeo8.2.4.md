## WALKTHROUGHS

# Rover Rodeo

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, the agency has traced a signal from space and have sent
 a rover to find the source. However, the software wasn't completed in
time and so we need to manually direct the rover to its destination.

Additionally, we are introduced to the browser developer tools in order to interact with the rover.

## Solution

If we look at the **Email** tab we're given some additional context as well as instructions to open the browser's developer tools; specifically the **Console**. We need to use the console to complete this challenge, so let's open it!

> For more information check out the [Console](https://play.cyberstart.com/field-manual/8fe93ace-a868-11ed-afa1-0242ac120002) page!

Note that the email also tells us how to get started interacting with the rover - the command `rover.help()`. With the Console open, we can run this command and are provided with an overview of the available commands: `rover.move(<spaces>)`, `rover.turn(<direction>, <times>)` and `rover.drill()`.

`rover.move()` can be run without the optional `spaces` argument - this just allows us to move more than one space at a time instead of having to call `rover.move()` multiple times in a row.

`rover.turn()` requires at least one parameter - either `"left"` or `"right"` to specify which direction to turn, e.g. `rover.turn("left")`. We can also add an optional parameter - `times` - to turn the rover multiple times.

Using these two methods we can navigate the rover towards the green flag. For example, you may need to run the commands:

```js
rover.turn("right")
rover.move(2)
rover.turn("left")
rover.move(3)
rover.turn("right")
rover.move()
...
```

And so on.

At some point on the rover's journey you'll encounter a side mission.
 The grid square will have a yellow border, and we'll see a message
output in the Console. In order to continue, we can call the `rover.drill()` method, which will drill for a sample and complete the side mission.

Once completed, continue navigating as before until the rover reaches
 the finishing flag. At this point, you'll see the success banner and
the text flag you need to complete the challenge.

## Real-world Uses

Here you're introduced to some early programming concepts: functions,
 how to call them, as well as one or more function arguments. These are
the core building blocks of larger and more complicated programming
projects, and better understanding these tools will be a great addition
to your coding journey!

[← Previous: 8.02.03 - Galactic Greetings](https://play.cyberstart.com/field-manual/abda13c8-0e88-11ec-82a8-0242ac130003)
[Next: 8.03.01 - Social Secret →](https://play.cyberstart.com/field-manual/cebaf72c-0e88-11ec-82a8-0242ac130003)
