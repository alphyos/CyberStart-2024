# 🐻 Tayga Bears - L09 C11

One of the Spetzners lives in Tayga, a heavily forested area with a lot of bears! So it's no surprise that he spends some of his spare time taking photographs of them and posting them to a nature site called медведь следить (which is Russian for "Bear Watch"). We thought it was fairly innocent until one of the agents spotted something weird about one of the images.

Take a look at them and see if you can spot what it is.

**Tip:** There's a hidden file, open it to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Take a close look at each of the images using "binwalk" or a hex editor.
   Do you see anything unusual about them?
```

</details>

## Files

- [challenge-bearwatch-pic-06.08648647](/assets/taygabears1.jpg)

<details><summary>

## Step by Step</summary>

- Download the files and run `binwalk *` in the directory where the files are located
  - Notice image 6 has a zip folder in it
  - Run `binwalk --dd='.*' imagename.jpg`
- Go to the newly created directory where binwalk extracted all the files
  - One of these is a zipfile
  - Run `unzip filename`
  - Give permissions to the newly extracted file using `sudo chmod +x extracted_executable`
- Run `./extracted_executable`
- The flag should appear after a while

`flag: B3znJluppFPJnNG7PAg`

</details>
