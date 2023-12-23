# 🪶 Rattlesnake - L05 C08

Well, one thing is for sure, the Yakoottees' scripting language of choice is Python. We've intercepted a lot of Python files from all over the place. So many, in fact, that we need someone to look at them and see what they do. Can have a look at this one to find out what it does?

**Tip:** The flag is in the file.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Did you run the python file without knowing what it does? Oops. Maybe just take a look at the source code first.

</details>

<details><summary>

## Step by Step</summary>

- Open the python file with any text editor
  - ex. VS Code, Notepad++, etc.

```python
from sys import argv

# THE FLAG IS: [REDACTED]
print("Deleting " + argv[0])
remove(argv[0])
```

- The flag is in the 4th line of the program, commented out

</details>
