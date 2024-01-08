## PROGRAMMING

# Loops

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/b22e6e85-922b-4de2-b47b-e2029ce5a64c" width="800" />
</div>

## Controlled repetition

Loops enable programs to step through a repetitive task - for
example; iterating over numbers 1 to 100, perhaps items in a list or
characters in a string, maybe even a set of files in a directory! Loops
in Python such as the `for` loop, or the `while` loop, are key to enabling your program to solve problems. You could for example build a `for` loop that tests 10000 password combinations one after the other; much easier than having to do it one by one yourself!

Care and consideration also need to be taken when working with loops
to ensure we only run things the intended number of times. Bugs or
otherwise badly written code involving loops could result in infinitely
repeating code, excessive memory use or other flaws and issues that
break computer programs.

To start, let's look at a simple loop example:

```py
colours = ["blue", "red", "orange", "cyan"]

for x in colours:
    print(x)
```

If we run this code you'll see each of the items in our list printed out one after another. We've looped through the list!

More specifically, we're saying `for` each item in the `colours` list, temporarily assign the item to the variable `x`.
 By indenting code we can then specify what we want to do during a
single iteration of the loop, using the state of the variable `x` at that time.

It's possible to loop through other data items as well, for example characters in a string:

```py
for y in "password1234":
    print(y == "w")
```

```console
$ python3 test.py
False
False
False
False
True
False
...
```

Here Python splits the string into the individual characters, assigning each to the variable `y`,
 and then we can do something with that character during each iteration
of the loop - in this case checking if it equals the letter w and
printing the resulting `True` or `False` boolean output.

If, for whatever reason, you didn't want to iterate through the
entire loop - perhaps you're searching for something specific - it's
possible to `break` out of the loop:

```py
for y in "password1234":
    print(y)
    if y == "w":
        break

print('finished')
```

```console
$ python3 test.py
p
a
s
s
w
finished
```

As you can see, we started looping through the characters in the string and printing each out. However, when `y` was equal to `w` we used `break` to exit the loop early.

Similarly, it's also possible to `continue` to the next iteration early, if needed:

```py
for x in ["blue", "red", "orange", "cyan"]:
    if x != "orange":
        continue
    print("I found the " + x)
```

```console
$ python3 test.py
I found the orange
```

Here for each iteration in the loop, we check if the item assigned to `x` is *not* equal to `orange`. As `blue` is not equal to `orange`, we `continue` on to the next iteration in the loop, next considering `red`; which has the same outcome and so we again continue, now onto `orange`. This however *does* equal `orange`, so we don't get into the code block under the condition to `continue` and instead we reach the `print` statement. It'll finally run the loop for `cyan` and that too will continue. Finally we've ran through all colour values and the loop has ended.

Along with the `for` loop, which will iterate over something, we also have the `while` loop which will continue as long as the condition is true:

```py
i = 1
while i <= 25:
    print(i)
    i += 1
else:
    print("I am now done")
```

If we run the above code we would see numbers 1-25 printed out. This is because initially we tell Python the variable `i` is equal to 1, next we start a loop that is going to continue as long as `i` is less than or equal to 25, then we print the current value of `i` and finally we increase the value of `i` by one. Note that we do that with a shortened version of `i = i + 1`.

Eventually, `i` will no longer be less than or equal to 25; this means the `while`
 condition is no longer met and the loop finishes. Here is where you
need to be particularly careful because if the while condition is *always* met your code will continue to run indefinitely! Or at least, until you realise something is wrong and forcefully stop it.

It's also possible to add an `else` condition to a `for` or a `while` loop. The code here will execute when the loop has finished. Note that if you `break` a loop early, Python doesn't consider it as having 'finished' (rather it was stopped early) and so the `else` code will not run.

In this section demonstrated a few basic uses of loops, but they will
 turn up again and again especially in more advanced programming. This
is exactly how you can build password crackers, web application testing
tools, or even problem solvers in your tools.

<div align="center">

[← Previous: 5.08 - Conditionals (if statements)](Conditionals(ifStatements)5.8.md) | [Next: 5.10 - Functions →](Functions5.10.md)
:-|-:
