# 🔓 Getting Access - L08 C04

Agent, it looks like the aliens' insider back on earth is someone with a good understanding of technology. The aliens have left him a very complicated backdoor into the ships control system, but we need your expertise to figure it out and break in. If we can do that we think we might be able to set the alien ship to self-destruct!

Write a script which connects to the server controlling the entry to the aliens' tech over TCP at localhost:10000 and send some random data. We've already tried it and it sends back a bunch of random word codes. There's also a file called backdoor.txt containing some random text. Use your script to encrypt a message using that text and the word codes. Each word is represented by: paragraph_number, line_number, word_number. We think sending the encrypted message back is what will unlock the server and give us access to the alien tech!

The server expects all the words in one transmission. The words should be stripped of punctuation and sent over separated by newline characters (\n). You'll need to look at the final server response to find the flag.

**Tip:** Send the encrypted message back to the server and look at the response to get the flag.

> 💡 Hint: Consider using split to break down the book into paragraphs, then into lines and finally into words.
>
> Make sure you remember to send the response all at once, and the words have to be separated with newline characters.
>
> Oh, and you have to strip out punctuation, so you can do that with regular expressions.
>
> Finally, remember to look at the response from the server to find the flag!

## Answer

```python
import socket

def get_word(paragraph_num, line_num, word_num, filename):
  with open(filename, 'r') as f:
    # read the entire file
    contents = f.read()

  # split the contents by paragraph
  paragraphs = contents.split('\n\n')

  # get the specified paragraph
  if paragraph_num <= len(paragraphs):
    paragraph = paragraphs[paragraph_num-1]
  else:
    return None
  
  # split the paragraph by line
  lines = paragraph.split('\n')

  # get the specified line
  if line_num <= len(lines):
    line = lines[line_num-1]
  else:
    return None

  # split the line by word
  words = line.split(' ')

  # get the specified word
  if word_num <= len(words):
    return words[word_num-1]
  else:
    return None


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 10000))
sock.send(b"test")
codes = sock.recv(1024)
codes = codes.decode()
codes_list = codes.split("\n")
no = codes_list.pop()

words = []
for code in codes_list:
  code_split = code.split(",")
  words.append(get_word(int(code_split[0]), int(code_split[1]), int(code_split[2]), "backdoor.txt"))

words_string = '\n'.join(words)

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for element in words_string:
  if element in punc:
    words_string = words_string.replace(element, "")

print(words_string)
sock.send(words_string.encode())
print(sock.recv(1024))
```
