# 🌌 Baffled By Browsers - L05 C11

Whilst monitoring the gang's web traffic, we noticed they've been visiting one particular page quite a lot. When we try we get rejected immediately without it even asking for a username or password.

Our field agent, who is working for the Yakoottees undercover, thinks it might be something to do with a particular browser that the gang built themselves called "Orion". Time for you to investigate. Try looking for a developer tool in the browser to help you out.

**Tip**: To get the flag, get access to the page!

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Do you know much about browser agents? Each browser sends a user agent to each web page it visits. This user agent tells the website which browser you are using. If you can figure out how to change it, you might be able to make the page think you're using the browser that the Yakoottees use.

</details>

<details><summary>

## Step by Step</summary>

- Use inspect element and click the three vertical dots in the top right corner
- Mouse over to `More tools`
- Click on `Network conditions`

![picture of the tab navigation](/assets/baffledbybrowsers1.png)

- At the bottom is a newly opened tab, scroll down to `User agent`
- Uncheck `Use browser default`
- Type `Orion`
- Reload the page and the flag should appear

![picture of the user agent box](/assets/baffledbybrowsers2.png)

</details>
