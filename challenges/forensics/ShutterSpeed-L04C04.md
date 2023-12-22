# ⛈ Shutter Speed - L04 C04

We have a quick and urgent job for you, Agent 707. One of our team in the field has managed to acquire the suspect's camera and download the images he had on it. They look innocent enough, just photo's of the tour, but we've received word that they've already been taken off the camera, a secret inserted into them, and put back, ready to be passed on to another gang member at the end of the tour. Can you take a look at this particular file and see what you can find.

**Tip:** The flag is in the image.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Did you know steghide has an extract feature?
```

</details>

## Files

- [masai-mara-01.jpg](/assets/shutterspeed1.jpg)

<details><summary>

## Step by Step</summary>

- Download the image
- Use `steghide --extract -sf filename`
- When asked for a password simply hit enter
- There should be a .rar archive in your directory now
- Extract the content, the flag is in the .txt file

`flag: hjkslPi8tyh!`

</details>
