## BINARY

# Buffer overflows

The basic idea of a buffer overflow is... to overflow a buffer. Ha! At the concept level imagine the following:

You have a program where the user is allowed to input data. Right
next to that area of memory reserved for their input is a very special
value that is used to control the code executed on the computer. The
user should **never** be able to modify this special value.
 If the program in question does a really poor job of preventing the
user submitting too much data, they can enter enough that it 'overflows'
 in to the next thing in memory - the special value! This means someone
could replace that special value with whatever they wanted.

> In most cases the result of a buffer overflow is just a program
> crash. You corrupt memory and the program breaks. However, if you can
> overwrite it with a very carefully selected value you may be able to
> hi-jack other users' data, bypass authentication or even trigger an RCE
> (remote code execution) where you can take over a system remotely! This
> is tricky but cyber criminals pull it off frequently.

Take a look at this utterly horrible program for an example. There are comments denoted by lines that start with '//'

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prepare a buffer of 16 bytes to store the user password
    char user_input[16];
    // Set authenticated to a default of 0 so no one has rights unless they use the password.
    int authenticated = 0;

    printf("Password please> ");
    gets(user_input);

    // Check if the password matches. If it doesn't reject them.
    if(strcmp(user_input, "Secur3Pa44!"))
    {
        printf ("\nDENIED.\n");
    }
    else
    {
        // If the password matches then set authenticated to 1 as they passed the test.
        printf ("\nGranted!\n");
        authenticated = 1;
    }
    // If authenticated does not = 0 then it exists, and therefore the user must have provided the password.
    if(authenticated)
    {
        printf ("\nYou get all the toys. We will now execute the super secret codes.\n");
    }
    return 0;
}
```

This code is far from beautiful but it really illustrates a point.
When this is allocated memory the program will do something like this:

```c
[16 bytes for user_input][some compiler stuff][authenticated]
```

The problem with this program is it uses the `gets()`
function which is notorious for not checking the size of user input. We
can supply way more than 16 bytes! This is the section where the
vulnerability is most exposed.

```c
    printf("Password please> ");
    gets(user_input);
```

However, it is also the case that the design of the `if(authenticated)` could be far more explicit than just requiring it to have any non zero value.

Let us build this program and disable the security checks. We have
saved the above code in to a file here called bad.c (you could do the
same if you want to try!).

```console
$ gcc -fno-stack-protector -o bad bad.c
chmod +x bad
```

We can now run this program and interact with it. Note if you provide
 the right or wrong password you get the expected responses. Now let us
flood it with bad data to see if we can trick it in to overwriting
authenticated even when we do not have the password.

```console
$ python -c 'print "A"\*30' | ./bad
```

This will put 30 A characters in to the binary input. If this does
not work try 40. Depending on how the compiler built it, at some number
greater than 16 but likely less than 60 we will overwrite the
authenticated value and execute the code like we provided the right
password!

This is a basic buffer overflow. In some attacks we need to more
carefully overwrite specific values, which means learning what the
computer expects and then carefully crafting an attack.

> Most modern day bugs come down to logic, size or type handling
> failures that trick a program in to doing something it should not!

<div align="center">

[← Previous: 6.04 - Memory](Memory6.4.md) | [Next: 6.06 - Taking it further →](TakingItFurther6.6.md)
:-|-:
