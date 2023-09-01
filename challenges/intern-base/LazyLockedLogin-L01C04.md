# 🦥 Lazy Locked Login - L01 C04

Our Dutch office recently bought a new Internet of Things (IoT) connected fridge. However, the temperature settings have been widely fluctuating as of late. All agents are currently out in the field and too busy to fix the problem.

We know there is a remotely accessible technician's page where fridge **settings can be modified**, and that the fridge's login page **isn't very secure**. It was easy enough to find the username and password, but the form still has some **very lazy extra protection**. Intern, can you see if the rumours are true, fix our fridge, and help us verify this reported security vulnerability?

**Tip:** Successfully login to get the flag.

```
💡 Hint: Inspect the elements on page to get an understanding of how they're disabling the form. Can we make any changes to 
the code that will allow us to make it work as intended, so we can submit our login information?
```

## Step by Step

- Right click the enter button on the fridge and click inspect.

![right click on "enter" button pops up the inspect menu, inspect button is at the very bottom](/assets/lazylockedlogin1.png)

- The source code will pop up, double click on `div class actions` and double click on the word “**disabled**” to change to “**enabled**”.

![image of code](/assets/lazylockedlogin2.png)

- The enter button should become clickable and the flag will appear.
