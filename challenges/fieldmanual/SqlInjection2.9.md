## WEB

# SQL injection

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/d79e32fb-4d60-4a05-91c6-69f47b3b998f" width="800" />
</div>

## Meddling with databases

SQL injection (SQLi) is a more difficult topic that can take a few
reviews before students grasp it. Practicing it in CyberStart will also
help you to understand why this attack category is significant.

At a high-level SQL injection enables you to trick a web application
in to altering a query it makes to a SQL database, and by doing so
return different data to what was originally intended. It might even
enable you to modify a database, or download and even delete the entire
database! It can be complex to understand how this works, so let us work
 through it with an example.

> If you have never used SQL you may find this section difficult to
> understand, and may wish to search for basic tutorials on database
> queries using SQL before you begin.

Most web applications you interact with are connected to a database
of some sorts. Think about it, every time you log in with a username and
 password the web server must go 'somewhere' to validate whether you
provided good information or not. What about when you are playing a
game? Something has to store your points, interactions, events and state
 data. Web applications will classically be backed by a database to load
 content, users or other dynamic content. Still to date one of the most
popular types of database is a relational database system, such as MySQL
 or MariaDB. These are databases that use SQL (Structured Query
Language) to query or update the database.

For example, if you have a database table called `users` as follows (*Ignore that storing passwords in plaintext like this is bad, it merely helps illustrate the attack!*):

| user_id | agent_name | agent_in_field | password |
| --- | --- | --- | --- |
| 1 | Agent J | Y | Pass123 |
| 2 | Agent Q | Y | passw0rd |
| 3 | Agent X | N | akjsdh1123! |

Imagine now that our web application has a login form, where agents can log in. The `agent_name` and the `password` are provided by the user and substituted into the query, e.g.

```sql
SELECT user_id FROM users WHERE agent_name = '<insert_login_name>' AND password = '<insert_login_password>';
```

The `<insert_login_name>` and `<insert_login_password>` are provided by the user and substituted into the query (the `<` and `>`
 characters are just to denote that user data is inserted at this
point). Your browser submits the data, the server code grabs it and
places the value into this query, which is subsequently executed. For
example, if we supply the right details for Agent Q the query would be:

```sql
SELECT user_id FROM users WHERE agent_name = 'Agent Q' AND password = 'passw0rd';
```

This would return the `user_id` of 2 as the `WHERE`
 has a valid lookup entry. This is where SQL injection comes in. What
happens if a user can provide unexpected data to change the *structure* of the query? For example, in the login form we will set the `agent_name` as `bob' OR 1=1 -- //`. Looks weird right? Well, let's see what SQL structure the web server will create:

```sql
SELECT user_id FROM users WHERE agent_name = 'bob' OR 1=1 -- //' AND password = 'passw0rd';
```

Whoah! Look at that! Notice how the second part of the query is now beyond `-- //` so ends up in a comment? The user input has been restructured the query and is now basically equivalent to:

```sql
SELECT user_id FROM users WHERE agent_name = 'bob' OR 1=1;
```

We *tricked* the web server into running a query other than
the one it intended! SQL injection! There is no agent called 'bob', so
it considers the next part and confirms 1 equals 1. That results in `true`
 and 'truthy' values such as this are often seen as a passing condition,
 therefore the database proceeds to return records. However, as the
'match' contains no specific user, **all** the users will be returned!

The web application will maybe then try and log us in as one of these
 users (perhaps first or last), but really, who knows what will happen!
How this strange situation is handled will be dictated by logic in the
web app - it might, not understanding the situation and what number to
use, make you user 0, which is quite often known to be admin. Or likely
now seeing the output of all usernames, you could now try a new SQLi for
 specific users, to be anyone. You can probably see why this is so
dangerous now, right?

SQL injection mastery is a much bigger topic. It could require some
careful tweaking to produce an injection that works as expected, as
there may be parametrised queries (making attacks vastly harder) or
perhaps to a lesser degree - filtering and enforcing variable types or
defining accepted characters. You may be lucky enough to get error
messages which indicate *how* things are erroring, so you can
adjust your attempts, otherwise will need to guess and try lots of
variations as you're working 'blind'.

**Remember, using this technique on a target that has not given you permission could violate local computer crime laws!**

> Manually crafting SQL injection or hunting for it on pages with many
> user inputs can be a pain. After all, each form element or user input
> might connect to a different query, and maybe only one or two of them
> are vulnerable. You often have to search for the one mistake the
> developer made, and only the worst sites have many vulnerable points.
> Tools like [SQLMap](https://sqlmap.org/)
> can expedite this hunting and exploitation process, and even automate
> much of the process to build more advanced SQL injection inputs.

<div align="center">

[← Previous: 2.08 - Cookies and sessions](CookiesAndSessions2.8.md) | [Next: 2.10 - Command injection →](CommandInjection2.10.md)
:-|-:
