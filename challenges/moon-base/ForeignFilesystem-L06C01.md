# 🌏 Foreign Filesystem - L06 C01

We're trying to make sense of a filesystem with a large number of empty directories that the aliens created. Can you write a script to browse the contents of /tmp/aliendir and see if you can actually find anything.

**Tip:** The name of a file you find is the flag.

> 💡 Hint: Consider using the os module's walk function for this one.  Remember, the name of the file is the flag!

## Answer

```python
import os
path = "/tmp/aliendir"
paths = "/tmp/aliendir/folder-"
i = 0

for x in os.listdir(path):
  i = i + 1
  path = paths + str(i)
  y = os.listdir(path)
  if y != []:
    print(x)
    print(y)
```
