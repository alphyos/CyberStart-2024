## PROGRAMMING

# Modules

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/7c7bef94-b69c-478f-a2ed-ce9f755410fc" width="800" />
</div>

## No need to reinvent the wheel

Modules are a way to build functionality to provide to other
programs. For example, if you're working on a larger program - perhaps a
 cool cyber security tool - and as part of it you need to be able to
scan external networks. You might create a module which contains that
specific functionality so that various parts of your program, or even
other programs, can make use of it.

Python modules also already exist in large numbers. There are some
which are included with Python when you install it, along with many
available on the web and via Python's package installer `pip`. As we have seen with the `math`
 module, these can provide lots of additional functionality and save you
 from needing to write your own code to accomplish the same thing.

To start with we'll look at an example using a built-in module:

```py
import sys

n = len(sys.argv)
print("You provided the following arguments:")

for i in range(1, n):
    print(sys.argv[i])
```

We're making use of the `sys` module in our code and so
import the module needed on the first line. This module provides access
to a bunch of things related to the Python 'system' - perhaps we need
the version so we can run slightly different code depending on the
version of Python the user is running.

However, in our case we're going to make use of the `argv`
 variable. This is a list of the command line arguments passed to Python
 when we are running the script. To begin with we calculate the **len**gth of the list, which we can then use to iterate through it.

We create a `for` loop, setting the variable `i` to a `range` of values from `1` to `n` (the length of the `sys.argv` list). If you remember from previous sections, lists are zero indexed - they start at 0. Well, the value at index 0 in `sys.argv` is the name of the script file we're running. We don't care about that here, so we'll start our `range` at `1`, skipping index `0`! Finally, we're printing out the list items at index `i`, each time we iterate through the loop.

If we just run this normally, we don't actually see anything:

```console
$ python3 test.py
You provided the following arguments:
```

As mentioned, we skipped `sys.argv[0]` as it's the script name and we didn't provide any additional arguments it never got into that loop. Let's try again:

```console
$ python3 test.py 127.0.0.1 username password
You provided the following arguments:
127.0.0.1
username
password
```

That's better! As you can see, when we invoked the script we provided three additional arguments. Our code, using the `sys`
 module, was able to read those arguments and display them. If we needed
 to, we could then use these arguments to dynamically connect to the
provided address, or perhaps execute different code depending on the
values provided.

But what if we want to create our own module? Let's add some code to a new file - `hello.py`:

```py
def say_hi(name):
    print("Hello! How are you " + name + "?")
```

This is of course a super simple example, but it could be any number
of functions and code that we wanted to re-use across one or more of our
 programs.

Next we can create a `test.py` file in the same directory as our `hello.py` file:

```py
import hello
hello.say_hi('Jane')
```

And if we run the `test.py` file from within the directory:

```console
$ python3 test.py
Hello! How are you Jane?
```

Nice! We have successfully imported our own module and called a function from within.

> This is a great practice to be able to build better scaling
> applications and re-use functionality over time. Where you find yourself
> needing the same piece of code across different projects, consider
> creating a module to store that functionality and make it easily
> available. This will take your use of reusable code to new higher
> levels.

[← Previous: 5.10 - Functions](https://play.cyberstart.com/field-manual/8fce691e-d7eb-11eb-94cc-0242ac140009)
[Next: 5.12 - Reading and writing files →](https://play.cyberstart.com/field-manual/8fd149ea-d7eb-11eb-99c7-0242ac140009)
