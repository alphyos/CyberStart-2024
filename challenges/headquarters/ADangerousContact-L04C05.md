# ☠️ A Dangerous Contact - L04 C05

During our research into The Choppers, we noticed that their website has a contact page with a form for getting in touch. Our agents want to know whether it might be vulnerable to SQL injection.

See if you can put the SQL code in the right order. If you do, the data should appear in the console at the top of the page. This will contain the information we're looking for - a list of all previously submitted messages.

**Tip:** The flag is the last name of the most recent person to send a message through the form.

```txt
💡 Hint: This is a test on SQL injection. You have to get the whole table of information by running the right SQL command, so
   re-order the parts of the command in the message box and submit the form. Try starting with the single quote character,
   which will close the speechmarks in the command and then think about what is always true.
```

## Step by Step

- Reorder the boxes to properly inject SQL into the webpage.
- A display should pop up, copy the last name of the most recent entry, and submit it as the flag.

![picture of the correct sql arrangement](/assets/adangerouscontact1.png)

`’)’ SELECT first_name, last_name, email, message FROM messages;—`

![picture of the sql output display](/assets/adangerouscontact2.png)
