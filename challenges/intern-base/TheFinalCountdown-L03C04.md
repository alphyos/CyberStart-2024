# ⌛ The Final Countdown - L03 C04

The main tourism website for Barcelona has been hacked. The hackers have devised a program that changes the content of the website based on a timer. You can imagine the confusion this has been causing the sites visitors! Can you figure out how we can get the secret code to stop this program from running?

It'll be tricky - they appear to use a **script** to **join multiple sets** of content together and finally **send the joined sets** to somewhere else to **validate**.

**Tip:** The characters at the 5 URLs change quickly, but computers can be far quicker than humans, especially when getting data!

<details><summary>

## Need a hint?</summary>

> 💡 Hint: With a little code you could probably get the contents from those 5 URLs as strings and join them together.
> With all the parts together, it'll just be a case of sending to the final URL. Pay attention to the formats shown!

</details>

![image of the challenge](/assets/thefinalcountdown.png)

<details><summary>

## Step by Step</summary>

- Open your command terminal, for Windows: Windows Key + R and type **cmd**
- Type `curl https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D`
  - This will take all of the links provided in the challenge and produce a concatenated version of the strings into one string, in order
- The outputted **code** will change every 10 seconds so try to give yourself the most time
- Copy the **code**
- Paste the portion of the **code** into the very last portion of the below URL
  - `https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string=`**code**

`flag: wh1te_Ro$E`

</details>
