# 🦥 Lazy Locked Login - L01 C04

The agency recently purchased a homehub for the office to automate appliances like lights and thermostats. But recently, we've been receiving complaints about irregular temperature changes and lights unpredictably turning on and off.

We've found where you can access the homehub settings along with the sign in details, but it turns out you can only submit the form and sign in from a technicians laptop. We need you to figure out how we can bypass this restriction so we can adjust the settings and restore normality in the office!

**Tip:** Try to inspect the login form with the tools provided to see what is stopping you from submitting the form and signing in.

**Related Field Manual Entries:** [Lazy Locked Login](../fieldmanual/LazyLockedLogin.8.1.4.md)

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Using either the provided document inspector (opened by clicking the blue icon in the top-right of the challenge), or using your browser's built-in document inspector, inspect the elements on the page to get an understanding of why the login form won't submit.
> 
> Are there any changes that can be made to the code that will bypass any restrictions, allowing the login credentials to submit?

</details>

![image of the challenge](/assets/lazylockedlogin.png)

<details><summary>

## Step by Step</summary>

- Right click the top right blue button of the fake challenge web browser

- The source code will pop up in the "Inspector" and click on the word **disabled** to type the change to **enabled**

![image of the inspector](/assets/lazylockedloginnew1.png)

- The enter button should become clickable, it turns blue to indicate this, and the flag will appear

`flag is unique`
</details>

<details><summary>

## 2022 Old Challenge Archive</summary>

# Lazy Locked Login - L01 C04 (RETIRED)

Our Dutch office recently bought a new Internet of Things (IoT) connected fridge. However, the temperature settings have been widely fluctuating as of late. All agents are currently out in the field and too busy to fix the problem.

We know there is a remotely accessible technician's page where fridge **settings can be modified**, and that the fridge's login page **isn't very secure**. It was easy enough to find the username and password, but the form still has some **very lazy extra protection**. Intern, can you see if the rumours are true, fix our fridge, and help us verify this reported security vulnerability?

**Tip:** Successfully login to get the flag.

> 💡 Hint: Inspect the elements on page to get an understanding of how they're disabling the form. Can we make any changes to the code that will allow us to make it work as intended, so we can submit our login information?

## Step by Step

- Right click the enter button on the fridge and click inspect

![right click on "enter" button pops up the inspect menu, inspect button is at the very bottom](/assets/lazylockedlogin1.png)

- The source code will pop up, double click on `div class actions` and double click on the word **disabled** to change to **enabled**

![image of code](/assets/lazylockedlogin2.png)

- The enter button should become clickable and the flag will appear

</details>
