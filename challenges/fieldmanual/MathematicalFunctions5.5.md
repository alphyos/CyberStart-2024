## PROGRAMMING

# Mathematical functions

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/8a04996f-1090-4ba6-8234-73636580c362" width="800" />
</div>

## Making maths easy

As you're building programs and applications you're going to run into
 scenarios where number manipulation is important. Maybe you're trying
to solve an interesting homework problem, or trying to come up with a
clever way to find the next number in a sequence for a tool you're
building. For these kinds of tasks, Python has a great built-in module
we can make use of: the `math` module.

Let's take a look at some examples of how we can use it.

```py
# Import the math module
import math
# Product of
print(math.prod((2, 4, 6)))
# Raise a number to the power of
print(math.pow(2, 3))
# Rounding numbers
x = 13.9
# Up
print(math.ceil(x))
# Down
print(math.floor(x))

```

As the comment helpfully points out, the first thing we need to do is import the `math`
 module. By default Python includes various useful modules, and you can
also download and make use of external modules too, however their
functionality isn't automatically available in your scripts.

Instead, we need to tell Python we want to include that module's features in our code with the `import math` line.

Now the module is available, we can make use of its many functions. If you check out Python's [math module](https://docs.python.org/3/library/math.html) you'll see many different functions available for assisting with all kinds of maths.

In our example we're first printing out the result of the `math.prod`
 function - this produces a product of a sequence of numbers provided.
Note here that the argument (the data we provide to the function) we
provide is 3 numbers inside parenthesis. This is called a **tuple**
 and we'll cover that in more detail later. For now, just know that it
allows us to provide the three numbers in a format the function can work
 with.

We see the output from this line of code is the value `48` which is the product of those numbers, that is; 2  *4*  8.

The next function we explore is the `math.pow` function; used to raise the first number provided by the power of the second number; 2  *2*  2. The output from this is `8` as expected.

The math module also has a couple of helpful functions for rounding
numbers up and down. As we can see in the example, we have a float `x` of `13.9`, and we print the result of `math.ceil` (to round up, or go to the 'ceiling' of the whole number) along with `math.floor` (to round down, or go to the 'floor' of the whole number). The resulting output would be `14` and `13`.

These are a few simple examples of just a small selection of the
functions available in Python's math module. Solving mathematical
problems is something you're almost certainly going to need to do in
your programming journey, and the math module will be a great tool to
help!

[← Previous: 5.04 - Data types](https://play.cyberstart.com/field-manual/8fc88b98-d7eb-11eb-b851-0242ac140009)
[Next: 5.06 - Lists and tuples →](https://play.cyberstart.com/field-manual/8fca838a-d7eb-11eb-93b2-0242ac140009)
