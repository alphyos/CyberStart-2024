# 👽 Alien Zip - L05 C03

Wow, things are getting crazy, the aliens have flooded us with cryptic zip files. We've no idea what's inside them or, for that matter, how and why they seem to be using human technology in their communications with us.

Anyway, we've started organising the files to try and make sense of them, but they're all locked with a numerical three-digit passcode. See if you can write a script to get into the example file alien-zip-2092.zip and read the text file inside. We think the text file has the same name as the zip (so in this case alien-zip-2092.txt).

Oh, by the way, files need to be extracted to the /tmp directory.

**Tip:** Make sure to break out of the loop when you hit the correct password, otherwise you may override the correct file with a blank one with the same name.

> 💡 Hint: Use the zipfile module on this one.  Remember we're looking for the correct file to be extracted to the /tmp directory.  It's really important to break out of the loop when you hit the right password too!

## Answer

```python
#
# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search

import zipfile
import itertools
import time

def extractFile(zfile, password):
  try:
    zfile.extractall("/tmp", pwd=password)
    return True
  except:
    return False

zipfile = zipfile.ZipFile("/tmp/alien-zip-2092.zip")
digits = "0123456789"

for c in itertools.product(digits, repeat=3):
  s = ''.join(str(x) for x in c)
  print("Trying: " + str(s))
  
  if extractFile(zipfile, str.encode(s)):
    print("Code found!: " + str(s))
    break

txtfile = open("/tmp/alien-zip-2092.txt", "r")
contents = txtfile.read()
print(contents)
txtfile.close()
```
