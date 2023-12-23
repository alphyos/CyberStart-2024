# 🔨 String Cruncher - L13 C11

We've discovered a web page used by the gang which seems to just generate some strings, but we're not sure why. They all seem to be random but we have a feeling, given the technical sophistication of this gang, that things might not be as they seem. Take a look.

**Tip:** One of these is not like the others... when you find the odd one out, it will lead you to the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Use a [Base64 decoder](https://www.base64decode.org/), an [XOR Calculator](https://xor.pw/#), and [ASCII Code Converter](https://www.rapidtables.com/convert/number/hex-to-ascii.html).

</details>

<details><summary>

## Step by Step</summary>

- Copy the entire chunk of strings and recognize that they’re all individual Base64 strings ending in `==`
- Use a Base64 decoder to decode them and find the one string that is odd and produces hex-like numbers
- Copy the Base64 string of the hex numbers and put them through the original website
- You should have your original Base64 string and the new one, put these through a Base64 decoder again to get hex values
- Use a XOR calculator, XOR the two sets of numbers from each other to get a number
- Copy the numbers and put them through an ASCII converter to get the flag

`flag: 5YhxvcWuwifyVicpC4Jm`

</details>
