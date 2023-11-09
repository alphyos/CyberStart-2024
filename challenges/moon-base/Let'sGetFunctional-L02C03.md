# 💃 Let's Get Functional - L02 C03

You may be thinking by now that programming means typing and retyping lots of things all the time, but actually there's a handy way we can reuse some of the code you're writing so you don't have to do that. They're called functions and they're simply little blocks of code that we can call on again and again to do useful things without writing duplicate code.


```
💡 Hint: Remember, a function doesn't necessarily return something.
```

## Answer

```python
# CHALLENGE 1: Write a function that takes in two integers and
#              multiplies them together then returns the result.
def multiply(a, b):
    return (a * b)

# CHALLENGE 2: Run the function from CHALLENGE 1, passing in the
#              integers 99 and 52 and print the result.
print(multiply(99, 52))

# CHALLENGE 3: Write a function that takes two integers and prints
#              the string "I am X ft Y inches tall", replacing the
#              X and Y with the numbers passed into the function.
def height(feet, inches):
    print("I am %d ft %d inches tall" % (feet, inches))

# CHALLENGE 4: Run the function from CHALLENGE 3, passing in 6 and 2
#              as the parameters.
height(6, 2)
```
