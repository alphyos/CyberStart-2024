# 🗃️ Fun With Files - L03 C01

Did you know you can use programming to work with files? It's actually a very common task when doing programming and something you really need to know well. So let's get learning!

> 💡 Hint: Consider using range() in your for loop. Refer back to Level 2 Challenge 5 if you can't remember how.

## Answer

```python
# CHALLENGE 1: Write a for loop that will create a file called
#      /tmp/cars.txt. There should be 50 lines of text in the
#      file. The first line should be "There are 0 cars"
#      and 1 car should be added every line. Until
#      the last line which should read "There are 49 cars"
with open("/tmp/cars.txt", "a") as myfile:
  for x in range(0, 50):
    myfile.write("There are " + str(x) + " cars\n")

# CHALLENGE 2: Open the file at /tmp/cars.txt and read the contents.
#      Print the contents to the screen.
with open("/tmp/cars.txt", "r") as myfile:
  print(myfile.read())
```
