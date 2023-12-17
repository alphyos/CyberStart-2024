# 📦 Multiple Boxes - L12 C12

Could this be the icing on the cake? Remember Filebox, the cloud storage site Bulldog gang member Billy Johnson was using to store his files? Well, it seems he's not the only gang member to store his secret files there.

As we know it's vulnerable we want to look at other ways to find the gang's files. We think the files can be exposed with directory traversal and there are some two levels up from the account page. See if you can get access to them.

**Tip:** Find the file to get the flag.

```txt
💡 Hint: Looks like this web server is setup to filter out common directory traversal attempts.
   Could you use some character encoding to bypass the filter? CAPEC 79
```

## Step by Step

- Replace the url with the following
  - https://www.easy-filebox.com/u/2374682/user/files..%2F..%2F..%2F..%2F..%2F..%2F..%2F
  - The flag should appear

`flag: Lpa8LauYxLKeUuiUUT6X`
