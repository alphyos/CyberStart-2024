# 🦕 Argentine Ambush - L06 C01

From a meeting she had in Argentina we were able to intercept an image file she sent to the person she met with shortly after they departed which we think has a secret within it. But it looks like she has used a tool that has the ability to use passphrases to hamper extracting hidden files. Some other tracking we put in place has also revealed she has been visiting websites about encoding messages. See if you can put these bits of information to good use.

**Tip:** Get into the file to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: You need to identify the passphrase and use it to extract the hidden file. Is the message in the file readable?

</details>

## Files

- [easter-island-01.jpg](/assets/argentineambush1.jpg)

<details><summary>

## Step by Step</summary>

- Download the file and examine using a [hex editor](https://hexed.it/)
- At the end of the file, there is a string, `ilovesteggivemetheflag`
- Taking this string and hashing it using MD5 will give you `c53fa35e5b2ed699ccc304088c3d9c8e`
- Using steghide and putting in the previous hashed string as the password will give you the flag.

`flag: w1n_4_st3g0`

</details>
