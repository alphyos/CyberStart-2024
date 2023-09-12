# 📏 Agent Profiles - L04 C02

```
💡 Hint:
```

## Answer

```python
import os.path

count = 1
string = ""

for i in range(20):
	fname = "/tmp/agent-" + str(count)+".txt"
	if os.path.isfile(fname):
		with open(fname, 'r') as content_file:
			content = content_file.read()
			string = string + (content.rstrip())
			count += 1
      
print(string)
```
