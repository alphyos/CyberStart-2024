# ➿ Going Loopy - L02 C05

Hello agent 707. I've just received a message from another agent letting me know something strange is going on - we may have intercepted an alien signal! It's time to accelerate your training and make sure you're ready for your role as an agent on the Moon Base. And what better way to do that than introduce you to loops!

```
💡 Hint: We can create an empty array with square brackets: myArray = []. As covered in the previous challenge, we can append new items to this array with myArray.append(item).

It's also possible to have Python increment by two for you using the 'range' function's third argument: for x in range(0, 50, 2):. This will increment from 0 to 50, increasing by two each time.

```

## Answer

```python
# CHALLENGE 1: Create an empty array called numbers.
numbers = []

# CHALLENGE 2: Write a while loop that will add 100 numbers to the
#              array, starting from the number 100 and incrementing by
#              2 each time. For example, start from 100, then the next
#              number added will be 102, then 104 and so on.
count = 0
number = 100
while count < 100:
    numbers.append(number)
    count = count + 1
    number = number + 2

# CHALLENGE 3: Write a for loop that will look through your numbers
#              array and print out each value in the array.
for x in numbers:
    print(x)
```
