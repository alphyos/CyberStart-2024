# 📏 Agent Profiles - L04 C02

The operations team have asked that we start preparing a group of agents that could be sent on a mission to intercept the alien craft. We need to review the profiles of our agents, but the script we wrote to get them seems to be broken. Can you fix it?

Tip: The files live in the /tmp directory and have names such as agent-1.txt, agent-2.txt and so on.

> 💡 Hint: In Python, the key is proper indentation.
>
> Remember after a colon ':' the code after belongs to that statement, so it has to be properly indented to show it belongs.
>
> You can have multiple indentations if there are code blocks within blocks.

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
