## PROGRAMMING

# Data types

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/65a490d2-d0d4-4743-8c97-fa9759ed0b4b" width="800" />
</div>

## How long is a piece of str?

In this section we will walk through data types. Python is a
dynamically and strongly typed language, which is a fancy way of saying
it really cares about the **type** of data, but it is quite
 flexible with the interpretation of those types allowing us to express
them in different ways at different times.

For example, if we had the following Python code:

```py
# Integer
x = 13
# Float
y = 13.333
# String
z = "13.0 hello"
```

Here we're setting a few different types of variable. `x` is a whole number, so Python will likely interpret it as an **integer**. `y` is a number with a decimal place, which will result in a **float**. `z` is defined within quotation marks, and as such it is a **string**.

As mentioned above, Python is *dynamically and strongly typed*, meaning we can do some fun things with these variables. Suppose we had this line of code:

```py
print(int(y))
```

This would print the variable `y` to the screen, but as it does so, we're asking Python to dynamically alter the type to an **int**eger. The output of this would be `13` - as integers can only contain whole numbers and Python adjusts the
variable accordingly. We also haven't overwritten the original value for
 the variable `y`, instead we've just asked Python to *temporarily* change the type within the `print` function.

Similarly, we could add this line of code:

```py
print(float(x))
```

The result of which would be `13.0`. We've asked Python to convert the integer of `x` into a float, which contains decimal places by default, and so Python has dynamically altered the original value accordingly.

Here we're using some of Python's [built-in functions](https://docs.python.org/3/library/functions.html)
 to interact with variables. If you take a look at the documentation
you'll see a few others that can be used for manipulating variable
types, for example `str` and `bool`.

Along with the more simple uses above, Python also allows us to work with hex values or even byte sequences. For example:

```py
# Integer
x = 254
print(hex(x))
```

If we were to run the above code, we would see the value `0xfe` - as requested Python has converted our integer type variable into hexadecimal. Or another neat example:

```py
# Hex string
y = "\x41\x42\x43"
print(y)
```

Here we have a string containing hex values. If we run this code,
Python is able to interpret these hex values to create a string of ASCII
 characters - `ABC`.

This is quite handy as often when we're interacting with applications
 they use encoding schemes or alternative representations of data such
as hexadecimal, and Python's dynamic interpretation makes this a lot
simpler to work with!

At it's core, Python is pretty intuitive with the types of data it
picks for the values you're storing. But as we have demonstrated here,
you can also provide your own instructions to ensure the data exists in
the type that you need. As your programming skills improve, you'll gain a
 better understanding of where and when different types of data are
particularly important!

<div align="center">

[← Previous: 5.03 - Variables](Variables5.3.md) | [Next: 5.05 - Mathematical functions →](MathematicalFunctions5.5.md)
:-|-:
