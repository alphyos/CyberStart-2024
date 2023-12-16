# 💼 Open Box - L11 C12

It looks like Billy Johnson, one of the gang's enforcers, is using a cloud storage service to keep his files secure. We know he has an account and we know his password, but we don't know his account name.

Our team have created an account with the service and logged in. See if you can find a way to trick the site into giving you a list of accounts.

**Tip:** Billy Johnson's account name is the flag.

```
💡 Hint: User input can be anything, not just a form field. What would happen if the value of a cookie
   was used to get data from a database. Could it also be used for SQL Injection?
```

## Step by Step

- Start by creating a new cookie with whatever name you desire by opening up inspect element/dev tools and moving to the applications tab
- The value of this cookie should be “`WHERE name = ‘Billy’ OR 1=1`”

![image of the new cookie](/assets/openbox1.png)

- Reload the page and you should be redirected to the admin page will all the account details
- `Billy Johnson's` account name is in the left column, it will be the flag

`flag: billy_goats_gruff`
