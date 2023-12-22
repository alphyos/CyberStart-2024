# 🛌 Hasty Action - L04 C03

Ok Agent 707, slight change of plan with our investigation! Our team in Africa decided to swoop in and arrest one of the hackers when they saw him doing something they thought was especially suspicious whilst in a cafe in Nairobi. The only problem is he closed the file on his laptop before he was arrested. Can you help the team there figure out what file it was? They've sent the image file for you to take a look at.

**Tip:** Find the recent files and find the flag.

**Note:** The files for this challenge are the same as Level 4 Challenge 1 and only need downloading once.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Look at the recent documents folder on the user profile. Are there any suspicious looking files?
```

</details>

## Files

- [hacked_laptop.zip.001](https://drive.google.com/file/d/1vmb1lQL77sZQSA4_-2Ie0uy_BNL5M5K4/view?usp=sharing)
- [hacked_laptop.zip.002](https://drive.google.com/file/d/1v1YTYumY-ZXuQHmdXw_yZXpgQH24HqKu/view?usp=sharing)
- [hacked_laptop.zip.003](https://drive.google.com/file/d/1O8b1pQCej2w77hZGvMdP_Cf16GK3OcBV/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the files
- Run `cat hacked_laptop.z* > laptop.zip` to combine the parts of the image
- Extract and open it in autopsy
- Use the keyword function to look for `secret`
- Additionally, there is a folder for recent documents and recently accessed files where a file called `secret_flag` is mentioned
- View the contents of that file

![content of secret_flag.rtf](/assets/hastyaction1.png)

`flag: secrets_lie_here`

</details>
