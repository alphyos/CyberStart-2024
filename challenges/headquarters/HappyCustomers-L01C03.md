# 🎡 Happy Customers - L01 C03

During our initial analysis of the gang we noticed something strange - they created lists of their customers and shared it between their bike shops, and each customer had a unique pattern of numbers after their name. One of our agents thinks the pattern of numbers might be **encoded words**. We also noticed the **numbers never went above 26**, that might be relevant. Can you work out what it means?

**Tip:** **Decode the message** to get the secret word and use that as the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Could the numbers represent letters somehow? Think about the position of letters in the alphabet.

</details>

<details><summary>

## Step by Step</summary>

- Set the letters of the alphabet to numbers with “A” as “1” and “Z” as “26”

- **Jan De Jong (20, 8, 5) - The**
- **Lars Jansen (19, 5, 3, 18, 5, 20) - Secret**
- **Gerrit Vries (23, 15, 18, 4) - Word**
- **Merel De Vries (9, 19) - Is**
- **Sanne Bakker (23, 8, 5, 5, 12) - `Wheel`**

- Enter the last word as the flag

`flag: Wheel`

</details>
