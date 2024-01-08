## BINARY

# Memory

As your
program executes, it will require memory to store information. It may be
 memory to store the program code that is being executed, or memory to
handle variables provided by the user.

Consider the following program:

```c
#include <stdio.h>
int main( ) {
   int c;
   printf( "Enter some value please :");
   c = getchar( );
   printf( "\nYou provided : ");
   putchar( c );
   return 0;
}
```

In this instance the program needs to store the value you provided
until later in execution. There are a few different areas of memory you
should be aware of and we will list them here:

* **Stack.** This area of memory is used by the computer
to handle execution and is very structured along with the program code.
As you enter functions and exit the stack grows and collapses to provide
 the right supporting data to the program. This is also an area where
data can be written by a program such as the above. This can be
dangerous as critical program execution information is near user input!
* **Heap.** Designed to hold long standing or sizeable
information. If you load a video in your web browser it must buffer the
data somewhere and has no idea if you will stop watching in 12 seconds, 1
 minute or 5 minutes. This area of memory is designed to be efficient at
 dealing with unknowns and is structured for non-finite operations.
* **Registers.** These are directly on the CPU (Central
Processing Unit) and are small, exceptionally fast and finite in number.
 They are mostly used for the calculations that run your computer, and
for very short spaces of time to hold data such as numbers or addresses
to variables. The above code may be optimised to use them if the program
 is simple enough. More likely, they will be used temporarily to
reference where the data is really stored.

Most of the time when we interact with memory, we have neat helper
functions provided by a programming language. However, if a developer
makes a mistake, we can trick the program into executing code it should
not. In this instance we may need to understand these data structures at
 a lower level to succeed.

## Cleaning up

After a program has stored some data in memory, there will likely
come a time where that information is no longer needed. This is known as
 **garbage memory**.

Many programming languages contain a built-in *garbage collector*,
 a feature which will automatically recover unused memory for you. Some
languages, such as C, do not include this feature by default and it is
left to the programmer to clear up as they'd like.

[← Previous: 6.03 - Compiling a binary](https://play.cyberstart.com/field-manual/8fe69958-d7eb-11eb-989f-0242ac140009)
[Next: 6.05 - Buffer overflows →](https://play.cyberstart.com/field-manual/8fe8a90a-d7eb-11eb-9ace-0242ac140009)
