## BINARY

# Compiling a binary

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/8d2e0caf-2f02-45a3-b94e-bc3919906c20" width="800" />
</div>

## Creating and executing a binary file

It's quick and easy to create your own program (aka a "binary file")
on Linux. The first concept to really understand is that the source code
 is the file you write and the binary file is the compiled,
machine-readable file that's ready for your computer to run.

Creating your own programs is a great skill to have as it enables you
 to build your own tools, particularly where another doesn't suit your
needs - plus is especially useful in CTFs, further learning and the
higher levels of CyberStart.

Let's have a look at the `ping` command to see some specifics about it:

```console
$ file /bin/ping
/bin/ping: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7e20c8bbbcf57159cb93bc4cb3bb5a58978fde5a, for GNU/Linux 3.2.0, stripped
```

We can see from the response that it's an ELF (Executable and
Linkable Format) type file. It's built for 64-bit architecture, so you
won't be able to run it on a 32-bit system and it's also dynamically
linked, so it relies on a library file to help it execute fine.

Now let's look at writing, compiling and executing our own file using the very popular C language. Start a new file called `test.c` and save the following into it:

```c
#include <stdio.h>

int main() {
    printf("Hello, world!");
    return 0;
}
```

Here we include the common C library **stdio.h**. It's a header file (hence the **.h** file extension) and it contains functions related to input/output, such as `printf`, `scanf`, `fopen` and more. As we'll be making use of `printf` shortly, we'll need to include the library. Next we start a single function - which is typically named `main` and inside this we use `printf` to output a basic text message. Finally we `return` with status code `0` to indicate no errors as it exits the program.

This will be all the code needed to output that simple message when
ran, but C is a compiled, not interpreted language like say, Python - so
 we'll need to compile it into a binary to make an executable file to
run. There are many compilers available, but a very common one is `gcc` (GNU Compiler Collection). Let's compile our code now:

```console
gcc test.c -o test
```

Here we've compiled our code, passing in our C file as the first argument and then specifying the output file by providing `-o test`.
 It should only take a spilt second to create the compiled file, which
is full of machine code a Linux system can run. You can run `file test` to see, much like the initial example, that it's an ELF type file suitable for 64-bit machines and is dynamically linked.

You may need to add execute permissions to the file (see [Linux permissions](LinuxPermissions4.7.md) if you need help). With your executable file ready to run, simply call `./test`
 to execute it and see your message! Congratulations, you've just
created, compiled and ran your own binary in no time at all. Search
online for more tutorials on the C language and indeed other great
compiled languages such as Rust, Go and even Assembly.

> Be careful of source code you take from online sites. Most is fine
> and time saving, but there's plenty out there that's created to be
> malicious. The computer will just do what it's instructed to do, so it's
> your job to check out source code (or even better - run inside a VM) to
> make sure you're happy to execute it!

<div align="center">

[← Previous: 6.02 - ELF and EXE files](ElfAndExeFiles6.2.md) | [Next: 6.04 - Memory →](Memory6.4.md)
:-|-:
