# 💰 Miguel the Moneyman - L07 C06

Agent 707, we think we know where the money for this Chiquitoo operation is coming from: one of their senior gang members, Miguel. And it's given us an idea.

To make the payments to gang members look normal, Miguel has asked them all to send him links to official looking PDF invoices, which we know he is opening on his computer and then paying. So our plan is to send him a malicious PDF disguised as an invoice from one of the gang members. But we need your help serving up the file to Miguel.

Create a web server with the terminal using Python, then finish off the email we've created by inserting the web server's location.

**Tip:** Serve the file up correctly to get the flag. Make your web server listen on port 8000 to be sure to bypass the firewall.

<details><summary>

## Need a hint?</summary>

> 💡 Hint: You need to find out the command to set up a web server with Python from the command line. When you do it correctly you'll get an IP address to add to the email.

</details>

<details><summary>

## Step by Step</summary>

- Type `python -m http.server 8000`
![setting up the web server](/assets/miguelthemoneyman1.png)
- Copy the highlighted text `http://10.10.127.202:8000`
![submitting the email](/assets/miguelthemoneyman2.png)
- Navigate to "Email" on the left of the screen
- Paste into textbox and press submit

</details>
