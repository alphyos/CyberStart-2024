# 🌃 A Secret Rendezvous - L03 C01

Yesterday we intercepted some code passed between two Chopper gang members - Ibert and Dante. We believe it mentions the **location of a secret meeting** to discuss plans to hack into their competitors' computers.

Fortunately, we know it uses the **Columnar Transposition Cipher** and have a CPA tool to help you crack it. We've loaded the code into the tool. Give it a try and see if you can decrypt the message.

**Tip:** The flag is the city they will be meeting in.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: This kind of encryption can be tough to crack, but luckily our tool makes it simple.
   Try dragging the columns around the page until the text makes sense. When you've got it,
   see if you can find a mention of the city where they're planning to meet - that's the flag!
```

</details>

<details><summary>

## Step by Step</summary>

- Move the columns so that the first row of letters spell "WEAR".
- If you actually read the sentence from left to right, top to bottom, you’ll see that they want to **meet in the city of** `[FLAG]`.

![photo of the correct column layout](/assets/asecretrendezvous1.png)

</details>
