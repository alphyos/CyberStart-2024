# 🍽 Custom Plates - L06 C10

We've just had some new intel. The Yakoottees are planning to change the supercar's numberplates to British plates when they steal it. For some reason, rather than create their own, they've ordered some from a site online called CoolPlates. We want to see which plates they've ordered and where they're being sent.

See if you can get into the site so we can find out. We don't have a username and password but we think it uses some simple JavaScript security checks.

**Tip:** Log in to get the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: The JavaScript has been obfuscated on purpose.  See if you can find the value that it is checking your input against to bypass the login page.

</details>

<details><summary>

## Step by Step</summary>

- Look at the page source oode and you will find this login script

```html
<script>
// Start our login process
var doLogin = function (uname, pword) {
  // Notes here for login, incase I forget
  // Username is 'yk1' and password is
  // using our amazing encryption system...
  var axle = 319;
  var brake = 24;
  var carburetor = axle * brake;
  var door = "pass" + (carburetor / 2);
  var engine = door + "go";
  var password = engine + 123;
  // Right that's all done and the password established
  // Attempt a login now with what the user provided
  tryLogin(uname, pword);
}
</script>
```

- The comments say the username is `yk1`
- If you work out the variables, the password is `pass3828go123`

</details>
