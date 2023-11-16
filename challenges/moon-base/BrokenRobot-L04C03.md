# 🤖 Broken Robot - L04 C03

We have a problem. Yesterday we sent out our remote tracking robot to collect some samples, but it's got a little lost. We need it back so we can send it back out to the alien landing site if they decide to land on the moon. Can you get it back to base?

Some instructions to help you:

Import our robot module which communicates to our server and moves the robot.
The available functions are robot.right(), robot.left(), robot.up() and robot.down().
The robot can travel within a 10x10 grid of x,y positions with values 0-9. Start is S and at 0,8, finish is F and at 7,5.
The goal is to get the robot to the finishing co-ordinates without crashing or going out of bounds.
The server will respond with messages letting you know how the robot is doing after each function call.
There are also blocked coords blockedCoords (x) = [[6,5], [6,6], [6,7], [7,7], [8,7], [9,7]].
Good luck agent!

Tip: Navigate the robot back to base to get the flag.

```
💡 Hint: First you need to import the module with 'import robot'.

   Next you need to call the movement functions within the robot library.

   We did this with other libraries before. Remember the 're' library from regular expressions?

   The format is: libraryname.functionname()


```

## Answer

```python
import robot

for i in range(4):
	robot.down()
for i in range(7):
	robot.right()
robot.up()
```
