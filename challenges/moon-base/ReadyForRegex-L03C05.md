# 🔎 Ready For Regex - L03 C05

```
💡 Hint:
```

## Answer

```python
# CHALLENGE 1: Write a regex search that extracts all the classes from
#             the divs and saves them into an array.

pattern = "class='(.*)'"
data = re.findall(pattern, html)

# CHALLENGE 2: Write a loop that goes through the array from
#              CHALLENGE 1 and prints the contents.

for x in data:
    print(x)
```
