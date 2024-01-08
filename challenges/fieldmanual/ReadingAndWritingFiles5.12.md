## PROGRAMMING

# Reading and writing files

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/8d2e0caf-2f02-45a3-b94e-bc3919906c20" width="800" />
</div>

## File I/O

Reading and writing files is a pretty important skill to have in
programming. Whether it's reading config files, attempting to crack a
password on a zip file or even crawling a website and making copies of
interesting files you find; you're likely to need to interact with files
 programmatically at some point.

There's quite a few different ways to interact with files in Python.
Some are more robust and structured, while others are more "quick and
dirty" for hacking together quick scripts. We'll focus on the latter
here and dive into a quick example:

```py
reader = open("file.txt", "r")
print(reader.readline())
print(reader.read(10))
reader.close()
```

```console
$ python3 test.py
Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Donec plac
```

Here we're attempting to open a file `file.txt` (in the same directory as the script), specifying we want to open in read only mode by providing the second argument `r`.

The first line of printed data is using the function `reader.readline()` - as the name suggests, we're reading a whole line from the file.

The next line of printed data is using the function `reader.read()` - this instead reads a specified amount of characters from the file, in our case `10`
 as we requested. Notice that the 10 characters read are not the same as
 the 10 characters from the first line as it continues to read data from
 where it previously stopped; the end of the first line. Think of there
being a "pointer" at your current position and you read more, the
pointer has moved on.

We then close the file handler `reader`. Usually this is
good practice, once you're finished with the file, as it prevents any
acciental data being written or other unwanted file interaction. Given
we opened the file in read-only mode here it doesn't really matter, but
it's a good habit to build.

What about writing to a file? Let's have a look at another example,
but first, be warned! When writing to files it's easy to accientally
overwrite data, so always double-check your code is doing what you
expect.

```py
log = open("log.txt", "a")
log.write("I am logging something")
log.close()
```

As before we create a variable containing a file handler, using the `open` function. Here we're using the file `log.txt` and opening the file in **append** mode - `a`.
 In this mode data will be appended to the end of an existing file,
retaining any existing file contents and merely having your additional
content added at the end.

When we run this code, if the file doesn't already exist it will be
created, and the specified data written to it. If we run it multiple
times, you'll notice the data is being added to the end each time.

If you specifically want to overwrite the existing data each time, the file can instead be opened with the `w` argument for **write** mode. Here, any existing data will be deleted and replaced with whatever data is written between the `open` and `close` of the file.

There are some more advanced use-cases for files we can briefly cover
 as well. So far we have been reading and writing in text mode, dealing
with bytes that are being interpreted as ASCII characters. However, we
might not always want to work with a file containing only text
characters - maybe we want to open an image instead. Here we can use a
binary write and read mode:

```py
with open("file.jpg", "rb") as image:
    print(image.read(10))
    image.close()
```

```console
$ python3 test.py
b'\xff\xd8\xff\xe2\x0cXICC_'
```

The syntax is slightly different here, but we're doing roughly the
same thing. Effectively, we're telling Python "with the result of the `open` function as the `image` variable" and then starting an indented code block, with the `image` variable then available in that indented block.

Notice here we're opening the file in `rb` mode - **read binary**
 and the indented code block is specifying we want the first 10 bytes of
 data to be read and printed. Not something you need to focus on too
much right now, but this functionality can be very powerful when
starting to work with file manipulation, advanced cryptography and more.

Finally, it's worth noting that these examples don't have any
exception handling, something we haven't covered in the Field Manual.
Simply put, if something goes wrong it'll usually result in an **exception** being **raised** or **thrown**.
 This is common when working with files as there's lots of points of
failure: the file doesn't exist; the program doesn't have permission to
read the file; the filesize is too large; plus other issues you may want
 to account for.

Something worth researching is how to **handle** these
exceptions so that your code can fail more gracefully, presenting
relevant messages to the user or behaving differently depending on what
kind of error has occurred.

We hope that this chapter of the Field Manual has given you a great
start with your programming journey, but it's really only covered the
basics. If you've enjoyed the start we've given you here, we'd advise
you to continue your learning by searching for more knowledge online;
there's so many great resources to learn from and so much to learn. Have
 fun and keep learning!

We hope that this chapter of the Field Manual has given you a great
start with your programming journey, but it's really only covered the
basics. If you've enjoyed the start we've given you here, we'd advise
you to continue your learning by searching for more knowledge online;
there's so many great resources to learn from and so much to learn. Have
 fun and keep learning!

[← Previous: 5.11 - Modules](https://play.cyberstart.com/field-manual/8fcf541e-d7eb-11eb-af45-0242ac140009)
[Next: 6.01 - Introduction to binaries →](https://play.cyberstart.com/field-manual/8fe3a086-d7eb-11eb-b2fc-0242ac140009)
