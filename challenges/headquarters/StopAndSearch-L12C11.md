# 🔎 Stop and Search - L12 C11

Agent 707, with all of the knowledge we have gathered about the trojan robot and the gang's plans for it we have been working with the bank to improve their security. We're currently doing penetration tests on all their internal systems and we've identified a possible XSS flaw in their contact management system, in the contact search field to be specific.

Here's a javascript payload, see if you can get it to work in the search field.

`<script>alert('Search this!!!')</script>`

Once this flaw has been fixed we are confident that the trojan robot the gang have been planning to send will have no effect on the banks system therefor rendering it useless! Good luck!

**Tip:** Submit the payload correctly to get the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: This page is filtered to prevent normal XSS but you should be able to hex encode the payload.
   Don't forget to browser encode it too!
```

</details>

<details><summary>

## Step by Step</summary>

- If you use a [hex encoder](https://www.convertstring.com/EncodeDecode/HexEncode) to transform the original payload, it will go through the filter.
- Type and enter the following:
  - `3C7363726970743E616C6572742827536561726368207468697321212127293C2F7363726970743E`
- After dismissing the alert, you should get the flag.

`flag: 1if06H1L7NJ9xPUy14me`

</details>
