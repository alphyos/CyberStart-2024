## WALKTHROUGHS

# Broken Banks

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, a gang is sending fake banking emails to unsuspecting
customers to try and defraud them. We have been given one of these scam
emails and are looking to find something suspicious within. We need to
click on the part of the email that leads us to believe it is fake,
which will give us the flag to complete the challenge.

## Solution

When attackers attempt to send emails impersonating a particular
company, they will often try to purchase a web domain that is similar
enough to the genuine website as to potentially evade notice.

If we take a closer look at the *header* section of the email, where we can see the **from** and **to**
 email addresses, we can see that the from address isn't quite right!
Judging by the email content, the company this email is allegedly from
is cloudnine bank; however the email address domain is cloudninebank*k* with an extra k.

This is definitely something suspicious! We can click it, and we'll
see the success message at the top of the screen, including the flag we
can submit to complete the challenge.

## Real-world Uses

A common technique in scam emails is to send an email from a domain
name that's very similar to the legitimate domain. Perhaps there's an
extra letter, or an `i` is changed to an `l` in the scammers' domain name; the characters can look very similar and so easily overlooked by the victim.

This can be an incredibly effective aspect of a scam email. If the
user is unaware, or busy (or both), they may simply focus on the content
 of the email - which could include some fantastic special offer, an
alarming warning or something else to get the user to act emotionally.
Often they'll be clicking a link to a scam website (which can look very
similar to the original site) and unwittingly enter their login details,
 which are sent to the scammer. The victim is effectively tricked into
giving away their credentials.

<div align="center">

[← Previous: 8.03.01 - Social Secret](SocialSecret8.3.1.md) | [Next: 8.03.03 - Happy Customers →](HappyCustomers8.3.3.md)
:-|-:
