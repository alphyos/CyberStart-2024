## WALKTHROUGHS

# Social Secret

## Briefing

Before jumping into the walkthrough, let's check the challenge briefing to confirm what we need to do for this challenge.

To summarise, we want to try and log in to a social media account
belonging to a gang member, and we're going to attempt to do so via the
site's password reset form. We already have some key information - his
username and favourite colour; we just need to try and figure out his
age.

Once we guess the correct age and successfully submit the password
reset form, we'll receive the flag and can complete the challenge.

## Solution

The setting for this challenge is actually quite a common scenario.
Whilst in this instance we're using our powers of deduction to get into a
 cyber criminal's account (with permission!); this is something we could
 all fall victim to if we overtly share our personal information.

We're looking for the user's age. In the username - lars\_1986 - we
have a year; we can reasonably assume this might be the user's year of
birth, as including information such as this is quite common in people's
 usernames and passwords.

Given we're looking for the user's current age, we can guess that by
taking the current year and subtracting 1986 from it. We can submit the
age to the password reset form to see a success message at the top of
the screen, containing the flag we're looking for. Submitting this in
the toolbox on the left completes the challenge.

## Real-world Uses

People can make some pretty poor choices regarding their personal data, but it's all too easily done. Perhaps `lars`
 was already taken as a username, and they had to add something extra
when signing up to make it unique. Adding a year of birth is a pretty
common next step in this scenario. However, it's a bad choice to do this - as anywhere the username is shown, it's informing people of the
persons age! There are plenty of other ways to make the username unique
in a site and not give away sensitive information - why make yourself
vulnerable?

Always be mindful of what personal data you might be giving away,
especially when using social media. Hackers can spend a lot of time
doing reconnaissance, but there's a lot of tools out there that can help
 automate the process too, so a hacker can quickly gain a profile of the
 victim. Don't make it easy for them!

[← Previous: 8.02.04 - Rover Rodeo](https://play.cyberstart.com/field-manual/789ab952-ade9-11ed-afa1-0242ac120002)
[Next: 8.03.02 - Broken Banks →](https://play.cyberstart.com/field-manual/f2860f0c-0e88-11ec-82a8-0242ac130003)
