# 🗿 Missing Image L06 C02

Here's another file we intercepted a while back. We know it contains a secret, and we're pretty sure it's an image file. But for some reason, it doesn't seem to be detected as one. She has probably made a change to it in some way and our analysts were never able to figure out what.

**Tip:** Make the image work to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Take a look at how file headers work.

</details>

## Files

- [easter-island-02.jpg](/assets/missingimage1.jpg)

<details><summary>

## Step by Step</summary>

- Download the file and examine using a [hex editor](https://hexed.it/)
- Change the first three hex bytes to `FF D8 FF` because the file does not have the correct header values
- After doing this, it should become an openable jpg file with the flag hidden at the top of the image

`flag: H3ad3r$_4_W1nn3r$`

</details>
