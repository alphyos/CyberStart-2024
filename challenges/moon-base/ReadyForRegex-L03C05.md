# 🔎 Ready For Regex - L03 C05

So, it looks like this might be your last lesson Agent 707, the team on the next level have called an emergency meeting. Rumours are that we've been contacted by aliens and all agents need to get ready for whatever happens next! Just time to teach you about regular expressions, a very handy way to search text for a pattern.

> 💡 Hint: RegEx is a whole language and is often seen as hard to read. Think about which part you want to extract, and what pattern both the class= attribute values have.

## Answer

```python
# CHALLENGE 1: Write a regex search that extracts all the classes from
#     the divs and saves them into an array.

pattern = "class='(.*)'"
data = re.findall(pattern, html)

# CHALLENGE 2: Write a loop that goes through the array from
#      CHALLENGE 1 and prints the contents.

for x in data:
  print(x)
```
