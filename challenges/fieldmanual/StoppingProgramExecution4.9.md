## LINUX

# Stopping program execution

This section
 is short, but important. Sometimes you start a command and it just
won't stop! Perhaps you sent it off to calculate pi to an infite number
of places? A good example is this:

```console
$ top
top - 15:51:27 up  6:34,  1 user,  load average: 0.73, 1.31, 1.47
Tasks: 552 total,   1 running, 536 sleeping,  15 stopped,   0 zombie
%Cpu(s):  2.9 us,  1.3 sy,  0.0 ni, 95.6 id,  0.0 wa,  0.0 hi,  0.2 si,  0.0 st
MiB Mem :  31953.4 total,  12456.1 free,   9597.7 used,   9899.7 buff/cache
MiB Swap:    976.0 total,    976.0 free,      0.0 used.  20265.2 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   2720 mainuser  20   0 4807024 303224 111800 S  10.5   0.9  43:26.26 shell
   2579 mainuser  20   0  749756 103404  52320 S   8.2   0.3  37:54.08 Xorg
  26238 mainuser  20   0 5268648 352428 204040 S   7.2   1.1  49:03.33 zoom
   4043 mainuser  20   0   32.6g 106508  67996 S   5.9   0.3   4:15.92 slack
   4109 mainuser  20   0   41.1g 303472 100936 S   4.9   0.9   8:42.60 slack
   5381 mainuser  20   0   32.6g 345900 190540 S   3.3   1.1  10:30.53 chrome
...
  63864 mainuser  20   0    8084    520    452 S   0.0   0.0   0:00.00 sleep
...
```

If you have ran the `top` command you will now have a
lovely list of processes on your system, updating every second. This is
great, but your shell is gone! What if you want to get back to your
prompt?

You can hit `Ctrl-C` to terminate the process. This sends a message to the process currently running in the terminal to stop it.

This may not work in every situation. If it doesn't, you need to use a tool like `kill` to terminate the process. For example, see the `sleep` command at the bottom of the processes above? For some reason someone ran this command:

```console
$ sleep 9999
```

This creates a running process that is 'sleeping' for 9999 seconds!
We can see the process ID of 63864, which we can use to kill this
process:

```console
$ kill 63864
```

The `kill` command will send the default or specified 'signal' to the process provided. It's worth noting that the default signal - `SIGTERM`, to terminate the program - doesn't always work. Instead, you can specify a particular signal with a higher *kill level*; effectively a higher authority to end the program.

A common kill command you'll see to stop a stubborn process is `kill -9 <process id>`. This sends the signal `SIGKILL`, the 'highest' level signal to stop a process.

If you're curious, you can view available signals with the `kill -l` command.

[← Previous: 4.08 - Running programs](https://play.cyberstart.com/field-manual/8fbdb7fe-d7eb-11eb-8381-0242ac140009)
[Next: 4.10 - SSH →](https://play.cyberstart.com/field-manual/8fbfeb14-d7eb-11eb-926e-0242ac140009)
