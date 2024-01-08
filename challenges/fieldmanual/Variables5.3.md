## PROGRAMMING

# Variables

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/c1cf7c85-dd14-45cc-a69f-514b8f82a9e1" width="800" />
</div>

## Basic data storage

Variables are a core component of programming and you'll be using
them a lot! Basically, a variable is just a reference to a container
storing some kind of information. They're a way we can say to our
program "hey, store this data so I can interact with it later".

A variable can contain lots of different *types* of data. We're going to look at those in more detail in the [Data types](https://play.cyberstart.com/field-manual/8fc88b98-d7eb-11eb-b851-0242ac140009) page, but for now lets try and understand the basic uses of variables and some neat things you can do with them!

```py
# Counter
counter = 1000
print(counter)
counter = counter - 1
print(counter)

# Base website address
address = "http://www.sans.org/cooltest.php?userid="
print(address + "123")

# String demos
print(address[0])
print(address[0:3])
print(address[-3])
print(address[7:])
```

Here's an example Python script demonstrating a few uses of
variables. Let's work through it. The first line is a comment, useful to
 set notes or helpful information for us to refer back to later. On the
second line we set our first variable - `counter`. Here we tell Python we want to store the value `1000` against this variable, using the `=` character.

On the next line, we ask Python to print this value out using our
variable to reference it. If we were to just run those first three lines
 of code, we'd see something like:

```console
$ python3 test.py
1000
```

A variable doesn't always have to stay the same. On the next line, we modify our variable by asking Python to replace `counter` with the value of `counter` minus 1. We can imagine Python would interpret this as something like `counter = 1000 - 1`. Similarly, we then print the new value. If we again just run this top portion of code we'd see something like:

```console
$ python3 test.py
1000
999
```

Here we can see at line 3 in our code the variable `counter` contains `1000` as we have originally set. Then, after modifying it, it now contains `999`!

In the next section of code, rather than storing a number in a
variable we instead store a string; in this case a web address. Note
it's missing a value for the `userid` parameter! In the next line we can print the `address` variable, but also *concatenate* an additional string on the end using the `+` character. If we ran those two lines of code only we'd have seen:

```console
$ python3 test.py
http://www.sans.org/cooltest.php?userid=123
```

Neat!

The last section of this example demonstrates a few ways we can interact with the `address` variable in Python. Using square brackets after the variable name, we can request a *portion* of the variable based on what we specify. Let's run the last set of examples and see what they do:

```console
$ python3 test.py
h
htt
i
www.sans.org/cooltest.php?userid=
```

Interesting! The first line, `print(address[0])`, told Python to display the character at **index 0** of the string - also known as the first character. If you were to split the string into individual characters, the **index** is the number associated with a given character. Notice it starts at 0! For example, h = 0, t = 1, t = 2, p = 3, and so on.

So, for the next line, `print(address[0:3])`, the colon allows us to specify a **range** of characters, starting with index 0 and ending **at** index 3. Hence the output `htt`! You'll notice that the end index isn't included in the portion, it stops *before* the end specified.

In the third line, `print(address[-3])`, we provide a
negative index. This will wrap from the beginning of the string to the
end. If we count 3 characters in from the end of original string (`http://www.sans.org/cooltest.php?userid=`), we reach the letter `i`.

Finally, the last example `print(address[7:])` starts at
index 7 and requests a range, but as we didn't provide any end value it
just grabs everything after the starting point!

> Variables can generally be given any 'name', or reference - you could name a variable `x`, `y`, `abc`
> and so on. However, when reading through your code it might not be
> immediately obvious what those variables are for, or what they could
> contain. A great habit to build is naming variables descriptively:
> seeing the variable `address` provides much more information than `x`. Name descriptively right from the start of your programming journey, it's a good habit to start with!

[← Previous: 5.02 - Running python programs](https://play.cyberstart.com/field-manual/8fc688ca-d7eb-11eb-84c6-0242ac140009)
[Next: 5.04 - Data types →](https://play.cyberstart.com/field-manual/8fc88b98-d7eb-11eb-b851-0242ac140009)
