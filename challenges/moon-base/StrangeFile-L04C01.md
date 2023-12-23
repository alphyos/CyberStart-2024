# 📖 Strange File - L04 C01

Ok, quick task for you Agent 707 - we've received a strange file from the first alien communication. It's at /tmp/alien-signal.txt, we need you to open and read the file.

Tip: Write a Python script to open and read the file to get the flag.

> 💡 Hint: If you need to remind yourself how to read file contents, it may be a good idea to review what you did on Level 3 Challenge 1.

## Answer

```python
with open("/tmp/alien-signal.txt") as f:
 print(f.readline())
```
