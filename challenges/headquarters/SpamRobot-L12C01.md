# 👨‍💻 Spam Robot - L12 C01

Agent 707, because of your great work on the previous level the gang have struggled to find a way to get physical access to the bank. So it looks like they are testing ways to get a package containing a small robot into the building which they can use remotely.

They plan to send it to one of the senior management as a gift from a friend (who the manager is unaware belongs to the Bulldog gang). When the manager plugs it into his computer to charge up via USB, it will hijack the computer and access his email. With this access, the gang will send a specific spam email, which the robot will use as a trigger to start an attack on the banks servers from the inside!

To help narrow our investigative efforts, we need to know which gang member is behind this new idea of theirs. Agents have managed to recover a log file and a mail queue of pending outgoing email spam messages. See if you can spot the spammer in the log file and let us know - we can then stop them sending the email.

**Tip:** The flag is the username of the gang member sending the spam.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Think about the traits of a spammer - they typically send a huge volume of emails.
   Is there a user who appears to send way more emails than other legitimate users?
```

</details>

## Files

- [log.txt](/assets/spamrobot1.txt)

<details><summary>

## Step by Step</summary>

- Download the text file and open it, try to see who is sending the most emails
- The username with the most frequent occurrence (~350) is james_joseph

`flag: james_joseph`

</details>
