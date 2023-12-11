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
alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
