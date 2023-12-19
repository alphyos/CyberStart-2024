# 🐚 Seashell - L13 C07

We've just made a big discovery Agent 707, it seems the gang have more than one ship! We know because we've intercepted a message sent between them. Trouble is we can't figure out what the message is. Take a look.

**Tip:** Code is just data.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: Run Run Run your boat
```

</details>

<details><summary>

## Step by Step</summary>

- Running the hex text into a hex decoder produces randomness paired with a legible string
  - `shellcode_is_data_data_is_shellcode`
- This indicates that the hex before this decoding is actually just regular C code that needs to be compiled and run

```c
int main() {
    const char shellcode[] = "\xeb\x3e\x58\x89\xc1\xbb\x00\x00\x00\x00\xba\x53\x00\x00\x00\x31\xc0\x8a\x04\x19\x53\x51\x50\x89\xe1\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x52\xba\x01\x00\x00\x00\xcd\x80\x5a\x59\x59\x5b\x43\x43\x4a\x75\xdb\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xbd\xff\xff\xff\x73\x68\x65\x6c\x6c\x63\x6f\x64\x65\x5f\x69\x73\x5f\x64\x61\x74\x61\x5f\x64\x61\x74\x61\x5f\x69\x73\x5f\x73\x68\x65\x6c\x6c\x63\x6f\x64\x65";
    (*(void(*)())shellcode)();
}
```

- `sudo apt install gcc-multilib`
- `gcc -m32 -z execstack -fno-stack-protector test.c`
- `./a.out`

`flag: seloei_aadt_sseloe`

</details>
