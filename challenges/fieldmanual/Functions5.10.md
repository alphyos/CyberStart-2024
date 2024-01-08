## PROGRAMMING

# Functions

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/06bcd286-8353-4c10-b0cd-d02c8a3e0e71" width="800" />
</div>

## Reusable code

A function in programming is a block of code which is only executed
when the function is 'called'; that is we specifically request the code
to run. You can provide data to the function, known as **arguments**, which may change the behaviour of the code within. Functions can also return data as well.

They're a means of *compartmentalising* a specific piece of
functionality in your program so that you can use it many times, rather
than duplicating the same lines of code often, perhaps in many places.
If your program needs to do the same thing in 10 difference places, why
write the same thing 10 times? A single function is much easier to
maintain and update, code is much more readable, and its likely to be
more efficient as well. In programming this is known as **DRY** - "Don't Repeat Yourself".

Let's dive into an example:

```py
def hello_world():
    print("Hello world!")
```

Here we're **def**ining a new function - `hello_world`.
 After the name we see the opening and closing parenthesis: here is
where we would specify arguments that could be provided, but for now
we'll leave it empty. Much like conditionals and loops, we finish the
line with a `:`. Within the function, indented, we print some text.

If we were to run this code as-is, nothing would happen. As mentioned, a function is only executed when we request it, or *call* it. So let's add some lines to call the function, and then run the code:

```py
def hello_world():
    print("Hello world!")

hello_world()
print('test')
hello_world()
```

```console
$ python3 test.py
Hello world!
test
Hello world!
```

We can call the function by referencing its name, followed by the
parenthesis. Here we can see the function's re-usability; we called it
twice while the function only needed to be defined once!

As noted earlier, it's possible to provide arguments to a function
and make use of them within, as well as returning data from a function:

```py
def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 5))
print(multiply(10, 6))
print(multiply(1234, 5678))
```

```console
$ python3 test.py
25
60
7006652
```

When defining the function here, inside the parenthesis we state that arguments `num1` and `num2`
 will be provided. These become variables within the function that we
can then make use of, in this case multiplying them. We also `return`
 the result back to where the function is being called from. If we
wanted to, we could store the result in a variable, however here we just
 print the returned values.

Typically, functions aren't likely to contain just a single line of code, but rather some more complex logic:

```py
def filter_list_by_letter(mylist, letter):
    newlist = []
    for item in mylist:
        if item[0] == letter:
            newlist.append(item)

    return newlist

names = ["Alex", "Charlotte", "John", "Jane", "Sam"]
filtered = filter_list_by_letter(names, 'J')
print(filtered)
```

```console
$ python3 test.py
['John', 'Jane']
```

While you could potentially create a fully-featured, complex program
without writing any of your own functions; it would likely be a bloated,
 difficult to maintain mess of code! Functions are integral to clean,
re-usable and easy to maintain programs and should definitely be
something you use a lot!

<div align="center">

[← Previous: 5.09 - Loops](Loops5.9.md) | [Next: 5.11 - Modules →](Modules5.11.md)
:-|-:
