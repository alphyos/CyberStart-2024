# 🏋️‍♀️ Brute Strength - L06 C12

Great news, recruit. Thanks to your work we've been able to recover a zip file from the Yakoottees' private server. We're looking for blueprints of the Superspin HQ and details of how they plan to get in. Hopefully, the zip contents will lead us to that.

The zip file is password protected, so we set one of our engineers on writing a script to brute force it. Unfortunately, he was called away onto a special project for a team on another level. Perhaps you could make the final few alterations to his script to get it working.

**Tip:** Change the script and open up the zip file to get the flag. Oh, and don't forget you can use your local terminal to help.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: We believe the password starts with 'Super' and ends in three characters (which could be mixed case). Try modifying the script with that in mind.

</details>

## Files

- [planz.zip](/assets/brutestrength2.zip)
- [zipcrack.py](/assets/brutestrength3.py)

<details><summary>

## Step by Step</summary>

- Download both files and examine the python script using a text editor such as Visual Studio Code
- Add all 26 letter of the alphabet to the alphabet variable but capitalized

```python
import zipfile
import itertools
import time

# Function for extracting zip files to test if the password works!
def extractFile(zip_file, password):
  try:
    zip_file.extractall(pwd=password.encode())
    return True
  except KeyboardInterrupt:
    exit(0)
  except Exception as e:
    pass

# Main code starts here...
# The file name of the zip file.
zipfilename = 'planz.zip'
# The first part of the password. We know this for sure!
first_half_password = 'Super'
# We don't know what characters they add afterwards...
# This is case sensitive!
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
zip_file = zipfile.ZipFile(zipfilename)

# We know they always have 3 characters after Super...
# For every possible combination of 3 letters from alphabet...
for c in itertools.product(alphabet, repeat=3):
  # Add the three letters to the first half of the password.
  password = first_half_password+''.join(c)
  # Try to extract the file.
  print("Trying: %s" % password)
  # If the file was extracted, you found the right password.
  if extractFile(zip_file, password):
    print('*' * 20)
    print('Password found: %s' % password)
    print('Files extracted...')
    exit(0)

# If no password was found by the end, let us know!
print('Password not found.')
```

- Run the new code and make sure the zipfilename variable is actually what the zip file is named

![running the new code](/assets/brutestrength1.png)

- A text file should appear on your machine, the flag is inside

</details>
