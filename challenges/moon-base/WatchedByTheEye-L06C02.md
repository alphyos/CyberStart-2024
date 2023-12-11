# 👁 Watched by the Eye - L06 C02

The aliens have got on to our Moon Base network; we don't know how but we know they're watching what we're doing.

We need to keep communicating in a secret way. See if you can write a script to hide some text in an image file at /tmp/image.gif by appending it to the end of the image. That way we can send random images back and forth to communicate without them knowing.

Test your script by hiding the text "alieneye" in the file.

**Tip:** Hide the text "alieneye" in the file to get the flag.

```
💡 Hint: This one is easier than it sounds. Don't get thrown off that it's an image file.
   
   Treat it like a text file. Remember you want to add text to the end of the file, not overwrite what's already there!
```

## Answer

```python
file = open("/tmp/image.gif", "a")  
file.write("alieneye")
```
