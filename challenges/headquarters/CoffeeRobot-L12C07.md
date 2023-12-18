# ☕ Coffee Robot - L12 C07

An inside agent has told us Charlie Hampton, one of the gang's smartest engineers, has been making detailed notes, instructions and schematic drawings of the robot and keeping them on one of his servers. Getting access to those drawings would really help us understand how this robot will operate.

The problem is, we don't know which server he's keeping the plans on. All we do know is that Charlie owns a legit business, a coffee shop in East London, which he uses as a cover for his gang activities. It's a long shot but we do know they run a small server in the basement of the shop which controls their on-demand coffee ordering service. Go to the coffee ordering site, see if it's vulnerable. If it is see if you can find anything useful on the server.

**Tip:** Find the drawings file to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: You might need to look for hidden files to find what you're looking for.
```

</details>

<details><summary>

## Step by Step</summary>

- In the text box at the bottom, type `$(ls -la)`
- Type `$(ls -la ..)`
- Type `$(ls -la ../robot-bank-job)`
- Type `$(cat ../robot-bank-job/.robot_sketches.txt)`

`flag: GnJRZZdHea3pSVmtwlNH`

</details>
