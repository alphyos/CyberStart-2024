# 💼 Open Box - L11 C12

It looks like Billy Johnson, one of the gang's enforcers, is using a cloud storage service to keep his files secure. We know he has an account and we know his password, but we don't know his account name.

Our team have created an account with the service and logged in. See if you can find a way to trick the site into giving you a list of accounts.

**Tip:** Billy Johnson's account name is the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: User input can be anything, not just a form field. What would happen if the value of a cookie was used to get data from a database. Could it also be used for SQL Injection?

</details>

<details><summary>

## Step by Step</summary>

- Start by navigating to the cookies in the web console
- Change the value of the cookie called `SQL_SESSuser` by appending `' OR 1=1` to what is there already

![image of the new cookie](/assets/openbox1.jpg)

- Reload the page and you should be redirected to the admin page will all the account details
- `Billy Johnson's` account name is in the left column, it will be the flag

`flag: billy_goats_gruff`

</details>
