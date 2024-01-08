## PROGRAMMING

# Running python programs

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/a36a4ea7-5323-4ba8-9d2b-9383fcde54d2" width="800" />
</div>

## A user friendly but powerful programming language

Whether you're creating your own or using a pre-built tool, at some
point you're likely going to want to run a Python program. We're going
to take a look at how to do that, along with creating a quick example
Python script.

If you're using a Mac or Linux system, it's possible you'll already
have a version of Python installed. If for whatever reason you don't,
you'll need to investigate how to install it on your machine - that's
unfortunately outside the scope of this Field Manual, but there's plenty
 of resources available online to help with this!

To start with, let's create a file - test.py. Note that this example
is for a Linux environment! Inside here we can begin with an environment
 declaration:

```py
#!/usr/bin/python3
```

Simply put, this is just telling the machine "when you run this file, please interpret it using "*[abc]*" - in this case, `python3` found in `/usr/bin`. You may notice this is similar to bash scripting where you may have `#!/usr/bin/bash` or `#!/user/bin/sh` !

Next, we'll add a simple line of Python:

```py
#!/usr/bin/python3
print("Hey how goes?")
```

Back on the command line, you may need to add execute permissions before you can run it:

```console
$ chmod +x test.py
```

Now we can run our program!

```console
$ ./test.py
Hey how goes?
```

Excellent! We've just made a Python program we can run from our present directory.

If this was a tool or script we wanted to run regularly and needed easy access to, we could move this script to a `PATH` directory. First lets change the name:

```console
$ mv test.py GreetingProg
$ ./GreetingProg
Hey how goes?
```

Next lets take a look at the directories currently included in our `PATH`:

```console
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin
```

`/usr/local/bin` looks like a good place to put our script. We'll move it there! Note that you might need to use `sudo` for appropriate permissions:

```console
$ sudo mv GreetingProg /usr/local/bin
```

Now that the program is in a `PATH` directory, you can access it from anywhere in your terminal! For example, if you start typing `Greet`
 and hit the 'TAB' key, it will autocomplete for you. You can hit enter
and run the program as before, and also confirm it's new location:

```console
$ GreetingProg
Hey how goes?
$ which GreetingProg
/usr/local/bin/GreetingProg
```

Hopefully this shows how easy it is to create your own script that
can be run from the command line and how to place it within the path, so
 it can be ran from anywhere. Next up - let's look at some common
programming aspects, starting with variables.

<div align="center">

[← Previous: 5.01 - Introduction to programming](IntroductionToProgramming5.1.md) | [Next: 5.03 - Variables →](Variables5.3.md)
:-|-:
