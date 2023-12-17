# 🥤 All Zipped Up - L07 C10

Agent 707, we need your scripting skills again. One of our field agents has managed to turn one of the Chiquitoos' to act as an informant. He has obtained access to a zip file from one of the senior gang members but it's password protected and he doesn't know the password (although we're pretty sure it starts with "Cola"). We've got a Python script that might help us brute force it but we think it needs some modifications.

**Tip:** Open the zip file to get the flag. And don't forget you can use your local terminal to help.

```txt
💡 Hint: We believe the password starts with "Cola" and ends in numbers and upper or lower case characters.
```

## Step by Step

- Download the zip file and python script
- Edit the script to run like the one below, changing the zipfile name to fit your zip name

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
zipfilename = 'l07c10.zip'
# The first part of the password.
first_half_password = 'Cola'
# We don't know what characters they add afterwards...
# This is case sensitive!
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
zip_file = zipfile.ZipFile(zipfilename)

# We know they always have 3 characters after the first half of the password
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

- Run the program int the terminal, in the same directory as the zip file
![running the python code](/assets/allzippedup1.png)
- The flag is in the newly extracted file
