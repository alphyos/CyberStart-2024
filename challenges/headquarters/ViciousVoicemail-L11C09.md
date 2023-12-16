# 🗣 Vicious Voicemail - L11 C09

Agent 707, once again we need you to step up and show us your skills. This time you need to stand in for Agent V, our resident audio expert, as he's been called up to help the team on the next level with a special mission.

Before he went he was able to get access to the private voicemail system the Bulldogs were using. He got access by logging in as one of the gang members, Terry Turner, and we can see there are a set of voicemails on there for him. Agent V didn't have chance to analyze them before he went, can you do it for him? We think there might be hidden messages in the audio files.

**Tip:** Find the hidden message to get the flag.

```
💡 Hint: You'll need to work out how to install a program on Linux to do this one.
   Check out '`steghide`' and find out how to install it. Then use it to extract the hidden message.
```

## Files

- [voicemail-01.59177932.wav](/assets/viciousvoicemail1.vaw)

## Step by Step

- Download the first audio file
- Run `steghide --extract -sf [filename]`
- You do not need a passphrase here, simply hit enter
- The flag should be written to a file called `flag`

`flag: sTg9UtlFLRUOXt7tTSS`
