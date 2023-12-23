# 🎠 Trojan Horse - L02 C03

Whilst in the shop the photographer asked to use one of the staffs Windows PC's to show them previews of the photos. We think he may have done something bad whilst he was using it as now it appears to run an **application** we don't recognize on **boot up**.

**Tip:** Find the **malicious process** to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Have you heard of the 'Windows Registry'? It dictates what software Windows runs at startup for the local machine. Find out where these are stored to solve this challenge.

</details>

## Files

- [Registry.zip](/assets/trojanhorse2.zip)

<details><summary>

## Step by Step</summary>

- Download the zip file and extract it using the password provided in the readme.txt
- Open it up with Autopsy and you want to navigate to the start-up registry keys location
  - This can be found within **Microsoft/Windows/CurrentVersion**
- Looking through the various keys, one stands out as being suspicious
- In the folder "Run", the flag is set as one of the `key values`
  - The key is named `Malicious`

![autopsy view](/assets/trojanhorse1.png)

`flag: 1238HgulsjtuwGF`

</details>
