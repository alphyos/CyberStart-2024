# ⛩ Spam For Dinner - L13 C01

Agent 707, we're trying to distract the gang whilst we try and gain access to their primary server and we think we've found a target for you.

We want to spam the booking form for their restaurants, the problem is the form is protected by a Captcha. You may be able to bypass the Captcha by tricking the form into using a different Captcha value; and if you can do so at least 5 times, that'll prove a successful bypass for the bot we'll create!

**Tip:** How are strings sometimes generated?

<details><summary>

## Need a hint?</summary>

> 💡 Hint: By searching "seedID" in the source code, you’ll discover a line of code that eerily matches something you would append to a url.

</details>

<details><summary>

## Step by Step</summary>

- Change the url to these 5 links, reload the page, and solve the captcha
  - `https://jiaozi-restaurants.com/booking-form?venue=shanghai?t=login_form&seedID=4:9:14:19`
  - `https://jiaozi-restaurants.com/booking-form?venue=shanghai?t=login_form&seedID=17:0:5:10`
  - `https://jiaozi-restaurants.com/booking-form?venue=shanghai?t=login_form&seedID=19:2:7:12`
  - `https://jiaozi-restaurants.com/booking-form?venue=shanghai?t=login_form&seedID=20:3:8:13`
  - `https://jiaozi-restaurants.com/booking-form?venue=shanghai?t=login_form&seedID=1:81:6:11`
- The flag should show up

`flag: mHpDS1kQoesVHs5CL0m8`

</details>
