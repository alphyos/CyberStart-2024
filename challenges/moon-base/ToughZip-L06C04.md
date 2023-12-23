# 🦹‍♂️ Tough Zip - L06 C04

So, remember those zip files from the previous level? Well, they're still sending them, thousands in fact, and it looks like they've improved the password protection too.

See if you can write a script to brute force one of the zip files, alien-sample-42.zip and read the extracted file alien-sample-42.txt.

We will provide a list of potential passwords.

Tip: Extract the file to the /tmp directory to get the flag.

**Tip:** Extract the file to the /tmp directory to get the flag.

> 💡 Hint: Trying all the items in an array sounds like a job for a for loop!

## Answer

```python
#
# Zip file found at /tmp/alien-sample-42.zip is password protected
# We have worked out they are using one of the passwords
# in the provided list
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout. If this occurs try narrowing
# down your search
#
from zipfile import ZipFile

possiblePasswordList = [
  'pant', 'papa', 'paps', 'para', 'path', 'pats', 'paty',
  'pard', 'pare', 'park', 'parr', 'pars', 'part', 'pase',
  'pash', 'past', 'pate', 'peal', 'pean', 'pear', 'peas',
  'pave', 'pawl', 'pawn', 'paws', 'pays', 'peag', 'peak',
  'peck', 'pele', 'peat', 'pech', 'peke', 'perm', 'perp',
  'pecs', 'peds', 'peed', 'peek', 'peel', 'peen', 'peep',
  'pelf', 'pelt', 'pend', 'pens', 'pent', 'pass', 'pepo',
  'pert', 'phon', 'phot', 'phut', 'peer', 'pegs', 'pehs',
  'pere', 'peri', 'perk', 'phat', 'phew', 'phis', 'phiz',
  'perv', 'peso', 'pest', 'pets', 'pews', 'pfft', 'pfui',
  'pial', 'pian', 'pias', 'pica', 'pice', 'pick', 'pics',
  'pied', 'pier', 'pies', 'pigs', 'plan', 'plat', 'ploy',
  'pika', 'pike', 'piki', 'pint', 'piny', 'pion', 'pith',
  'pile', 'pili', 'pill', 'pily', 'pima', 'pimp', 'pina',
  'pine', 'ping', 'pink', 'pins', 'plug', 'plum', 'pein',
  'poll', 'peps', 'pits', 'pity', 'pixy', 'plop', 'plot',
  'pipe', 'pips', 'pipy', 'pirn', 'pish', 'piso', 'pita',
  'pole', 'plow', 'plod', 'pois', 'poke', 'poky',
  'play', 'plea', 'pleb', 'pled', 'plew', 'plex', 'plie',
  'plus', 'pock', 'poco', 'pods', 'poem', 'poet', 'pogy',
]

with ZipFile('/tmp/alien-sample-42.zip') as zf:
  for password in possiblePasswordList:
  try:
  zf.extractall(pwd=bytes(password,'utf-8'), path='/tmp')
  print(f"password found: {password}")
  break
  except:
  print("wrong password")
```
