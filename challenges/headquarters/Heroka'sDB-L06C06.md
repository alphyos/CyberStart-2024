# 🏎 Heroka's DB - L06 C06

In the previous level you may have been part of the investigation into Heroka. She recently created a site where she posts photos of her favourite cars. That investigation revealed that the site was vulnerable to injection and that she's been hiding details about their plans there.

We think that some results from a search of the site are also hidden unless you're logged in. We don't have any login details, so perhaps you could use SQL injection to get all the results. Think about which SQL query is run when you submit the search form.

**Tip:** Get the full results and then you'll get the flag!

<details><summary>

## Need a hint?</summary>

> 💡 Hint: An SQL query is running in the background when you submit the form. The SQL query refines the results from the database to your search by using `WHERE = 'your search input'`. Can you modify the `WHERE` statement to always be true?

</details>

<details><summary>

## Step by Step</summary>

- At the top right search bar in orange, type the following
  - `SELECT meow FROM cats WHERE cat_name = 'Rodney' OR 1 = 1`
- When you hit enter the flag should appear

</details>
