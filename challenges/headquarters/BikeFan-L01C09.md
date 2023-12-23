# 🚲 Bike Fan - L01 C09

Quick task for you Agent 707, one of the gang, Lars De Vries, has written a post where he lists pictures of bikes he likes. Recently we've noticed some of the images are broken and he hasn't fixed it. Seems odd. **Take a look** at this page and see if you can **get the image to show**, perhaps take a look at the **source code of the page** and see if anything **doesn't look right**.

**Tip:** Find a way to **get the image to show** and you'll find the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The broken image seems to be missing a file extension. Try adding some common image file extensions and see if you can get it to show. Your browser has "Dev Tools" and an "Element Inspector", within it, that can help with this.

</details>

<details><summary>

## Step by Step</summary>

- Right click on the photo link that is not properly showing on the website and use **inspect element**.

![image of what the link looks like in element inspector](/assets/bikefan1.png)

- Add `.jpg` to the end of the link.
- The flag should appear in the newly uploaded image.

</details>
