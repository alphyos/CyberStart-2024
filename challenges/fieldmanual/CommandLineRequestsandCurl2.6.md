## WEB
# Command line web requests and curl

<div align="center">
| <video src="" width="800" />
</div>

# curl

So far you have been using a web browser to interface with a web server, but you can use command line tools too.

>If you are not familiar with the Linux command line yet, you may want to check out the [Linux]() section of the field manual. You can get practice in CyberStart and the CyberStart Virtual Machine too. Command line skills are invaluable as you progress in cyber security, and computer science generally!

Below we introduce you to two tools - `curl` and `wget`. These enable you to access resources like a web browser would; but have the added benefit of being able to very precisely control your requests, or even script them. Also, you look so much cooler whilst doing it (bonus points if you make the screen black and the text green)!

From a Linux command line, `curl` is often available by default, and we can use it to retrieve the **robots.txt** file (the use of this file is covered later in the field manual!) from **cyberstart.com**. To do this we execute the following:

`$ curl https://cyberstart.com/robots.txt
User-agent: *`

The result is then output to the screen. If we want, we can also save this into a file. For example, if we wanted to save the **cyberstart.com** home page in to a file called **cs.html**, we would execute:

```$ curl https://cyberstart.com > cs.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 39832  100 39832    0     0   303k      0 --:--:-- --:--:-- --:--:--  303k```


One of the major benefits of `curl` and other command line tools is that they can be scripted in advanced and powerful ways. Below we give an example of brute forcing a user id using curl to send the requests. This is done with a bash loop trying numbers 1 to 100 under variable $i:

`$ for i in {1..100} do curl http://127.0.0.1/demo/login.php?uid=$i done
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>404 Not Found</title>
...`

The $i is replaced with the value of i each time the counter increases, from 1 to 100. In this way we make a request for each potential value and see the output on the screen. This is a simple version of brute forcing (trying lots of values to see if you can guess one that works)!