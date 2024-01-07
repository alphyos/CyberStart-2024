## WEB 
# Manipulating URLs

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/56136760-4d39-428d-a19e-f8079f148723" width="800" />
</div>

# Unintended consequences

A URL (Uniform Resource Locator) is a way of specifying a request address, plus perhaps data which is then received by the server, which considers the request and provides output according to logic defined in the web app. Normally when we interact with websites we click links, buttons or are redirected to various intended resources. As we do that the URL is generated and sent as the request, rather than us changing the address bar manually ourselves.

The URL structure may contain a number of parts, broken down for demonstration purposes:

`https` :// `user-login` . `example` . `com` / `login` ? `uid=1&name=john%20o%27malley`

Above, `https` is the protocol, `user-login` is the subdomain, `example` is the domain and `com` is the TLD (Top Level Domain). This all describes how the client app (our browser) should attempt to communicate with the 'host' over secure HTTP protocol to the `user-login.example.com` host. Upon looking up that host and finding the server it resides on, the host can then handle the rest of the request.

`login` is the directory or 'path' required, and we're passing through 2 data items to it. Firstly `uid` (usually short for User ID) which has a value of `1`, and `name` which has a value of `john%20o%27malley`. This last value is URL encoded so here non-alphanumeric characters are converted into a URL safe format, in this case `%20` is within the value which translates to a space character and `%27` translates to an apostrophe, so when received by the web server can be understood as 'john o'malley`.

The concept of URL manipulation is simple. We change the parts of the URL to see if we can make the web application or web server do something interesting or unintended!

For example, `uid` likely indicates a user id and has a value of 1. What happens if we try 2? Perhaps a large number like 987654321987654321 or a negative number like -1? What happens if we remove it? What happens if we specify it twice like `?uid=1&uid=2`? What about if we change it to a weird, unexpected data type like `?uid=null`. These changes might cause the application to crash or redirect us to an unusual location. That might be interesting and enable us to do something we shouldn't!

Of course, we can also change other parts of the URL. What about changing `/login` to `/admin`? Perhaps this file exists, has poor security and enables us to do something interesting! How do we know what files exist? Well, we can guess. Of course, if this is an open source application maybe we can look at other examples to figure out what might exist. We could also try scripting this and try thousands of combinations at once, in the hope one of them works. Pre-made scripts and tools can also help with this, not only to avoid work writing something ourselves but to provide well known variations to try.

> You can manually manipulate URLs, but you can also script it to find more interesting pages or conditions. A tool that can try common directory locations and manipulate URLs is called [DirBuster](https://www.kali.org/tools/dirbuster/) (by OWASP). You can also use a tool like [Burp](https://portswigger.net/burp) which can use patterns or wordlists to guess. This is a more advanced skill, but useful in the higher levels of CyberStart.

Remember that running tools and guessing how to manipulate URLs requires permission. If you do this on a website without permission **you could be breaking a local computer crime law!**

### <div dir="rtl">[→ Next: 2.5 Web Requests And HTTP](WebRequestsAndHTTP2.5.md)
