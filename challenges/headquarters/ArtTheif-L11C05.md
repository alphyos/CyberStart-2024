# 🖌 Art Theif - L11 C05

Agent 707, we've been doing some research on Barry Brigley, one of the Bulldogs and a notorious art thief. We've managed to get access to a site he uses to post images of the art he's stolen which are for sale on the black market, but he's hiding the images somehow so we don't know what he's stolen. If we knew it would help us track his movements over the past few months (we think the art comes from a variety of galleries all over Europe).

Take a look at the site and the images. You can download the images, they're in a common image format, see if you can recover them.

**Tip:** The flag is in one of the images.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Take a look at the images in a hex editor and you'll find the file header information is missing. See if you can recover it.

</details>

## Files

- [artwork.11f7c21f.zip](/assets/arttheif1.zip)

<details><summary>

## Step by Step</summary>

- Download the zip of corrupted images and extract it
- Open the third image `artwork-03.jpg` in a hex editor that supports inserting bytes
- Prepend the missing part of the jfif file signature `FF D8 FF E0`
- Alternatively use this command: `echo -n "FF D8 FF E0" | xxd -r -p | cat - artwork-03.jpg > new3.jpg
`
- Save the file and open the image, it contains the flag

`flag: MaGiC_NuMbErS`

</details>
