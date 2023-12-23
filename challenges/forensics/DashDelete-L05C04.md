# 🗑 Dash Delete - L05 C04

So here's what we know so far – someone gained access to the company's servers, set up accounts and left suspicious files. We also think they may have deleted at least one important file called ‘coms.txt’, but fortunately not in a forensically sound way. Can you find anything important in this file?

**Tip:** Find what they deleted to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The file you are looking for exists in allocated space. Look at how Recycle bin forensics are carried out.

</details>

## Files

- [company_server_data.zip.001](https://drive.google.com/file/d/1fJsdix4TaU_wmDgtSbA6nr3rj0ZDwhs7/view?usp=sharing)
- [company_server_data.zip.002](https://drive.google.com/file/d/19PslT6C2-FjEBSRl1VRoBJ0yDC9T0SBz/view?usp=sharing)
- [company_server_data.zip.003](https://drive.google.com/file/d/1Mwzv804mNaHYUJD7ggN455LTxythZc7Y/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the file and extract the contents
- Put it through Autopsy and it should detect items that were deleted/in the recycle bin
- Of these, one of them has a path with "Coms.txt" and within the text of that file is a lot of random strings
- Observing very closely, there is the flag in plain text

![autopsy view](/assets/dashdelete1.png)

`flag: r3cycl3b1nf0r3n$1c$`

</details>
