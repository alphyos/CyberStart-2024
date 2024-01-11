# 🏇 Rover Rodeo - L02 C04

The agency has traced a strange signal from space that leads back to a nearby planet. In anticipation, we have sent a remote-controlled rover to its surface to uncover what might be sending the signal. Your mission is to navigate the rover to the location marked with a green flag and complete any side missions on the way.

But there's a problem. The software used to control the rover wasn't completed in time for this mission. This means you're going to need to input any instructions to the rover manually via your browser's console. Don't worry, one of our agents will guide you on how to get access.

Good luck!

Tip: Move the rover to the green flag, using the browser's developer console, to receive the flag.

<details><summary>

## Need a hint</summary>

> 💡 Hint: Check out the instructions in the email, or the field manual, to open the Console in the developer tools.
>
> Once the Console is open, you can solve the challenge using `rover.move()`, `rover.turn('left')`, `rover.turn('right')` and `rover.drill()`. Don't forget you can run `rover.help()` for a more detailed description of these functions.

</details>

<details><summary>

## Step by Step</summary>

- Right click somewhere on the page and select the "Inspect" option - this will open the developer tools
  - If you're on a Windows computer, click the three dots ( ⋮ , typically in the top-right corner) and then "More tools", then "Developer tools"
  - If you're on a Windows computer, press F12
  - If you're on a Mac computer, select "View" from the browser's main drop-down menus, then go to "Developer" and finally click "Developer Tools"
- You want to move the rover from the bottom left to the top right of the grid while avoiding the stone obstacles
- Execute the following commands on the Console, line by line

```js
rover.move(2)
rover.turn("right")
rover.move(2)
rover.turn("left")
rover.move(1)
rover.turn("right")
rover.move(2)
rover.turn("right")
rover.move(1)
rover.turn("left")
rover.move(1)
```

- At this position, your rover should be stopped over a highlighted yellow box and there is a console message that appears:
  - "A mineral deposit has been detected at your location. Drill down to collect a sample."
- Execute the following commands on the Console, line by line

```js
rover.drill()
rover.move(2)
rover.turn("left")
rover.move(2)
```

- Once your rover is on the flag space, the flag should appear

</details>
