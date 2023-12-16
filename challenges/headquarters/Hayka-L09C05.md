# 🖨 Hayka - L09 C05

Remember we said the Spetzners were mad scientists? Well, one of the gang, Vladimir, is an actual scientist, and runs an official scientific paper submission site called Hayka. But here's the thing - the server he runs the site from is his own, and we think he's also using it to store the gang's secret plans.

We want you to take a look at the scientific paper upload page, we think it might be vulnerable. See if you can upload a PHP file which will output the code word "b1n4ry" to the screen when you visit the page.

**Tip:** Upload the correct file and visit the file page to get the flag.

💡 **Hint:** Make sure your php file has the right extension and contains actual PHP code.
   The goal is to demonstrate that you could have run malicious code on the server if you wanted to.

## Step by Step

- Create a new .php file with the following contents and with your chosen `filename`

```php
< ?PHP
echo "b1n4ry"
? >
```

- Upload the file to the page
- Change the url to https://www.hellohayka.com/`filename`.php
- The flag should appear

`flag: 7ADEvbYwJXzEw3tIcCB0`
