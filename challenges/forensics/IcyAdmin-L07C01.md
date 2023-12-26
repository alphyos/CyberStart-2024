# 🧊 Icy Admin - L07 C01

Ok agent, first up we need to recover the NTLM hash of the administrator account. We've had one of the research team send you a memory dump to take a look at.

**Tip:** The hash is the flag.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Think about the Volatility filters you may have used previously, as well as other plugins needed for a "hashdump".

</details>

## Files

- [admin - memory dump.zip](https://drive.google.com/file/d/12IbzcbQxRXrb49zfpmOC-RGpZ81OttL5/view?usp=sharing)

<details><summary>

## Step by Step</summary>

- Download the file and extract
- You can figure out the profile by using `volatility -f filename imageinfo` and confirming using `volatility -f filename --profile=(profile) kdbgscan`
- Run `volatility -f filename --profile=Win81U1x64 hashdump > hash.txt`
- The administrator hash is as follows:
  - aad3b435b51404eeaad3b435b51404ee:`fc525c9683e8fe067095ba2ddc971889`:::
- Enter only the indicated hash as the flag
  - `fc525c9683e8fe067095ba2ddc971889`

`flag: fc525c9683e8fe067095ba2ddc971889`

</details>
