# 🎊 Hooray For Arrays - L02 C04

If you thought functions were useful just wait until you learn about arrays! They're simple things, just collections of data, but they're really handy for programming. In this lesson you'll learn how to create them, plus add and remove items in them, and more.

```
💡 Hint: Remember that we start counting arrays from 0.

So the fourth value in an array will be array[3]

0, 1, 2, 3. That's four values but the highest number is 3
```

## Answer

```python
# CHALLENGE 1: Create an array with the following values in it in
#             order:
#             42, 1337, "Coffee", "Anonymous" then print the array.
anArray = [42, 1337, "Coffee", "Anonymous"]
print(anArray)

# CHALLENGE 2: Add two more values to the end of the array you created
#              in CHALLENGE 1: "Blue", "Sky" then print the array.
anArray.append("Blue")
anArray.append("Sky")
print(anArray)

# CHALLENGE 3: Print the fourth value in the array you created in
#              CHALLENGE 1.
print(anArray[3])

# CHALLENGE 4: Create a dict that includes the following values in
#              order: "Subject": "Hacking", "Grade": "A".
aDict = {"Subject": "Hacking", "Grade": "A"}

# CHALLENGE 5: Print the grade value in the dictionary you created in
#              CHALLENGE 4.
print(aDict["Grade"])
```
