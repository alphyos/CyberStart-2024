# 📜 Listicle - L07 C05

As part of the final report we're producing for the team, they've asked us to make a list of all the user accounts and passwords that have been used on one of the compromised machines. We have a memory dump from that machine, take a look and see what you can find.

**Tip:** Find the bad account and that will give you the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Mimikatz can be used with Volatility to gain certain important information.

</details>

## Files

- [pc397 mem dump.zip](https://drive.google.com/file/d/1YSusu97GrR733Zrwj3dkzvxBOQSFRCai/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Dowload the file and extract it
- You can figure out the profile by using `volatility -f filename imageinfo`
- To get the mimikatz plugin for volatility (version 2.6.1), copy the text from [https://raw.githubusercontent.com/dfirfpi/hotoloti/master/volatility/mimikatz.py](https://raw.githubusercontent.com/dfirfpi/hotoloti/master/volatility/mimikatz.py)
- Paste it in your editor and save it as `mimikatz.py`
- Move it into the `/plugins` directory of your volatility install
- For the VM provided by cyberstart this may be `/opt/volatility/volatility/plugins/`
- To move the file run `sudo mv mimikatz.py /path/to/volatility/plugins/`
- Now executing `volatility -f filename --profile=Win7SP0x64 mimikatz` should get you the passord
- In case of import errors, make sure to install `construct, pycrypto and pycryptodome` via pip

![image of mimikatz result](/assets/listicle1.jpg)

`flag: M1m1Katz_0wn1ng`

</details>
