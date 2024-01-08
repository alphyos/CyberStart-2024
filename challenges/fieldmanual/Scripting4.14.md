## LINUX

# Scripting

<div align="center">
  <video src="https://github.com/alphyos/CyberStart-2023/assets/108233076/a5c65148-3cee-4d9b-997a-081c8b354921" width="800" />
</div>

## Automating tasks

Finally, let's take a look at some scripting on Linux! This provides a
 pretty rich set of capabilities, and as you learn more about [Programming](https://play.cyberstart.com/field-manual/8fc594ba-d7eb-11eb-b20b-0242ac140009),
 writing better scripts quickly will also become a lot easier. It's
beyond the scope of this field manual to teach you about scripting
overall; there's lots of different types and already many useful
resources you can refer to online for your chosen tool and/or language.

A big challenge, however, is often knowing how to get started and why
 you should really care about writing your own scripts. We'll try to
explain that here.

For our example, let's assume that we know there is a server leaking
secret information on a particular port. Unfortunately, we don't know
the specific port number.

In theory, we could try manually connecting to each individual port. However, this would be quite tedious and time consuming.

With some simple scripting, we can build a basic port scanner to
connect to a series of ports one after another, to determine if there is
 any valuable data at each port. Let's create a file called `scan.sh` and write some code:

```bash
#!/bin/bash
for i in {1..100}
do
    echo "Connecting to $i"
    nc 127.0.0.1 $i
done
```

The first line here just tells Linux what tool this script is intended to work with, in this case `/bin/bash`.

The next line states we need to loop through numbers 1 to 100, each time setting the number to the variable `i`. Next, we say for each of those iterations we want to print out some debug info, and use [netcat](https://play.cyberstart.com/field-manual/8fc23310-d7eb-11eb-8b90-0242ac140009) to connect to `127.0.0.1` with the port number provided as the variable `i`.

So, the first attempt would be `nc 127.0.0.1 1`, then `nc 127.0.0.1 2` and so on.

You may need to set executable permissions on this with `chmod +x scan.sh` so we can allow the file to be executed. If we now run this script, we can see that one of the attempts was successful:

```console
$ ./scan.sh
Connecting to 1
Connecting to 2
Connecting to 3
...
Connecting to 55
Connecting to 56
Connecting to 57
This is a secret
```

This is, of course, a super simple example. In fact, there are many
port scanners readily available and you likely wouldn't need to create
your own for something like this - unless you fancied the challenge!
However, being able to put together a simple script like this, quickly,
enables you to rapidly prototype solutions and hopefully solve problems
with much less effort.

> Many tasks that you would have to repeat manually could be automated
> to make your life easier. This is a powerful skill to learn for cyber
> security in particular, but also comes in very handy for life in
> general!

[← Previous: 4.13 - Reading history](https://play.cyberstart.com/field-manual/8fc35358-d7eb-11eb-b062-0242ac140009)
[Next: 5.01 - Introduction to programming →](https://play.cyberstart.com/field-manual/8fc594ba-d7eb-11eb-b20b-0242ac140009)
