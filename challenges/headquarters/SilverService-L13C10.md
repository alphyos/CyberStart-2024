# 👨‍🍳 Silver Service - L13 C10

Good news agent, we've found a TCP service used by the gang, it's services.cyberprotection.agency on port 13222. Take a look and see what you can find.

**Tip:** Decrypt all the things! Are you sure the first line is fully decrypted?

<details><summary>

## Need a hint?</summary>

> 💡 Hint: Use Cyberchef, the very first line can only be decoded with a certain Rot13 (Lowercase Only)

</details>

<details><summary>

## Step by Step</summary>

- Run `nc services.cyberprotection.agency 1322`
- Here is an example of the response

Pzmxizm bw jm kwvncaml! <- Caesar cipher  rot18
(^_^)?
0n65 0n69 0n83 <- decimal ascii = AES
3840 / (22 - 7)  <-  =  256
0j43 0j42 0j43  <- hex = cbc
xrl = [key value here no need to change] <- = key  
vi = [iv value here no need to change]  <- = iv 
[encrypted message]  <- last line
```

- Put the last line of the response into Cyberchef with the below steps

![cyberchef recipe](/assets/silverservice1.png)

`flag: cdjtDhivVF`

</details>
