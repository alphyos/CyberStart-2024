# 🥶 Chilly Command - L07 C04

We know the hackers gained access to a particular Windows box, but we're not sure exactly what they did. See if you can use the registry file to figure out what the last command was that they ran.

**Tip:** Get the command to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Have you thought about MRU lists?

</details>

## Files

- [HKEY_CURRENT_USER.reg.xml](/assets/chillycommand1.xml)

<details><summary>

## Step by Step</summary>

- Download the file an examine it, here I used Visual Studio Code
- Search for the keyword "RunMRU" and a single entry should be found
- Beside `encodedcommand`, there should be a string decodable by Base64

![vsc view](/assets/chillycommand2.png)

- Decoding in Base64 should give letters separated by "�" characters which form a cohesive flag
- Remove these symbols to get the flag

`flag: Th3_B3sT_Fl4gs_R_F0r3n51c`

</details>
