## PROGRAMMING

# Conditionals (if statements)

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/82289147-a0b1-4f1b-a47c-44743bcfa60e" width="800" />
</div>

## If this, then that

Conditionals in programming enable us to control the flow of our
programs based on a test. Think of them as branches of code that will
only execute under a certain condition. They're super useful, and you'll
 be using a lot of them as you start to build more complex programs.

In its simplest form, a conditional simply says "if this thing or statement is **true** then I will run the following code":

```python
x = True
if x:
    print('x is true')
```

Note the indentation of the `print` line above - in
programming generally, not just Python, we need to identify what code
'belongs' to the conditional; that is what lines of code will be
executed if the conditional statement 'passes', i.e. is true. In some
languages, such as Javascript or PHP, you'll often see `{` and `}` wrapping the code belonging to the conditional. In Python, we simply indent the related code.

As well as a basic conditional check above, we can use `else` to tell the program "if this thing is true then run some code, otherwise do something **else**":

```python
x = False
if x:
    print('x is true')
else:
    print('x is false')
```

You'll notice the `else` statement is not indented. Anything indented after the `if` will be executed if the statement is `true`,
 but we want to do something if the statement is not true... so we need
to return to the original indentation to leave the original 'if'
statement.

The `else` statement can also be combined with an `if` statement to form an `elif` - **else if**. This tells Python "if the previous condition was not met, check this other condition instead". For example:

```python
x = 1
if x == 1:
    print('x is equal to 1')
elif x == 2:
    print('x is equal to 2')
elif x == 3:
    print('x is equal to 3')
else:
    print('x is not 1, 2 or 3')
```

A few things to note here! First, when we want to check if two things are equal to each other we use `==`. As you know, if we were to use a single equals (`=`)
 we would be trying to set a variable, so instead we use two. This is
common among other languages as well; in fact some even allow `===` as well, for a stricter comparison where it checks not only the values match but also the types match too!

You'll also see we can chain `elif` statements. If one
condition isn't met, check another. If that one isn't met, then check
another, and so on. Once we've checked everything we need, we can have a
 final 'fallback' `else` to run some code if *none* of the conditions were met.

So far we've looked at pretty simple examples of these concepts. Let's take a look at some more complicated ones:

```python
# Example 1
if 'pass' in 'password':
    print('Found!')

# Example 2
x = 15
if x > 10 and x < 20:
    print('x is greater than 10 AND less than 20')
if x > 10 or x < 20:
    print('x is greater than 10 OR less than 20')

# Example 3
arg = 'abc'
if arg:
    print('argument provided')
    if arg == 'abc':
        print('argument abc provided')
    else:
        print('unexpected argument provided')
else:
    print('no argument provided')
```

In example 1 we're checking something slightly different: is one
string found within another. Conditional statements aren't just limited
to simple 'checks', you can do all kinds of things:

* is the first letter of a string the letter Y? `if string[0] == 'Y':`
* is the result of another function what we expect? `if math.floor(1.5) == 1:`
* is something false, rather than true? `if variable is False:`

In example 2 we check multiple conditions in a single `if`
 statement. In theory, you could check as many things as you like;
however that would probably lead to code that is pretty difficult to
understand! Of particular importance here are the `and` and `or` pieces - with `and`, *all* of the conditions must pass for the associated code to run, while with `or` only *one* of the conditions must pass. Make sure you're using the right one!

Example 3 shows how we can nest conditional statements. Initially, we just want to check if the variable `arg`
 exists and has a value. If it does, we can then check the value to run
different code accordingly. Pay close attention to the indentation here -
 try to identify which code will run for each conditional statement;
change the `arg` variable and run the code to see if you were correct!

> You can combine conditionals with other logic such as loops, which we
> will learn next. These are the building blocks of all modern programs
> and very powerful.

<div align="center">

[← Previous: 5.07 - Dictionaries](Dictionaries5.7.md) | [Next: 5.09 - Loops →](Loops5.9.md)
:-|-:
