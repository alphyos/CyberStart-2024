# 💰 Big Transfer - L03 C11

Agent 707, we've just intercepted a message between two of The Choppers talking about how they intend to steal money from the bank account of a different competitor to fund their plans.

It said they've found a weakness in the money transfer tool on the Global Bank website. **We've just successfully put through a test transfer**, can you prove it's vulnerable by transferring **1000** to a bank account called **cpatestreceiver** from **cpatestsender**.

**Tip:** Sometimes URLs can be manipulated to bypass security.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Did you notice the URL on the successful transfer page? I wonder what would happen if you changed the parameters and submitted it again?

</details>

<details><summary>

## Step by Step</summary>

- Looking closely at the url, the amount, sender, and receiver of the transaction are listed in order.
- By manipulating the url by typing `https://www.bankwithglobal.com/transfer?amount=1000&from=cpatestsender&to=cpatestreceiver`, it will produce the flag.

</details>
