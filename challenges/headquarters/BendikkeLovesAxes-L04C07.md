# 🪓 Bendikke Loves Axes - L04 C07

Whilst doing some background research on one of the gang members, Bendikke, we discovered that she writes a blog all about axes. We suspect she might be using the backend of the blogging tool to store information about how they plan to attack their competitors and, more importantly, the specific machinery blueprints they are after. If we knew that, it would really help us foil the gang's plans.

See if you can find the login page on the blog and use some of the techniques you've learned already to break in.

**Tip:** If you successfully log in you'll get the flag!

<details><summary>

## Need a hint?</summary>

> 💡 Hint: It looks like she may have left herself a password hint in the source code and, luckily for us, the hint she mentions is all about what she writes on the blog.

</details>

<details><summary>

## Step by Step</summary>

- View the source code and use Ctrl + F to search for `password`.

![image of the source code](/assets/bendikkelovesaxes1.png)

- Taking a look back at the blog, a post talks about her favorite axe, `Thor`.

![image of post](/assets/bendikkelovesaxes2.png)

- Username: `Thor` Password: `rohT`.

</details>
