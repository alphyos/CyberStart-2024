## WALKTHROUGHS

# Hidden Report

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we have access to an account page on a gang's online
bike store. There, we can generate a report of our transactions, and we
think there might be a vulnerability here we can exploit. Specifically,
we need to try and view a transaction report for the **very first user** of the site.

Once we're able to access this report, we'll be given the flag we need to complete this challenge.

## Solution

As the briefing suggests, we want to take a look at the transaction
report section to see if we can find a vulnerability we can make use of.
 On the initial page, we can click the "Generate report" button to see *our* report.

There's nothing particularly note-worthy about the content in our
report. However, if we look at the URL in the challenge browser, we can
see that the page we're on is `/account/transactions-user-456.txt`. Reading this through, it almost looks like "transactions *for* user 456", so we could make the assumption that 456 is the user ID for our account.

Our user ID isn't very complicated; it's just three numbers. This
might suggest that the account IDs are automatically incrementing for
each new account - the very first account that was created was given the
 ID 1, the next 2, and so on.

As the briefing notes, we want to access the report for the very first user, potentially user ID 1, so let's change the `456` portion of the URL to `1` instead, and submit the URL.

Success! We have gained access to another user's transaction report,
specifically user 1, and we're given the flag we can submit to complete
the challenge.

## Real-world Uses

Websites have come a long way from their "static" (not changeable)
beginnings, and today we're used to "dynamic" (changeable) data in rich
web apps. A typical setup would be for a logged-in user to have their
reference ID sent to the server everytime a new page is requested, so
the server knows what account details to provide.

However, what if the user ID is guessable (perhaps incremented; that
is, each user simply has the next number available), can you can attempt
 to request data for another user using that ID? If there's poor
security, the server can willingly give you content for that other
account. It may sound it would never happen, but with web apps doing so
much, it only takes a oversight of security by a web developer in one
area to provide the ability to leak content for any account to a
determined hacker, and one leak can then lead to so much more!

[← Previous: 8.03.07 - Secret Caesar](https://play.cyberstart.com/field-manual/81c783e4-0e89-11ec-82a8-0242ac130003)
[Next: 8.03.09 - Bike Fan →](https://play.cyberstart.com/field-manual/bfb59632-0e89-11ec-82a8-0242ac130003)
