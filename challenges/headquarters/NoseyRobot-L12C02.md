# 🤖 Nosey Robot - L12 C02

Agent 707, thanks to your efforts in finding the gang member leading the effort to send a robot to the bank, we've managed to recover some C code we think might be used by the robot to take photos, but we can't be sure because running it currently returns a segmentation fault. Another agent has rigged up the code to a camera interface. See if you can fix the code, get it to run and take a photo.

**Tip:** Take the photo, the robots confirmation message will show the flag.

<details><summary>

## Need a hint?</summary>

```txt
💡 Hint: This program suffers from a buffer overflow vulnerability.
   You should know by now what causes a buffer overflow so you'll have to fix it.
```

</details>

<details><summary>

## Step by Step</summary>

```c
#include <stdio.h>
#include <string.h>
int main()
{
  int take_photo = 0;
  char command[8];
  char * pictures = "take_pictures";

  strcpy(command, pictures);
  if (strcmp(command, "take_pictures") == 0) {
    printf("%s\n", "CLICK_PHOTO_TAKEN");
    take_photo = 1;
  } else {
    printf("%s\n", "SEG_FAULT_NO_PHOTO");
  }
  return 0;
}
```

- The string “command” is too small for the string you are trying to copy to it. By changing “`char command[8]`” to “`char command[32]`”, buffer overflow will not occur.

`flag: GOxVYN1Ckz7h3j32R53k`

</details>
