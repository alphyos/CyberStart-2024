# 🏃‍♀️ Moving Mix-Up - L02 C05

Well, this is embarrassing. It seems the team over in Paris captured the **running memory** from a machine used by the photographer, but the documentation got all mixed up in transit. Can you see if you can at least confirm the **Operating System Profile** needed to analyse this image?

**Tip:** The flag is the correct profile.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Try `volatility -f <filename>`, but with which plugin?
```

</details>

## Files

- [suspect-memdump.zip](https://drive.google.com/file/d/1cU7OVhGgdwv8-JvGU3ekMFi6A9Fi7WIy/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the suspect-memdump.zip
- Extract the contents and navigate there in a terminal
- Use the imageinfo plugin with volatility `volatility -f memdump.mem imageinfo` (it may take a while to finish)
- The correct profile is the second one of the Suggested Profile(s)

![running volatility](/assets/movingmixup1.jpg)

`flag: Win81U1x64`

</details>
