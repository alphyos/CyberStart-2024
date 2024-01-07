
## WEB
# Web Requests And HTTP

<div align="center">
 <video src="https://github.com/alphyos/CyberStart-2023/assets/116646389/055972b3-c1d1-4052-a833-efa5be45ed44" width="800" />
</div>

# HTTP

HTTP, the Hypertext Transfer Protocol, is used to transmit hypermedia documents such as HTML. It was designed for communication between web browsers and web servers, though it can be used for other purposes.

HTTP follows a client-server model: where a client will send a request to a server and wait until it receives a response. It was also a stateless protocol, meaning that HTTP itself did not maintain any data between individual requests. State has since been added with the inclusion of [Cookies](), which allow a web browser and web server to persist data between requests.

The protocol includes different **methods** that can change the way a client and server will interpret the request.

# GET and POST

GET and POST are two types of HTTP request methods. Simply put, they are just ways to get resources from a server, or ask to store or change data. There are technically other mechanisms for transferring data between web applications, but these are two of the main ones. Let us briefly discuss the key differences between each:

**GET**. GET is used to request data from a specific resource or location. A GET request would typically look something like `http://127.0.0.1/login.php?uid=1`. GET requests can remain in the browser history, they can be bookmarked, and they can potentially be shared via e-mail as links. GET should be used to request data, but sometimes applications use it to change data and this can be a security risk! Most web servers also log URL requests - that means recording the querystring, and subsequently storing the data items provided within the logs. Not ideal for users if there's sensitive data.

**POST**. POST is used to send data to a server to create or update some data. You would typically use it to send login information, for example, as unlike GET it does not turn up in the browser history or web server logs. A POST request can also handle much more data than a GET, useful for a big file upload or binary data for example!

Modifying a GET request is often as easy as modifying it in the browser address bar (though it can be trickier if you have scripts interacting with the server). POST on the other hand usually requires a little more adjustment, or the use of a tool designed to make it easy to modify the data. Your browser dev tools has a **Network** tab which allows you to see the GET and POST requests and may even have edit and resend functions to adjust and make a new request.

>If you want to try a more advanced tool, take a look at [Burp](https://portswigger.net/burp) or [ZAP](https://owasp.org/www-project-zap/) (Zed Attack Proxy). These enable you to modify data on the way out from your browser, or on the way back from the server. They are a bit more versatile than using only your browser.

Note that whilst we can modify the data being sent via GET or POST, a good web application should assume that tampering will occur and handle the exceptions. Unfortunately, that does not always happen and can lead to security flaws!

### <div dir="rtl">[→ Next: 2.6 Command Line Web Requests And Curl](CommandLineWebRequestsAndCurl.6.md)
