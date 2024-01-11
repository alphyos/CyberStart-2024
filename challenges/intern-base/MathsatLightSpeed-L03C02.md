# 📐 Maths at Light Speed - L03 C02

Agent 707, I hope you know how to use a calculator? Of course you do. In theory you should be able to bypass this security gateway to a warehouse we believe holds clues to the whereabouts of a gang we are in hot pursuit of.

The thing is, the gateway was created by someone who loves doing everything **super fast**! You **only get 0.1 seconds** to answer the question asked by the gateway. Can you find a way around it? We're not able to **form**ulate an **action** quick enough.

**Tip:** Bypass the calculator lock to get the flag.

<details><summary>

## Need a hint</summary>

> 💡 Hint: Try watching the source code as you are spinning a new set of numbers. What changes when the spin is happening and then gets removed when the calculator gets locked?

</details>

<details><summary>

## Step by Step</summary>

![picture of calculator](/assets/mathsatlightspeed1.png)

- Click the “Spin for question” button. It should give you an addition or subtraction problem that is locked, go ahead and **solve for the answer**.
- Open inspect element over the box you type in. It should open up the details of the box which is “`<form class="form" action id="calc-form">`”.
- Change action to “`action="/flashfast/answer`".
![picture of source code](/assets/mathsatlightspeed2.png)
- Type in the answer and click submit, a `flag` should appear.

</details>
