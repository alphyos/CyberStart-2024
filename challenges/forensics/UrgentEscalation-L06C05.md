# 🤯 Urgent Escalation L06 C05

Ok, urgent work for you, Agent 707 - this case just got escalated up through the ranks. As you've been looking into it again I decided to get a couple of other agents to take a look as well and they've noticed something of serious concern - we believe one of the servers in our Brazilian office which we were using to conduct the initial investigation has been compromised by exploiting a potential vulnerability. Can you identify it from the log files?

**Tip:** Find the vulnerability to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Did you know that Windows has a feature that stores specific data about the applications you run to help them start faster?

</details>

## Files

- [access.log](/assets/urgentescalation1.log)

<details><summary>

## Step by Step</summary>

- Download the log file and examine it using something like WordPad or a text editor.
- When roughly scanning, you will see a discrepancy with a result because it extends to the second line in an odd manner

![weird lines](/assets/urgentescalation2.png)

- You will see two instances of Base64 with the string of `U2gzbGxfU2gwY2tlZF9ieV9TMW1wbDFjMXR5IQo=`
- Putting this through a [Base64 decoder](https://www.dcode.fr/base-64-encoding), it will produce the flag

`flag: Sh3ll_Sh0cked_by_S1mpl1c1ty!`

</details>
