### CRYPTOGRAPHY
# Substitution Ciphers

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/32279986-a16e-42ce-b8f9-f1946e3fd728" width="800" />
</div>

# Switch it up
A **Substitution cipher** is a way of encrypting data, where every occurrence of specific letter from the alphabet within the plaintext you supply, is substituted by another character from the alphabet. This encrypted series of characters is given to the recipient, who knows what the character substitutions are and can reverse the process to get the plaintext back again.

For example:

```txt
A = X
B = D
C = H
D = S
... (and so on)
```

The key here is the arrangement of letters mapped to the original. If you possess the above key (in full) then returning the data to the original plaintext (decryption) is trivial - simply reverse it. There may be more complex substitution methods, for example, pairs of characters `AB = MK` rather than singles, but the above is a common and simple method.

You can also apply the same logic to bytes. If the same substitution is used throughout the message the cipher is referred to as monoalphabetic, whereas a polyalphabetic cipher uses a number of substitutions at different positions in the message.

>Substitution ciphers also don't have to work with letters and/or predictable ASCII values! You could substitute characters with weird pictograms or emoji - it can be fun and confusing to look at which makes it more challenging!

# Breaking Simple Substitution Ciphers

As time has passed and with the addition of computers and the internet with incredible processing power, breaking these ciphers became trivial; particularly for a simple substitution cipher. However, it's still a great introduction to simple cryptography. If you search online, you'll find plenty of tools which will take encrypted text and attempt to decrypt it automatically by trying all variations and when it detects a few readable words, decide that's an answer to show you.

If you want to try a more manual approach to breaking substitution ciphers, you can use **Frequency Analysis**. This initially involves understanding some of the most commonly used letters - specifically `e`, `t` and `h` - and perhaps looking for the same groups of 3 letters, taking a guess those might be the word `the`. If you're right you'll have the added bonus of revealing parts of other words that contain those letters. Let's look at an example:
```txt
mit egrt ol xtkb lmkgfu of miol gft
```
We might take a guess that `mit` actually decrypts to `the` as it's 3 letters and the letters appear often. Let's try that as a starting point; we'll swap the letters to uppercase as we replace them:
```txt
THE egrE ol xEkb lTkgfu of THol gfE
```
A great start! Another common word, would be `is`, which has as both `i` and `s` - both common letters as well. In fact, we have 2 groups that start with `o` in groupings `ol` and `of`, these might be words such as `is`,`in` etc. Let's take a chance on `ol` being `is`, especially as it would make `THol` the word `THIS`.
```txt
THE egrE IS xEkb STkgfu If THIS gfE
```
This is looking positive with just 2 guesses. If we took a guess at `f` being `N`, we'd reveal `IN` and the last group `gfE` could be `ONE`, so that seems likely.
```txt
THE eOrE IS xERb STkONu IN THIS ONE
```
We can probably make some final educated guesses that we've likely got the word `STRONG` and with just a few of letters left can finally guess the full message:
```txt
THE CODE IS VERY STRONG IN THIS ONE
```
Hopefully this demonstrates that starting with a little knowledge on common letters and words, we can try some educated guesses, and you can actually decrypt messages yourself fairly quickly (there's also tools online to assist you with the above). It takes a little smart guessing but is absolutely feasible. All of this presumes we know a little about the message, or even ideally a word that is used in it. In cryptography this inside knowledge of the plaintext is called a `crib` and tools online may boost your efforts in what's known as `crib dragging`.

>These ciphers are not the strongest, but they are a wonderful introduction to making and breaking codes before you need more maths.

### <div dir="rtl">[→ Next: 3.3.2 Caesar or ROT ciphers](CaesarOrROTCiphers3.3.2.md)
