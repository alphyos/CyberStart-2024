# ✏ Perilous Pencils - L10 C11

Agent 707, we've just had an interesting piece of intel. It seems the gang know we're monitoring their own sites and servers, and have therefore started removing anything incriminating. But they still intend to implement their plans to steal the EMP and so need a new way of sharing information.

You may have already come across the pencil selling e-commerce site Kapa that the gang hacked into and have been using to exchange messages. The Spetzners, being geeky science types, do love their pencils, but we think it's a little more sinister than that - it seems they might have hacked the site and started adjusting the images on it to contain hidden messages! If we hadn't noticed them using the site, we would never have known. Clever.

Have a look at this page in particular which the gang member was looking at. Anything strange about it?

**Tip:** The flag is in one of the images! Oh, and for password protected files don't attempt to drag and drop them.

```txt
💡 Hint: Consider looking at the images in a hex editor or with a binary extracting tool.
```

## Files

- [challenge-pencilz-gioconda-01.de7c4fac.jpg](/asstets/perilouspencils1.jpg)
- [challenge-pencilz-gioconda-02.e76dd0ff.jpg](/asstets/perilouspencils2.jpg)
- [challenge-pencilz-gioconda-03.d3dcf782.jpg](/asstets/perilouspencils3.jpg)

## Step by Step

- Download the image files, this guide will be referring to each as image 1, 2, and 3 in descending order matching the one on the challenge page
- Use binwalk to extract zip data from image 1
- Running `strings image` on images 2 and 3 will reveal the password segments towards the top of strings
  - Combined password is `Vidanya_Das`
  - Extract the zip data to reveal an executable file
    - Run `sudo chmod +x executable`
    - Run `./executable`
    - When prompted for the password, type `Vidanya_Das`
- After some time, the flag should appear

`flag: f1bVHxhlqR1pSkfAeao`
